from .models import *
from rest_framework.serializers import ModelSerializer

class CollegeSerializer(ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class LibrarySerializer(ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'