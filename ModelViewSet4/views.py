from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from ModelViewSet4.serializers import BookSerializer4
from ModelViewSet4.models import Book4

class ModelViewSet44(ModelViewSet):
    queryset = Book4.objects.all()
    serializer_class = BookSerializer4
    lookup_field = 'id'
