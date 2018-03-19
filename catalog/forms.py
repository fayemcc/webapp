from django import forms

from .models import Book, Location


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'isbn']


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['name', 'country', 'description']

