# Generated by Django 3.0.7 on 2020-06-19 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RatingForm',
            new_name='Rating',
        ),
    ]