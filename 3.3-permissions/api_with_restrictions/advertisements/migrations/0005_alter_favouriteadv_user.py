# Generated by Django 4.1.7 on 2023-03-03 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0004_alter_favouriteadv_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouriteadv',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creators', to='advertisements.advertisement'),
        ),
    ]
