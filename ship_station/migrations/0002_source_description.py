# Generated by Django 3.1.2 on 2021-03-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship_station', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
