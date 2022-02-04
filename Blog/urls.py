from django.urls import path
from .views import blog
# Create your views here.
app_name='Blog'
urlpatterns = [
    path('',blog, name='blog'),
]


