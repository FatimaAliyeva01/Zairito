from argparse import Namespace
from django.urls import path
from .views import index
from .views import index2
from .views import index3
from Home import views
app_name='Home'
urlpatterns = [
    path('', index, name='index'),
    path('', index, name='index2.')
    
]
