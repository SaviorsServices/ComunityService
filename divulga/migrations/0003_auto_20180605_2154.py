# Generated by Django 2.0.4 on 2018-06-05 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divulga', '0002_auto_20180529_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='establishment',
            name='community_action',
        ),
        migrations.AddField(
            model_name='communityaction',
            name='establishment',
            field=models.ManyToManyField(to='divulga.Establishment'),
        ),
        migrations.AlterField(
            model_name='communityaction',
            name='close_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='communityaction',
            name='start_date',
            field=models.DateField(),
        ),
    ]