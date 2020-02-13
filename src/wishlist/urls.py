from django.urls import path
from .views import WishListView, WishDetailView


app_name = "wishlist"
urlpatterns = [
    path("", WishListView.as_view(), name="list"),
    path("<slug:wish_slug>/", WishDetailView.as_view(), name="detail"),
]
