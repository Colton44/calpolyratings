# Generated by Django 2.1.2 on 2019-07-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0005_auto_20181229_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='overall_rating_num',
            field=models.IntegerField(default=0),
        ),
    ]
