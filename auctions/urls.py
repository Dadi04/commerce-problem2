from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("watchlist_page", views.watchlist_page, name="watchlist_page"),
    path("create_listing", views.create, name="create"),
    path("listings/<int:item_id>", views.auction_item, name="auction_item"),
    path("listings/<int:item_id>/bid", views.bid, name="bid"),
    path("listings/<int:item_id>/comment", views.comment, name="comment"),
    path("listings/<int:item_id>/watchlist", views.watchlist, name="watchlist"),
    path("listings/<int:item_id>/close", views.close_auction, name="close_auction"),
    path("category/<str:category_name>", views.category_listing, name="category_listing")
]
