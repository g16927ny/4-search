# Generated by Django 2.2.7 on 2019-12-09 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='hotelurl',
        ),
    ]
