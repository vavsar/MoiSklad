# Generated by Django 3.2.8 on 2021-10-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20211014_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ware',
            name='price',
            field=models.FloatField(),
        ),
    ]
