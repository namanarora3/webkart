# Generated by Django 3.2.20 on 2023-08-27 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='des',
            field=models.TextField(default='naman'),
        ),
    ]
