from string import Template

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML
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
from django.utils.safestring import mark_safe

from jobs.models import Company, Vacancy, Application
from stepik_jobs.settings import MEDIA_URL


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        labels = {
            'username': 'Логин',
        }

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
        self.fields['username'].label = "Логин"
        self.helper.add_input(Submit(
            'submit', 'Войти', css_class='btn btn-primary btn-lg btn-block'
        ))


class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html = Template("""<img style="max-width: 120px;height: auto;" src="/$media$link"/>""")
        return mark_safe(html.substitute(media=MEDIA_URL, link=value))


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'logo', 'employee_count', 'location', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit(
            'submit', 'Сохранить', css_class='btn btn-block btn-info'
        ))
        default_url = 'https://place-hold.it/100x60'
        if args[0].get('logo') != default_url:
            url = f"{MEDIA_URL}{args[0].get('logo')}"
        else:
            url = default_url
        self.helper.layout = Layout(
            'name',
            'logo',
            HTML(f"""
            <img class="img-responsive" src="{url}" style="max-width: 120px;height: auto;">
            """, ),
            'employee_count',
            'location',
            'description',

        )


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'skills',
                  'salary_min', 'salary_max', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit(
            'submit', 'Сохранить', css_class='btn btn-block btn-info'
        ))


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit(
            'submit', 'Отправить', css_class='btn btn-block btn-info'
        ))
