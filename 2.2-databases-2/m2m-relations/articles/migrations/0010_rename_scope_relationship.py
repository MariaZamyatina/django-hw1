# Generated by Django 4.1.6 on 2023-02-04 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_remove_tags_is_main_scope_is_main'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Scope',
            new_name='Relationship',
        ),
    ]
