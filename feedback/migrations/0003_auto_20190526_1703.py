# Generated by Django 2.2.1 on 2019-05-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20190526_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='STATUS',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Review', 'Review'), ('Pending', 'Pending')], default='', max_length=150),
        ),
    ]
