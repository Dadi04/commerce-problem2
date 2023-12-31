# Generated by Django 4.2.3 on 2023-08-11 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_alter_auction_datetime_alter_auction_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 11, 18, 29, 57, 918267, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='bid',
            name='current_price',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
