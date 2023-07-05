from django.shortcuts import render
from ModelViewSet7.models import Book7
from ModelViewSet7.serializers import SerializerBook7
from rest_framework import viewsets


class ModelViewSetBook7(viewsets.ModelViewSet):
    queryset = Book7.objects.all()
    serializer_class = SerializerBook7
    lookup_field = 'id'
