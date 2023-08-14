from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Count, Q

from .models import User, Comment, Auction, Bid, Watchlist


def index(request):
    return render(request, "auctions/index.html", {
        "item": Auction.objects.filter(isActive=True).order_by('-datetime')
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
        # create 0th bid
        bid = Bid(current_price=starting_bid, times_bid=0, latest_bidder=request.user)
        bid.save()

        watchlist = Watchlist(watchlist=False, watchlisted_by=listed_by)
        watchlist.save()

        item = Auction(name=title, description=description, category=category, price=bid, image=image, listed_by=listed_by, isActive=True, watchlisted=watchlist)
        item.save()
        return render(request, "auctions/index.html", {
            "item": Auction.objects.filter(isActive=True).order_by('-datetime')
        })
    else:
        return render(request, "auctions/create.html")
    
def auction_item(request, item_id):
    item = Auction.objects.get(pk=item_id)

    if request.user == item.listed_by:
        return render(request, "auctions/listings.html", {
            "item": item,
            "comments": Comment.objects.filter(item=item),
            "exist": True
        })
    else: 
        return render(request, "auctions/listings.html", {
            "item": item,
            "comments": Comment.objects.filter(item=item)
        })

def bid(request, item_id):
    item = Auction.objects.get(pk=item_id)
    bid_price = float(request.POST["bid"])

    if bid_price > item.price.current_price:
        new_bid = Bid(current_price=bid_price, times_bid=item.price.times_bid+1, latest_bidder=request.user)
        new_bid.save()
        item.price = new_bid
        item.save()

        if request.user == item.listed_by: 
            return render(request, "auctions/listings.html", {
                "item": item,
                "message": "Bid updated successfully!",
                "update": True,
                "comments": Comment.objects.filter(item=item),
                "exist": True
            })
        else:
            return render(request, "auctions/listings.html", {
                "item": item,
                "message": "Bid updated successfully!",
                "update": True,
                "comments": Comment.objects.filter(item=item)
            })
    else:
        if request.user == item.listed_by: 
            return render(request, "auctions/listings.html", {
                "item": item,
                "message": "Bid update failed!",
                "update": False,
                "comments": Comment.objects.filter(item=item),
                "exist": True
            })
        else:
            return render(request, "auctions/listings.html", {
                "item": item,
                "message": "Bid update failed!",
                "update": True,
                "comments": Comment.objects.filter(item=item)
            })

def comment(request, item_id):
    item = Auction.objects.get(pk=item_id)
    user = request.user
    comment = request.POST["comment"]

    new_comment = Comment(comments=comment, commented_by=user, item=item)
    new_comment.save()
    
    if request.user == item.listed_by: 
        return render(request, "auctions/listings.html", {
            "item": item,
            "comments": Comment.objects.filter(item=item),
            "exist": True
        })
    else: 
        return render(request, "auctions/listings.html", {
            "item": item,
            "comments": Comment.objects.filter(item=item)
        })

def watchlist(request, item_id):
    item = Auction.objects.get(pk=item_id)
    user = request.user
    watchlist = item.watchlisted.watchlist
    if watchlist == False:
        change_status = Watchlist(watchlist=True, watchlisted_by=user)
        change_status.save()
        item.watchlisted = change_status
        item.save()
    elif watchlist == True:
        change_status = Watchlist(watchlist=False, watchlisted_by=user)
        change_status.save()
        item.watchlisted = change_status
        item.save()

    if user == item.listed_by:
        return render(request, "auctions/listings.html", {
            "item": item,
            "comments": Comment.objects.filter(item=item),
            "exist": True
        })
    else: 
        return render(request, "auctions/listings.html", {
            "item": item,
            "comments": Comment.objects.filter(item=item)
        })

def close_auction(request, item_id):
    item = Auction.objects.get(pk=item_id)

    if request.user == item.listed_by:
        item.isActive = False
        item.save()
        return render(request, "auctions/listings.html", {
            "item": item,
            "comments": Comment.objects.filter(item=item),
            "exist": True
        })
    else: 
        return render(request, "auctions/listings.html", {
            "item": item,
            "comment": Comment.objects.filter(item=item)
        })

def categories(request):
    # get all unique categories
    all_categories = Auction.objects.values('category').distinct()
    # count every active auction to their category
    categories_with_counts = all_categories.annotate(item_count=Count('category', filter=Q(isActive=True)))
    
    return render(request, "auctions/categories.html", {
        "categories_with_counts": categories_with_counts
    })

def category_listing(request, category_name):
    return render(request, "auctions/category_listing.html", {
        "item": Auction.objects.filter(category=category_name, isActive=True).order_by('-datetime')
    })

def watchlist_page(request):
    watchlist = Watchlist.objects.filter(watchlist=True, watchlisted_by=request.user).values_list('auction', flat=True)
    item = Auction.objects.filter(isActive=True, pk__in=watchlist)
    return render(request, "auctions/watchlist.html", {
        "item": item
    })

# TO DO CSS malo to mora lepse da izgleda (SASS da se ubaci malo)