from django.urls import path
from .views import about
# Create your views here.
app_name='About'
urlpatterns = [
    path('',about, name='about'),
]


