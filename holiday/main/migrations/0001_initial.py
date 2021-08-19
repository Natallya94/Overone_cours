# Generated by Django 3.2.6 on 2021-08-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, verbose_name='Имя')),
                ('lname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('data', models.EmailField(max_length=254, verbose_name='дата')),
            ],
            options={
                'verbose_name': 'Подпищик',
                'verbose_name_plural': 'Подпищики',
            },
        ),
    ]