# Generated by Django 2.2.7 on 2019-12-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelname', models.CharField(max_length=20)),
                ('nearstation', models.CharField(max_length=10)),
                ('hotelurl', models.TextField(max_length=200)),
            ],
        ),
    ]
