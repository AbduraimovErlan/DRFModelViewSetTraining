from django.shortcuts import render
from ModelViewSet10.serializers import SerializersBook10
from ModelViewSet10.models import Book10
from rest_framework import viewsets



class ModelViewSetBook10(viewsets.ModelViewSet):
    queryset = Book10.objects.all()
    serializer_class = SerializersBook10
    lookup_field = 'id'