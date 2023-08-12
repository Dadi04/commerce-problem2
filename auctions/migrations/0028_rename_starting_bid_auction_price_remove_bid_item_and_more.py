# Generated by Django 4.2.3 on 2023-08-12 15:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_alter_auction_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='starting_bid',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='item',
        ),
        migrations.AddField(
            model_name='auction',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 12, 15, 42, 22, 122125, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='bid',
            name='current_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auction'),
        ),
    ]