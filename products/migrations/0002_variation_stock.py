# Generated by Django 3.1.2 on 2020-10-14 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='stock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
