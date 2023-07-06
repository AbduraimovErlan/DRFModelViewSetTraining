from django.shortcuts import render
from ModelViewSet12.models import Book12
from ModelViewSet12.serializers import SerializersBook12
from rest_framework import viewsets



class ModelViewSetBook12(viewsets.ModelViewSet):
    queryset = Book12.objects.all()
    serializer_class = SerializersBook12
    lookup_field = 'id'