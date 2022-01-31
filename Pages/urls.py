from django.urls import path
from .views import faq
# Create your views here.
app_name='Pages'
urlpatterns = [
    path('/', faq, name='faq'),
]


