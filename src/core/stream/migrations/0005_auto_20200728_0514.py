# Generated by Django 2.2.9 on 2020-07-28 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0004_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='current',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stream',
            name='ended',
            field=models.BooleanField(default=False),
        ),
    ]