from django.contrib.auth.models import User
from django.db import models
from tinymce import models as tinymce_models

from stepik_jobs.settings import MEDIA_SPECIALITY_IMAGE_DIR, MEDIA_COMPANY_IMAGE_DIR

MAX_LENGTH = 255


class Specialty(models.Model):
    title = models.CharField(verbose_name='Название', max_length=MAX_LENGTH)
    picture = models.ImageField(default='https://place-hold.it/100x60', upload_to=MEDIA_SPECIALITY_IMAGE_DIR,
                                blank=True)
    code = models.CharField(verbose_name='Код', max_length=MAX_LENGTH)

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(verbose_name='Название', max_length=MAX_LENGTH)
    location = models.CharField(verbose_name='Город', max_length=MAX_LENGTH)
    logo = models.ImageField(verbose_name='Логотип', default=MEDIA_COMPANY_IMAGE_DIR + '/100x60.png',
                             upload_to=MEDIA_COMPANY_IMAGE_DIR, blank=True)
    description = models.TextField(verbose_name='Информация о компании')
    employee_count = models.IntegerField(verbose_name='Количество сотрудников')
    owner = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, blank=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(verbose_name='Название вакансии', max_length=MAX_LENGTH)
    specialty = models.ForeignKey(Specialty, verbose_name='Специальность', on_delete=models.CASCADE,
                                  related_name="vacancies")
    company = models.ForeignKey(Company, verbose_name='Компания', on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(verbose_name='Навыки', max_length=MAX_LENGTH)
    description = tinymce_models.HTMLField(verbose_name='Описание')
    salary_min = models.IntegerField(verbose_name='Зарплата от')
    salary_max = models.IntegerField(verbose_name='Зарплата до')
    published_at = models.DateField(verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title


class Application(models.Model):
    written_username = models.CharField(verbose_name='Имя', max_length=MAX_LENGTH)
    written_phone = models.CharField(verbose_name='Телефон', max_length=MAX_LENGTH)
    written_cover_letter = models.TextField(verbose_name='Сопроводительное письмо')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'

    def __str__(self):
        return self.written_username
