# Generated by Django 2.2.5 on 2019-10-01 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobrestapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_job',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
