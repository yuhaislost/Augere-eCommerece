# Generated by Django 3.2.7 on 2021-10-06 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20211005_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='listingImages/<django.db.models.fields.related.ForeignKey>/%Y/%m/%d'),
        ),
    ]
