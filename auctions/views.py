from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Comment, Auction, Bid


def index(request):
    return render(request, "auctions/index.html", {
        "item": Auction.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        image = request.POST["image"]
        category = request.POST["category"]
        listed_by = request.user
        bid = Bid(current_price=starting_bid, times_bid=0)
        bid.save()

        item = Auction(name=title, description=description, category=category, price=bid, image=image, listed_by=listed_by)
        item.save()
        return render(request, "auctions/index.html", {
            "item": Auction.objects.all(),
        })
    else:
        return render(request, "auctions/create.html")
    
def auction_item(request, item_id):
    item = Auction.objects.get(pk=item_id)
    return render(request, "auctions/listings.html", {
        "item": item,
        "bid": item.price
    })

def bid(request, item_id):
    item = Auction.objects.get(pk=item_id)
    # ostalo za uraditi : watchlist, zatvoriti bid, pobednicka strana, comments, categories.
    bid_price = float(request.POST["bid"])

    if bid_price > item.price.current_price:
        new_bid = Bid(current_price=bid_price, times_bid=item.price.times_bid+1)
        new_bid.save()
        item.price = new_bid
        item.save()

        return render(request, "auctions/listings.html", {
            "item": item,
            "message": "Bid updated successfully!",
            "update": True
        })
    else:
        return render(request, "auctions/listings.html", {
            "item": item,
            "message": "Bid update failed!",
            "update": False
        })

def comment(request, item_id):
    item = Auction.objects.get(pk=item_id)
    if request.method == "POST":
        print("Success")
        return render(request, "auctions/listings.html", {
            "item": item
        })


def categories(request):
    pass

def watchlist(request):
    pass