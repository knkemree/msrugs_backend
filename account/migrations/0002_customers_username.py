# Generated by Django 3.1.2 on 2020-10-14 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='username',
            field=models.CharField(default='a', max_length=30),
            preserve_default=False,
        ),
    ]
