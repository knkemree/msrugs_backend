# Generated by Django 3.1.2 on 2020-10-24 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201022_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='image',
            field=models.ForeignKey(blank=True, default='img/no_image.png', null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productimage'),
        ),
    ]