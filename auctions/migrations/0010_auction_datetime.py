# Generated by Django 4.2.3 on 2023-08-10 19:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_auction_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 21, 45, 33, 454397)),
        ),
    ]
