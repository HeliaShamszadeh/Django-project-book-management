from django.contrib import admin
from django.urls import include, path
from . import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name = 'index'),
    path('booklist', views.booklist, name = 'booklist'),
    path('addbook', views.addbook ,name = 'addbook'),
    path('search', views.search_book, name='search'),
    path('success', views.addbook, name='seccess'),
    path('result', views.search_book, name='result'),
    path('changeborrow/<int:id>/',views.changeborrow, name='changeborrow'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('changeborrow1/<int:id>/',views.changeborrow1, name='changeborrow1'),
    path('delete1/<int:id>/',views.delete1, name='delete1'),
]           