from django.shortcuts import render
from rest_framework import viewsets
from ModelViewSet11.models import Book11
from ModelViewSet11.serializers import SerializersBook11




class ModelViewSetBook11(viewsets.ModelViewSet):
    queryset = Book11.objects.all()
    serializer_class = SerializersBook11
    lookup_field = 'id'