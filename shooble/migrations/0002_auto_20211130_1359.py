# Generated by Django 3.2.9 on 2021-11-30 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shooble', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='following',
            name='userID',
        ),
        migrations.AddField(
            model_name='following',
            name='userFollower',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
