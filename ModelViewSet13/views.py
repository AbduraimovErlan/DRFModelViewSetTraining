from django.shortcuts import render
from rest_framework import viewsets
from ModelViewSet13.models import Book13
from ModelViewSet13.serializers import SerializersBook13



class ModelViewSetBook13(viewsets.ModelViewSet):
    queryset = Book13.objects.all()
    serializer_class = SerializersBook13
    lookup_field = 'id'
