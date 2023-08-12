# Generated by Django 4.2.3 on 2023-08-12 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_alter_auction_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='money',
        ),
        migrations.AlterField(
            model_name='auction',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 12, 14, 54, 3, 662279, tzinfo=datetime.timezone.utc)),
        ),
    ]