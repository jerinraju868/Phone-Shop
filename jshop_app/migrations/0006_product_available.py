# Generated by Django 3.2.7 on 2021-12-09 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jshop_app', '0005_alter_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
