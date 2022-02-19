from django.urls import path
from .views import item_list
# # Create your views here.
# app_name='Accounts'
urlpatterns = [
    path('',item_list, name='item-list'),
]


