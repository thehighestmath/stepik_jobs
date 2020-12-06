from django.db import models
from tinymce import models as tinymce_models

MAX_LENGTH = 255


# Create your models here.
class Specialty(models.Model):
    title = models.CharField(verbose_name='Название', max_length=MAX_LENGTH)
    picture = models.URLField(default='https://place-hold.it/100x60')
    code = models.CharField(verbose_name='Код', max_length=MAX_LENGTH)

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(verbose_name='Название', max_length=MAX_LENGTH)
    location = models.CharField(verbose_name='Город', max_length=MAX_LENGTH)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField(verbose_name='Информация о компании')
    employee_count = models.IntegerField(verbose_name='Количество сотрудников')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(verbose_name='Название вакансии', max_length=MAX_LENGTH)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(verbose_name='Навыки', max_length=MAX_LENGTH)
    description = tinymce_models.HTMLField(verbose_name='Текст')
    salary_min = models.IntegerField(verbose_name='Зарплата от')
    salary_max = models.IntegerField(verbose_name='Зарплата до')
    published_at = models.DateField(verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title
