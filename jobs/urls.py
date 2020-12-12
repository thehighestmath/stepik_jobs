from django.urls import path, re_path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:code>/', Specialization.as_view(), name='specialization'),
    path('companies/<int:id>/', CompanyView.as_view(), name='company'),
    path('vacancies/<int:id>/', VacancyView.as_view(), name='vacancy'),

    path('vacancies/<int:id>/send/', SendView.as_view(), name='send'),
    re_path(r'^mycompany/(?P<state>create)?$', MyCompany.as_view(), name='my_company'),
    re_path(r'^mycompany/vacancies/(?P<id>\d+)?$', MyVacancies.as_view(), name='my_vacancies'),

    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
