from django import forms
from django.core import validators


class CommentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'کامنت خودت رو بنویس'}), required=True,
        label='کامنت', validators=[validators.MaxLengthValidator(180)])
