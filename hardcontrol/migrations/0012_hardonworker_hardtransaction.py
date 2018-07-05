# Generated by Django 2.0.6 on 2018-07-05 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hardcontrol', '0011_remove_userprofile_fio'),
    ]

    operations = [
        migrations.CreateModel(
            name='HardOnWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата выдачи')),
                ('select_auto', models.BooleanField(default=False, verbose_name='Выбрано автоматически')),
                ('hard_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hard_on_work_hard_id', to='hardcontrol.Hard_objects')),
                ('worker_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hard_on_work_worker_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HardTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.BooleanField(default=True, verbose_name='Выдача/Прием')),
                ('datetime', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата операции')),
                ('select_auto', models.BooleanField(default=False, verbose_name='Выбрано автоматически')),
                ('hard_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_hard_object', to='hardcontrol.Hard_objects')),
                ('worker_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_worker_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
