from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import date


class User(AbstractUser):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    money = models.PositiveIntegerField()

class Auction(models.Model):
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    image = models.ImageField(upload_to='profile_pics/', height_field=600)
    first_price = models.PositiveSmallIntegerField()

class Bids(models.Model):
    current_price = models.PositiveSmallIntegerField()
    times_bid = models.PositiveSmallIntegerField()
    watchlist = models.BooleanField()

class Comments(models.Model):
    comments = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Auction, on_delete=models.CASCADE)