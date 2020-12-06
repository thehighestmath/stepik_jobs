from django.http import Http404
from django.shortcuts import render
from django.views import View
from .models import Vacancy, Company, Specialty


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
