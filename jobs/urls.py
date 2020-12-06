from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:code>', Specialization.as_view(), name='specialization'),
    path('companies/<int:id>/', CompanyView.as_view(), name='company'),
    path('vacancies/<int:id>/', VacancyView.as_view(), name='vacancy'),
]
