# Generated by Django 4.2.3 on 2023-08-12 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_alter_auction_datetime_alter_bid_current_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 12, 14, 52, 59, 906750, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='bid',
            name='current_price',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
