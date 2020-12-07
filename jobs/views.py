from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from .forms import UserForm, LoginForm
from .models import Vacancy, Company, Specialty
from django.contrib.auth.models import User



# Create your views here.
class HomeView(View):
    # Получите компании из базы данных и выведите все компании на главной странице
    def get(self, request, **kwargs):
        companies = Company.objects.all()
        specialities = Specialty.objects.all()
        return render(request, 'jobs/index.html', {
            'companies': companies,
            'specialities': specialities
        })


class VacanciesView(View):
    def get(self, request, **kwargs):
        specialities = Specialty.objects.all()
        specialities_list = []
        for specialty in specialities:
            vacancies = Vacancy.objects.filter(specialty__title=specialty.title)
            d = {
                'specialty': specialty,
                'vacancies': vacancies,
            }
            specialities_list.append(d)
        return render(request, 'jobs/vacancies.html', {
            'specialities_list': specialities_list,
        })


class Specialization(View):
    def get(self, request, **kwargs):
        specialty = Specialty.objects.filter(code=kwargs.get('code')).first()
        if specialty is None:
            raise Http404('Specialty does not exist')
        vacancies = Vacancy.objects.filter(specialty__code=kwargs.get('code'))
        specialities_list = [{
            'specialty': specialty,
            'vacancies': vacancies,
        }]
        return render(request, 'jobs/vacancies.html', {
            'specialities_list': specialities_list,
        })


class CompanyView(View):
    def get(self, request, **kwargs):
        company = Company.objects.filter(id=kwargs.get('id')).first()
        if company is None:
            raise Http404('Company does not exist')
        vacancies = Vacancy.objects.filter(company__id=kwargs.get('id'))
        return render(request, 'jobs/company.html', {
            'company': company,
            'vacancies': vacancies
        })


class VacancyView(View):
    def get(self, request, **kwargs):
        vacancy = Vacancy.objects.get(id=kwargs.get('id'))
        return render(request, 'jobs/vacancy.html', {
            'vacancy': vacancy,
        })


class SendView(View):
    def get(self, request, **kwargs):
        return render(request, 'jobs/sent.html')


class MyCompany(View):
    def get(self, request, **kwargs):
        return render(request, 'jobs/company.html')


class MyVacancies(View):
    def get(self, request, **kwargs):
        return render(request, 'jobs/vacancies.html')


class MyVacancy(View):
    def get(self, request, **kwargs):
        return render(request, 'jobs/vacancy.html')


class RegisterView(CreateView):
    form_class = UserForm
    success_url = '/'
    template_name = 'jobs/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)


# class RegisterView(View):
#     def get(self, request, **kwargs):
#         register_form = RegisterForm()
#         return render(request, 'jobs/register.html', {
#             'form': register_form
#         })
#
#     def post(self, request, **kwargs):
#         register_form = RegisterForm(request.POST)
#         if register_form.is_valid():
#             data = register_form.cleaned_data
#             User.objects.create(
#                 username=data['login'],
#                 first_name=data['first_name'],
#                 last_name=data['last_name'],
#                 password=data['password_1'],
#             )
#             return redirect('/')
#         else:
#             return render(request, 'jobs/register.html', {
#                 'form': register_form
#             })
#
#
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    form_class = LoginForm
    template_name = 'jobs/login.html'


class LogoutView(View):
    def get(self, request, **kwargs):
        return render(request, 'jobs/login.html')
