# Generated by Django 3.2.7 on 2021-10-06 05:11

import auctions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_listings_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=auctions.models.filepath),
        ),
    ]
