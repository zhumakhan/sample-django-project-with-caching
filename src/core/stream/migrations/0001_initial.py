# Generated by Django 2.2.9 on 2020-07-25 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='Start Time')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='End Time')),
                ('url', models.CharField(blank=True, max_length=1023, null=True)),
                ('title', models.CharField(blank=True, max_length=1023, null=True)),
            ],
        ),
    ]
