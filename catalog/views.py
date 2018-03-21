from django.shortcuts import render
from .models import Book, Location

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django import forms

from django.contrib.auth import login, authenticate
from catalog.forms import (SignUpForm,EditProfileForm)
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

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


# User related ----------------------------------------
def signup(request):
    # POST in HTTP basically means that the user is sending data as opposed to receiving it
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = SignUpForm()

        args = {'form':form}

        return render(request, 'users/signup.html', args)


def profile(request):
    args = {'user': request.user}

    return render(request, 'users/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('my-profile')
    # Accounts for 'GET'
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'users/edit_profile.html', args)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/myprofile')
        else:
            return redirect('change-password')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'users/change_password.html', args)



# Contribution page to choose what to contribute
def contribute(request):

    return render(
        request,
        'users/contribute.html',
        context={}
    )

