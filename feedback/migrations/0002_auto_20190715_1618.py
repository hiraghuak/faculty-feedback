# Generated by Django 2.2.1 on 2019-07-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ASSESSMENT_OF_LEARNING_ACTIVITY',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='ASSESSMENT_OF_LEARNING_ACTIVITY_3',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='ASSESSMENT_OF_LEARNING_ACTIVITY_4',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='ASSESSMENT_OF_LEARNING_ACTIVITY_5',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='LEARNING_ACTIVITY',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='LEARNING_ACTIVITY_2',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='LEARNING_ACTIVITY_3',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='LEARNING_ACTIVITY_4',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='LEARNING_ACTIVITY_5',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='NAME_OF_THE_LESSON',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
