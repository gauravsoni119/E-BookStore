'''
Created on Feb 7, 2016

@author: ACER
'''
from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    '''
    Perform CRUD operations on book model.
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
 