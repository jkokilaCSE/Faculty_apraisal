# Generated by Django 4.1.4 on 2023-01-16 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_faculty_details_bio_faculty_details_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_details',
            name='date_of_join',
            field=models.DateField(default=datetime.datetime(2023, 1, 16, 11, 15, 43, 333503)),
        ),
    ]
