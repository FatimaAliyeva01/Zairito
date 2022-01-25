from django.urls import path
from numpy import append
from .views import index
app_name='Home'
urlpatterns = [
    path('/', index, name='index'),
]
