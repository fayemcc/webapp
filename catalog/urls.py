from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Books
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-details'),
    path('mycontributions/add/book/', views.BookCreate.as_view(), name='add-book'),
    # Locations
    path('locations/', views.LocationListView.as_view(), name='locations'),
    path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-details'),
    path('mycontributions/add/location/', views.LocationCreate.as_view(), name='add-location'),

]
