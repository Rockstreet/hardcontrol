# Generated by Django 2.0.6 on 2018-06-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardcontrol', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hard_objects',
            name='rfid_id',
            field=models.CharField(default='', max_length=1000, verbose_name='Rfid ID'),
        ),
    ]