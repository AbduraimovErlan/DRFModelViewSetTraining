from django.shortcuts import render
from ModelViewSet5.models import Book5
from ModelViewSet5.serializers import SerializersBook5
from rest_framework import viewsets



class ModelViewSetBook5(viewsets.ModelViewSet):
    queryset = Book5.objects.all()
    serializer_class = SerializersBook5
    lookup_field = 'id'
