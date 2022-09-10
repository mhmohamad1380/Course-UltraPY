from django import forms
from django.core.exceptions import ValidationError
from captcha.fields import ReCaptchaField, ReCaptchaV3


class ChangePassword(forms.Form):
    captcha = ReCaptchaField(label='امنیت سایت', widget=ReCaptchaV3(api_params={'hl': 'fa'}),
                             error_messages={'required': 'مشکلی پیش آمده است'})
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'کلمه عبور جدید خود را وارد نمایید'}),
        label='کلمه عبور جدید')
    re_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'تکرار کلمه عبور جدید خود را وارد نمایید'}),
        label='تکرار کلمه عبور جدید')

    def clean_re_password(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if password != re_password:
            raise ValidationError('کلمات عبور برابر نیستند')
        return password, re_password
