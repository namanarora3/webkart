# Generated by Django 3.2.20 on 2023-08-28 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
