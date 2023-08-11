# Generated by Django 4.2.3 on 2023-08-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_bids_bid_rename_comments_comment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='type',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='auction',
            old_name='first_price',
            new_name='starting_bid',
        ),
        migrations.AddField(
            model_name='auction',
            name='description',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='first',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='last',
            field=models.CharField(default='', max_length=64),
        ),
    ]