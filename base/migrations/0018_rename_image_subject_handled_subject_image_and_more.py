# Generated by Django 4.1.4 on 2023-01-16 04:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_faculty_details_date_of_join'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject_handled',
            old_name='image',
            new_name='subject_image',
        ),
        migrations.AlterField(
            model_name='faculty_details',
            name='date_of_join',
            field=models.DateField(default=datetime.datetime(2023, 1, 16, 9, 52, 47, 778518)),
        ),
    ]
