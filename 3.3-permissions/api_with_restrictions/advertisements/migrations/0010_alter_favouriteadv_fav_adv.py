# Generated by Django 4.1.7 on 2023-03-04 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0009_rename_creator_favouriteadv_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouriteadv',
            name='fav_adv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adv', to='advertisements.advertisement'),
        ),
    ]
