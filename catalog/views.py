from django.shortcuts import render
from .models import Book, Location

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django import forms

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required


# Create your views here.

# Home (index) view
def index(request):
    # search bar
    # most viewed book
    # most viewed location

    return render(
        request,
        'index.html',
        context={}
    )


# Book related -----------------------------------------------
class BookListView(generic.ListView):

    model = Book
    paginate_by = 10


# Will get all records from the db for the 'Book' model
class BookDetailView(generic.DetailView):
    model = Book

"""
class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    permission_required = 'catalog.has_edit_rights'
    """


class BookCreate(CreateView):
    model = Book
    template_name_suffix = '_add'
    fields = '__all__'


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    permission_required = 'catalog.has_edit_rights'


# Location related ----------------------------------------
class LocationListView(generic.ListView):
    model = Location
    paginate_by = 10


class LocationDetailView(generic.DetailView):
    model = Location


class LocationCreate(CreateView):
    model = Location
    template_name_suffix = '_add'
    fields = '__all__'


"""
class LocationCreate(PermissionRequiredMixin, CreateView):
    model = Location
    fields = "__all__"
    permission_required = 'catalog.has_edit_rights'
"""


class LocationUpdate(PermissionRequiredMixin, UpdateView):
    model = Location
    fields = "__all__"
    permission_required = 'catalog.has_edit_rights'

"""
# User related ----------------------------------------
class UserCreate(CreateView):
    model = User
    template_name_suffix = '_add'
"""


