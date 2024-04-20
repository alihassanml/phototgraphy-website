"""ali URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.header, name='header'),

    path('delete_item/<int:pk>', views.deleteItem, name = 'deleteItem'),
    path('navbar/', views.navbar, name='navbar'),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('footer/', views.footer, name='footer'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
  
    path('gallery/', views.gallery, name='gallery'),
    path('image_upload/',views.image_upload, name='image_upload'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
