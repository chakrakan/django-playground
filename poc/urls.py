from django.urls import path

from .views import index, about, item_list, item_list_drf, item_detail

urlpatterns = [
    path('', index),
    path('about/', about),
    path('item-list/', item_list),
    path('item-list-drf/', item_list_drf),
    path('<int:pk>/', item_detail),
]