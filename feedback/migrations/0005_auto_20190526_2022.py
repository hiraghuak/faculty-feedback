# Generated by Django 2.2.1 on 2019-05-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20190526_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='AUDITORY',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='', max_length=150),
        ),
    ]
