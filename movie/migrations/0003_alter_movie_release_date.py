# Generated by Django 3.2.8 on 2021-10-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20211024_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(),
        ),
    ]
