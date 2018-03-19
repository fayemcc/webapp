from django.contrib import admin

from .models import Book, Location #Author , Country, City
# Register your models here.

admin.site.register(Book)
admin.site.register(Location)
#admin.site.register(Author)
#admin.site.register(Country)
#admin.site.register(City)
