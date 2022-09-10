from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from captcha.fields import ReCaptchaV3, ReCaptchaField

from User.models import User


class LoginForms(forms.Form):
    captcha = ReCaptchaField(label='امنیت سایت', widget=ReCaptchaV3(api_params={
        'hl': 'fa'
    },
    ), error_messages={
        'required': 'مشکلی پیش آمده است'
    })

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'لطفا نام کاربری خود را وارد کنید'}),
        label='نام کاربری', required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'لطفا کلمه عبور خود را وارد کنید'}),
        label='کلمه عبور',
        validators=[validators.MinLengthValidator(8)], required=True)


class RegisterForms(forms.Form):
    captcha = ReCaptchaField(label='امنیت سایت ', widget=ReCaptchaV3(api_params={'hl': 'fa'}),
                             error_messages={'required': 'مشکلی پیش آمده است'})
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'لطفا نام کاربری خود را وارد کنید',
                                      'style': 'text-align:left'}),
        label='نام کاربری', required=True)
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'لطفا ایمیل خود را وارد کنید',
                                       'style': 'text-align:left'}),
        label='ایمیل', required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'لطفا کلمه عبور خود را وارد کنید',
                                          'style': 'text-align:left'}),
        label='کلمه عبور',
        validators=[validators.MinLengthValidator(8)], required=True)
    re_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'لطفا کلمه عبور خود را دوباره وارد کنید',
                   'style': 'text-align:left'}),
        label='تکرار کلمه عبور',
        validators=[validators.MinLengthValidator(8)], required=True)

    def clean_re_password(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']

        if password != re_password:
            raise ValidationError('کلمات عبور یکی نیستند')
        return password, re_password

    def clean_email(self):
        email = self.cleaned_data['email']

        email_exists = User.objects.filter(email__iexact=email).exists()
        if email_exists:
            raise ValidationError('این ایمیل تکراری است')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']

        username_exists = User.objects.filter(username__iexact=username).exists()
        if username_exists:
            raise ValidationError('نام تکراری در دسترس نیست')
        return username
