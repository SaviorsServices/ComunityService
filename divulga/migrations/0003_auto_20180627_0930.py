# Generated by Django 2.0.4 on 2018-06-27 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divulga', '0002_voluntaryservice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voluntaryservice',
            name='closeHour',
        ),
        migrations.RemoveField(
            model_name='voluntaryservice',
            name='openHour',
        ),
    ]
