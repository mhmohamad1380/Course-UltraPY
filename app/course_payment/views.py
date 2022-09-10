from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect
from azbankgateways import bankfactories, models as bank_models, default_settings as settings

from django.http import HttpResponse, Http404
from django.urls import reverse

from azbankgateways import bankfactories, models as bank_models, default_settings as settings

from Course_home.models import Course

# Create your views here.
from Users_Buying_Status.models import UsersBuysStatus
from .tasks import send_confirmation_mail

@login_required(login_url='/Login')
def go_to_gateway_view(request, cId):
    course = Course.objects.filter(id=cId)
    if course.first().final_price == 0:
        raise Http404()
    buyer = UsersBuysStatus.objects.filter(user=request.user, course_id=cId)
    if buyer.exists():
        return HttpResponse('شما قبلا این دوره را خریداری کرده اید.')
    if not course.exists():
        raise Http404()
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = int(course.first().final_price) * 10

    factory = bankfactories.BankFactory()
    bank = factory.auto_create()  # or factory.create(bank_models.BankType.BMI) or set identifier
    bank.set_request(request)
    bank.set_amount(amount)
    # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
    bank.set_client_callback_url(f'/callback-gateway/{course.first().id}')

    # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
    # پرداخت برقرار کنید.
    bank_record = bank.ready()

    # هدایت کاربر به درگاه بانک
    return bank.redirect_gateway()


@login_required(login_url='/Login')
def callback_gateway_view(request, cId):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        UsersBuysStatus.objects.create(user=request.user, course_id=cId)
        course = Course.objects.get(id=cId)
        if course.discount_person >= course.course_discount:
            course.final_price = course.course_price
        course.buyers_count += 1
        if course.buyers_count == course.discount_person:
            course.course_discount = 0
            course.discount_person = 0
        course.save()
        send_confirmation_mail.delay(request.user.email, cId)
        messages.success(request, 'پرداخت با موفقیت انجام شد')
        return redirect(f'/Courses-List/{course.id}/{course.name}')

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    course = Course.objects.get(id=cId)
    messages.warning(request, 'پرداخت با شکست مواجه شد ، در صورت کسر وجه ، پس از ۴۸ ساعت به حسابتان باز می گردد')
    return redirect(f'/Courses-List/{course.id}/{course.name}')
