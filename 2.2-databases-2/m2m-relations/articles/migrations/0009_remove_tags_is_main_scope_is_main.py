# Generated by Django 4.1.6 on 2023-02-04 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_remove_scope_is_main_tags_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='is_main',
        ),
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]