'''
Created on Feb 7, 2016

@author: ACER
'''
from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    '''
    Serialize book model fields.
    '''
    class Meta:
        model = Book
        