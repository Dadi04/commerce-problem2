# Generated by Django 4.2.3 on 2023-08-13 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0036_alter_auction_datetime_alter_bid_latest_bidder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 13, 19, 14, 23, 17000, tzinfo=datetime.timezone.utc)),
        ),
    ]