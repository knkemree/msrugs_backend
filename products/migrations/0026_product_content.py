# Generated by Django 3.1.2 on 2020-10-27 20:01

from django.db import migrations
import editorjs_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content',
            field=editorjs_field.fields.EditorJSField(blank=True, null=True),
        ),
    ]
