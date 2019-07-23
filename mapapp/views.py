from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class CollegeViewSet(viewsets.ModelViewSet):
    serializer_class = CollegeSerializer
    queryset = College.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class LibraryViewSet(viewsets.ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()


