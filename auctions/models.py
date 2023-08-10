from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import date


class User(AbstractUser):
    first = models.CharField(max_length=64, default='', blank=True)
    last = models.CharField(max_length=64, default='', blank=True)
    money = models.PositiveIntegerField(default=1000)

class Auction(models.Model):
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    image = models.URLField(max_length=254, blank=True)
    first_price = models.PositiveSmallIntegerField()

class Bid(models.Model):
    current_price = models.PositiveSmallIntegerField(default=1)
    times_bid = models.PositiveSmallIntegerField(default=0)
    watchlist = models.BooleanField(default=False)

class Comment(models.Model):
    comments = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Auction, on_delete=models.CASCADE)