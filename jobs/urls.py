from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:code>/', Specialization.as_view(), name='specialization'),
    path('companies/<int:id>/', CompanyView.as_view(), name='company'),
    path('vacancies/<int:id>/', VacancyView.as_view(), name='vacancy'),

    path('vacancies/<int:id>/send/', SendView.as_view(), name='send'),
    path('mycompany/', MyCompany.as_view(), name='my_company'),
    path('mycompany/vacancies/', MyVacancies.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/<int:id>/', MyVacancy.as_view(), name='my_vacancy'),

    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
