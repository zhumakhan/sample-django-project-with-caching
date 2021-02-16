# Generated by Django 2.2.9 on 2020-11-19 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0010_auto_20201119_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='currency',
            field=models.CharField(choices=[('KZT', 'KZT'), ('RUB', 'RUB'), ('USD', 'USD')], default='KZT', max_length=250, verbose_name='currency'),
        ),
        migrations.AlterField(
            model_name='stream',
            name='ticket_cost',
            field=models.FloatField(verbose_name='ticket cost'),
        ),
    ]