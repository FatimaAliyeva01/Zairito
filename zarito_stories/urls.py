"""zarito_stories URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

#from zarito_stories.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Accounts/', include('allauth.urls')),
    path('Home/',include('Home.urls',namespace='Home')),
    path('Shop/',include('Shop.urls',namespace='Shop')),
    path('Pages/',include('Pages.urls',namespace='Pages')),
    path('Contact/',include('Contact.urls',namespace='Contact')),
    path('About/',include('About.urls',namespace='About')),
    path('Blog/',include('Blog.urls',namespace='Blog'))
    #path('Accounts/',include('Accounts.urls',namespace='Accounts'))
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [path('__debug__/',include(debug_toolbar.urls))]
