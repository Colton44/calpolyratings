# Generated by Django 2.1.2 on 2019-08-01 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_profile', '0011_auto_20190801_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_profile',
            name='difficulty_rating',
        ),
        migrations.RemoveField(
            model_name='teacher_profile',
            name='evaluations',
        ),
        migrations.RemoveField(
            model_name='teacher_profile',
            name='rating_num',
        ),
        migrations.RemoveField(
            model_name='teacher_profile',
            name='total_difficulty_rating',
        ),
        migrations.RemoveField(
            model_name='teacher_profile',
            name='total_overall_rating',
        ),
    ]