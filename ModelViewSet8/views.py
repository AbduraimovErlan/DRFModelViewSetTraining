from django.shortcuts import render
from ModelViewSet8.models import Book8
from ModelViewSet8.serializers import SerializerBook8
from rest_framework import viewsets


class ModelViewSetBook8(viewsets.ModelViewSet):
    queryset = Book8.objects.all()
    serializer_class = SerializerBook8
    lookup_field = 'id'
