from django.urls import path
from .views import Accounts
# Create your views here.
app_name='Accounts'
urlpatterns = [
    path('/',Accounts, name='accounts'),
]


