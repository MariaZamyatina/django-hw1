# Generated by Django 4.1.7 on 2023-03-03 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0005_alter_favouriteadv_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'verbose_name': 'объявление', 'verbose_name_plural': 'объявления'},
        ),
        migrations.AlterModelOptions(
            name='favouriteadv',
            options={'verbose_name': 'избранное', 'verbose_name_plural': 'избранные'},
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.TextField(choices=[("<class 'advertisements.models.AdvertisementStatusChoices.Meta'>", 'Meta'), ('OPEN', 'Открыто'), ('CLOSED', 'Закрыто')], default='OPEN'),
        ),
        migrations.AlterField(
            model_name='favouriteadv',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
