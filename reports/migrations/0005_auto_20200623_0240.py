# Generated by Django 3.0.7 on 2020-06-23 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20200622_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itstaff',
            old_name='employement_number',
            new_name='employee_number',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='employement_number',
            new_name='employee_number',
        ),
    ]
