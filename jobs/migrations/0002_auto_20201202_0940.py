# Generated by Django 3.1.3 on 2020-12-02 09:40

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Текст'),
        ),
    ]
