from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خو را وارد نمایید'}),
                               label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'لطفا پسورد خو را وارد نمایید'}),
                               label='پسورد')

class ResetPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'example@example.com'}))

class ResetPasswordNewPassword(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'رمز جدید'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'تکرار رمز'}))

    def clean_password2(self):
        pass1 = self.changed_data['password']
        pass2 = self.changed_data['password2']
        if pass1 == pass2:
            return pass1
        else:
            raise forms.ValidationError('عدم تطابق')
    def clean_username(self):
        username = self.cleaned_data['username']
        is_exist = User.objects.filter(username=username).exists()
        if not is_exist:
            raise forms.ValidationError('این نام کاربری در دسترس نیست')

        return username


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خو را وارد نمایید'}),
                               label='نام کاربری',
                               validators=[MaxLengthValidator(limit_value=20, message='باید کمتر از ۲۰ حرف باشد')])
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خو را وارد نمایید'}),
                             label='ایمیل')

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'لطفا پسورد خو را وارد نمایید'}),
                               label='پسورد')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'لطفا پسورد را تکرار نمایید'}),
                                label='تکرار پسورد')

    def clean_password2(self):
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['password2']
        if pass1 == pass2:
            return pass1
        else:
            raise forms.ValidationError('عدم تطابق رمز')

    def clean_username(self):
        username = self.cleaned_data['username']
        is_exist = User.objects.filter(username=username).exists()
        if is_exist:
            print(User.objects.filter(username=username).first())
            raise forms.ValidationError('این نام کاربری در دسترس نیست')
        else:
            return username
