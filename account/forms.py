from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from account.models import Profile


class UserRegisterationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError('Passwords are not match')

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This email is already exist.')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('This username is already exist')
        return username


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ('age', 'bio')