# Generated by Django 3.2.9 on 2021-12-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooble', '0009_auto_20211203_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepic',
            name='userID',
            field=models.IntegerField(null=True),
        ),
    ]
