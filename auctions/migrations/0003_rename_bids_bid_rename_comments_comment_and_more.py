# Generated by Django 4.2.3 on 2023-08-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction_bids_user_first_user_last_user_money_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bids',
            new_name='Bid',
        ),
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.URLField(blank=True, max_length=254),
        ),
    ]
