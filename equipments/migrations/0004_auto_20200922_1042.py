# Generated by Django 3.0.7 on 2020-09-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0003_auto_20200922_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='implementcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='implements_category'),
        ),
    ]