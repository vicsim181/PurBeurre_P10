# Generated by Django 3.1.7 on 2021-03-05 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_product_last_modified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='last_modified',
        ),
    ]
