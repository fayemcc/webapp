"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import re_path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from catalog import views
from django.contrib.auth.views import login, logout

# Main
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls'), name='catalog'),
    # User related
    re_path(r'^myprofile/$', views.profile, name='my-profile'),
    re_path(r'^myprofile/edit/$', views.edit_profile, name='edit-profile'),
    re_path(r'myprofile/change-password/$', views.change_password, name='change-password'),
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    path('logout', logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    # User contributions
    path('mycontributions/', views.contribute, name='contribute-choose'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

