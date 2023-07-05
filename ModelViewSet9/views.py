from django.shortcuts import render
from ModelViewSet9.serializers import SerializerBooks9
from ModelViewSet9.models import Book9
from rest_framework import viewsets



class ModelViewSetBook9(viewsets.ModelViewSet):
    queryset = Book9.objects.all()
    serializer_class = SerializerBooks9
    lookup_field = 'id'
