from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}"

class Bid(models.Model):
    current_price = models.DecimalField(decimal_places=2, max_digits=10)
    times_bid = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.current_price}"

class Auction(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    image = models.URLField(max_length=254, blank=True)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now())
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    
    def formatted_datetime(self):
        return self.datetime.strftime("%b. %d, %Y, %I:%M %p")

    def __str__(self):
        return f"{self.id}. {self.category}:{self.name} ({self.description}), {self.price}$ at {self.formatted_datetime()} by {self.listed_by}"

class Comment(models.Model):
    comments = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_discussion')
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_discussed_by')
    item = models.ForeignKey(Auction, on_delete=models.CASCADE)

class Watchlist(models.Model):
    watchlist = models.BooleanField(default=False)
    watchlisted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Auction, on_delete=models.CASCADE)    