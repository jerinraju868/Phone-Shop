# Generated by Django 3.2.7 on 2021-12-09 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jshop_app', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='media'),
        ),
    ]
