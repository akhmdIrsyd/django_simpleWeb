from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.About, name='about'),
    path('galery', views.Galery, name='galery'),
    path('berita', views.Berita, name='berita'),
    path('kontak', views.Kontak, name='kontak'),
    path('detail_berita/<int:pk>/', views.detail_berita, name='detail_berita'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)