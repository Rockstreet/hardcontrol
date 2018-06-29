# Generated by Django 2.0.6 on 2018-06-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardcontrol', '0005_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='foto',
            field=models.ImageField(blank=True, upload_to='images/users', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='passport',
            field=models.CharField(blank=True, default='', max_length=1000, verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='template1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='template10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='template2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='template3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='template4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='template5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='template6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='template7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='template8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='template9',
            field=models.TextField(blank=True, null=True),
        ),
    ]