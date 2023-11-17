from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("logout/", views.logout, name="logout"),
    path("<str:product_name>/detail", views.detail, name="detail"),
    path("category/<str:category>", views.category, name="category"),
    path("mypage/", views.mypage, name="mypage"),
    path("cart/<str:order_list>", views.cart, name="cart"),
    path("best/", views.best, name="best"),
    path("search/", views.search, name="search"),

]