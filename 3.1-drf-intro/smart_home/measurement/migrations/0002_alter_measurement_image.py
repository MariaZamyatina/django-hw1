# Generated by Django 4.1.7 on 2023-02-24 21:12

from django.db import migrations, models
import measurement.models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=measurement.models.user_directory_path),
        ),
    ]