# Generated by Django 3.1.2 on 2020-10-28 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_remove_product_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='clearance',
        ),
    ]
