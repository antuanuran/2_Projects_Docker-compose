# Generated by Django 4.1 on 2023-04-26 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_alter_phone_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateTimeField(max_length=20),
        ),
    ]