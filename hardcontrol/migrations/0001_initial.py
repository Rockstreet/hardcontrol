# Generated by Django 2.0.6 on 2018-06-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hard_objects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edited_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата редактирования')),
                ('title', models.CharField(default='', max_length=1000, verbose_name='Наименование оборудования')),
                ('meta_description', models.CharField(blank=True, max_length=1000, verbose_name='Описание оборудования')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Оборудование',
                'ordering': ['title'],
            },
        ),
    ]