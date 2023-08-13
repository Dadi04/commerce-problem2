from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("create_listing", views.create, name="create"),
    path("listings/<int:item_id>", views.auction_item, name="auction_item"),
    path("listings/<int:item_id>/bid", views.bid, name="bid"),
    path("listings/<int:item_id>/comment", views.comment, name="comment"),
    path("listings/<int:item_id>/watchlist", views.watchlist, name="watchlist")
]
