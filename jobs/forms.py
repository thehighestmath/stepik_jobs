from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.models import User

# class RegisterForm(forms.Form):
#     login = forms.CharField(label='Логин', min_length=5)
#     first_name = forms.CharField(label='Имя', min_length=5)
#     last_name = forms.CharField(label='Фамилия', min_length=7)
#     password_1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, min_length=8)
#     password_2 = forms.CharField(label='Пароль ещё раз', widget=forms.PasswordInput, min_length=8)
#
#     def clean(self):
#         cleaned_data = self.cleaned_data
#         password1 = cleaned_data.get("password_1")
#         password2 = cleaned_data.get("password_2")
#         print(password1)
#         print(password2)
#         if password1 != password2:
#             raise forms.ValidationError("Пароли должны быть одинаковыми")
#
#         return cleaned_data
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#
#         # self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Зарегистрироваться'))


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(Submit(
            'submit', 'Зарегистрироваться', css_class='btn btn-primary btn-lg btn-block'
        ))


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(Submit(
            'submit', 'Войти', css_class='btn btn-primary btn-lg btn-block'
        ))
