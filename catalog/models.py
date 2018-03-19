from django.db import models
from django.urls import reverse # to generate URLs by reversing URL patterns

# For user
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save # signals allows to update etc..


# Model representing a book
class Book(models.Model):

    # Fields
    title = models.CharField(max_length=200)
    # author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=200, null=False, default='No author', blank=False)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book.')
    isbn = models.CharField(max_length=13,
                            help_text='13 character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number.</a>')
    # locations = models.ManyToManyField(Location)

    # Return the url to access a particular book instance
    def get_absolute_url(self):
        return reverse('book-details', args=[str(self.id)])

    def __str__(self):
        return self.title

"""
# Model representing book author
class Author(models.Model):

    # Fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    dod = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    # Get the url to access a particular author instance
    def get_absolute_url(self):
        return reverse('author-details', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

"""


# Model representing location
class Location(models.Model):

    # Fields
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True, null=True, help_text='A short description of the location.')

    class Meta:
        ordering = ["name", "country"]

    def get_absolute_url(self):
        return reverse('location-details', args=[str(self.id)])

    def __str__(self):
        return f'{self.name} ,{self.country}'

"""
# Model representing country
class Country(models.Model):

    # Fields
    country_name = models.CharField(max_length=50)

    class Meta:
        ordering = ["country_name"]

    def get_absolute_url(self):
        return reverse('country-detail', args=[str(self.id)])

    def __str__(self):
        return self.country_name


# Model representing city/other non-country place
class City(models.Model):

    # Fields
    name = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('city-detail', args=[str(self.id)])

    def __str__(self):
        return f'{name}, {country}'
"""

# Model representing location
#class Location(models.Model):
#
    # Fields
    #? location_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#    description = models.TextField(max_length=200, help_text="A brief description of a location.")
#

"""
class UserProfile(models.Model):

    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    dob = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.created(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
"""