# Generated by Django 3.1.3 on 2020-11-30 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('location', models.CharField(max_length=64, verbose_name='Город')),
                ('logo', models.URLField(default='https://place-hold.it/100x60')),
                ('description', models.TextField(verbose_name='Информация о компании')),
                ('employee_count', models.IntegerField(verbose_name='Количество сотрудников')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название')),
                ('picture', models.URLField(default='https://place-hold.it/100x60')),
                ('code', models.CharField(max_length=64, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'Специализация',
                'verbose_name_plural': 'Специализации',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название вакансии')),
                ('skills', models.CharField(max_length=64, verbose_name='Навыки')),
                ('description', models.TextField(verbose_name='Текст')),
                ('salary_min', models.IntegerField(verbose_name='Зарплата от')),
                ('salary_max', models.IntegerField(verbose_name='Зарплата до')),
                ('published_at', models.DateField(verbose_name='Опубликовано')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='jobs.company')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='jobs.specialty')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
