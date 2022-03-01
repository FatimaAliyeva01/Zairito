from argparse import Namespace
from django.urls import path

from Contact.views import contact
from .views import index
from Home import views
app_name='Home'
urlpatterns = [
    path('', index, name='index'),
    path('Contact/', contact, name='contact'),
    path('', index, name='index2'),
    path('', index, name='index3')
]
