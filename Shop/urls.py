from django.urls import path
from .views import card
# Create your views here.
app_name='Shop'
urlpatterns = [
    path('', card, name='card'),
]


