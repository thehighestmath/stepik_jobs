from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from .forms import RegisterForm, LoginForm, CompanyForm, VacancyForm, ApplicationForm
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
            'send_form': ApplicationForm(),
        })


class SendView(View):
    def post(self, request, **kwargs):
        send_form = ApplicationForm(request.POST)
        if send_form.is_valid():
            send_form = send_form.save(commit=False)
            print(send_form.__dict__)
            send_form.__dict__['vacancy_id'] = kwargs.get('id')
            send_form.__dict__['user_id'] = request.user.id
            send_form.save()
        return render(request, 'jobs/sent.html', kwargs)


class MyCompany(View):
    def get(self, request, **kwargs):
        if kwargs:
            if kwargs.get('state') == 'create':
                Company.objects.create(
                    name='Название компании',
                    location='Расположение',
                    employee_count='0',
                    description='Описание',
                    owner=request.user
                )
                return redirect('/mycompany/')
        company = Company.objects.filter(owner=request.user).first()
        if company:
            company_form = CompanyForm(company.__dict__)
            return render(request, 'jobs/company-edit.html', {
                'company': company,
                'company_form': company_form
            })
        return render(request, 'jobs/company-create.html')

    def post(self, request, **kwargs):
        company_form = CompanyForm(request.POST, request.FILES)
        if company_form.is_valid():
            company_form = company_form.save(commit=False)
            company = Company.objects.get(owner=request.user)
            company.name = company_form.name
            if company_form.logo != 'https://place-hold.it/100x60':
                company.logo = company_form.logo
            company.employee_count = company_form.employee_count
            company.location = company_form.location
            company.description = company_form.description
            company.save()
            return render(request, 'jobs/company-edit.html', {
                'company': company,
                'company_form': CompanyForm(company.__dict__)
            })
        # company = Company.objects.filter(owner=request.user).first()
        # if company:
        #     return render(request, 'jobs/company-edit.html', {
        #         'company': company
        #     })
        return render(request, 'jobs/company-edit.html')


class MyVacancies(View):
    def get(self, request, **kwargs):
        if kwargs:
            id_ = kwargs.get('id')
            if id_:
                vacancy = Vacancy.objects.filter(id=id_).first()
                vacancy.__dict__['specialty'] = Specialty.objects.get(
                    id=vacancy.__dict__['specialty_id']
                )
                vacancy_form = VacancyForm(vacancy.__dict__)
                return render(request, 'jobs/vacancy-edit.html', {
                    'vacancy': vacancy,
                    'vacancy_form': vacancy_form
                })
        vacancies = Vacancy.objects.filter(company__owner=request.user)
        return render(request, 'jobs/vacancy-list.html', {
            'vacancies': vacancies
        })

    def post(self, request, **kwargs):
        if kwargs:
            id_ = kwargs.get('id')
            if id_:
                vacancy_form = VacancyForm(request.POST)
                if vacancy_form.is_valid():
                    vacancy_form = vacancy_form.save(commit=False)
                    vacancy = Vacancy.objects.filter(id=id_)
                    vacancy_form.__dict__.pop('_state')
                    vacancy_form.__dict__.pop('published_at')
                    vacancy.update(**vacancy_form.__dict__)
                    vacancy.save()
                    vacancy.__dict__['specialty'] = Specialty.objects.get(
                        id=vacancy.__dict__['specialty_id']
                    )
                    return render(request, 'jobs/vacancy-edit.html', {
                        'vacancy': None,
                        'vacancy_form': VacancyForm(vacancy.__dict__)
                    })
        # company = Company.objects.filter(owner=request.user).first()
        # if company:
        #     return render(request, 'jobs/company-edit.html', {
        #         'company': company
        #     })
        return render(request, 'jobs/vacancy-edit.html')


class MyVacancy(View):
    def get(self, request, **kwargs):
        return render(request, 'jobs/vacancy.html')


class RegisterView(CreateView):
    form_class = RegisterForm
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

