'''
Models to store book informations.
'''
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator

from core.models import TimeStampedModel

def profile_directory_path(instance, filename):
    ''' file will be uploaded to MEDIA_ROOT/books/book_<id>/author/<filename>.'''
    return 'books/book_{0}/author/{1}'.format(instance.id, filename)

def book_directory_path(instance, filename):
    ''' file will be uploaded to MEDIA_ROOT/books/book_<id>/book/<filename>.'''
    return 'books/book_{0}/book/{1}'.format(instance.id, filename)

# Create your models here.
class Book(TimeStampedModel):
    '''
    Store books related information in to the database.
    '''
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=70)
    long_description = models.TextField()
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    price = models.FloatField()
    author = models.CharField(max_length=70)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10),])
    author_image = models.ImageField(upload_to=profile_directory_path)
    book_image = models.ImageField(upload_to=book_directory_path)

    def __unicode__(self):
        return self.title
