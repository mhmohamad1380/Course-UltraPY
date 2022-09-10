from django.contrib import admin

# Register your models here.
from Users_Buying_Status.models import UsersBuysStatus


class UsersBuysStatusAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'course']


admin.site.register(UsersBuysStatus , UsersBuysStatusAdmin)
