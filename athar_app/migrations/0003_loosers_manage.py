# Generated by Django 3.1.1 on 2020-09-24 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('athar_app', '0002_loosers_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='loosers',
            name='manage',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
