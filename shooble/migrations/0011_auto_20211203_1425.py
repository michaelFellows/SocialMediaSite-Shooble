# Generated by Django 3.2.9 on 2021-12-03 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shooble', '0010_alter_profilepic_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepic',
            name='userID',
        ),
        migrations.AddField(
            model_name='profilepic',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
