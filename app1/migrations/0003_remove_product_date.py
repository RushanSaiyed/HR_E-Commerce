# Generated by Django 4.1.1 on 2022-09-14 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
    ]
