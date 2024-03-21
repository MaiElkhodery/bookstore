from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
        
class BookApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
class BooksListApi(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
class BookCreateApi(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()