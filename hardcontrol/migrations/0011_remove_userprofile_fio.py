# Generated by Django 2.0.6 on 2018-07-04 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardcontrol', '0010_userprofile_fio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='fio',
        ),
    ]