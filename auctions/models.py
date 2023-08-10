from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    money = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return f"{self.id}. {self.username} ({self.money}$)"

class Auction(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254, default='')
    category = models.CharField(max_length=254)
    image = models.URLField(max_length=254, blank=True)
    starting_bid = models.PositiveSmallIntegerField()
    datetime = models.DateTimeField(default=timezone.now())
    
    def formatted_datetime(self):
        return self.datetime.strftime("%b. %d, %Y, %I:%M %p")

    def __str__(self):
        return f"{self.id}. {self.category}:{self.name} ({self.description}), {self.starting_bid}$ at {self.formatted_datetime()}"

class Bid(models.Model):
    current_price = models.PositiveSmallIntegerField(default=1)
    times_bid = models.PositiveSmallIntegerField(default=0)
    watchlist = models.BooleanField(default=False)

class Comment(models.Model):
    comments = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Auction, on_delete=models.CASCADE)