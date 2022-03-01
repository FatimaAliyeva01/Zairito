from django.urls import path
from .views import contact
# Create your views here.
app_name='Contact'
urlpatterns = [
    path('', contact, name='Contact'),
]


