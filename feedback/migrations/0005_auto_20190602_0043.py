# Generated by Django 2.2.1 on 2019-06-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20190602_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='AUDITORY',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='FINE_MOTOR',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='GROSS_MOTOR',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='STUDENTS_EXPERIENCE_VISUAL',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]