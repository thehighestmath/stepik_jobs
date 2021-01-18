# Generated by Django 3.1.3 on 2020-12-07 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20201202_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='https://place-hold.it/100x60', upload_to=''),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(default='https://place-hold.it/100x60', upload_to=''),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_username', models.CharField(max_length=255, verbose_name='Имя')),
                ('written_phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('written_cover_letter', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='jobs.user')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='jobs.vacancy')),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.user'),
        ),
    ]