from django.shortcuts import render
from ModelViewSet6.models import Book6
from ModelViewSet6.serializers import SerializersBook6
from rest_framework import viewsets

class ModelViewSerBook6(viewsets.ModelViewSet):
    queryset = Book6.objects.all()
    serializer_class = SerializersBook6
    lookup_field = 'id'
