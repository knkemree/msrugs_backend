# Generated by Django 3.1.2 on 2021-03-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ship_station', '0003_delete_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
