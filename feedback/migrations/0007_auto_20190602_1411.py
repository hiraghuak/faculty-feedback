# Generated by Django 2.2.1 on 2019-06-02 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_auto_20190602_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='INSTRUCTIONAL_OBJECTIVE_1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='INSTRUCTIONAL_OBJECTIVE_2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='INSTRUCTIONAL_OBJECTIVE_3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='INSTRUCTIONAL_OBJECTIVE_4',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='INSTRUCTIONAL_OBJECTIVE_5',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]