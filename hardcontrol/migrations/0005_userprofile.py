# Generated by Django 2.0.6 on 2018-06-29 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hardcontrol', '0004_hard_objects'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='images/users', verbose_name='Фото')),
                ('passport', models.CharField(default='', max_length=1000, verbose_name='Номер паспорта')),
                ('template1', models.TextField(null=True)),
                ('template2', models.TextField(null=True)),
                ('template3', models.TextField(null=True)),
                ('template4', models.TextField(null=True)),
                ('template5', models.TextField(null=True)),
                ('template6', models.TextField(null=True)),
                ('template7', models.TextField(null=True)),
                ('template8', models.TextField(null=True)),
                ('template9', models.TextField(null=True)),
                ('template10', models.TextField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='related_name_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
