from django.urls import path
from .views import contact
# Create your views here.
app_name='contact'
urlpatterns = [
    path('/', contact, name='contact'),
]


