from rest_framework import viewsets
from ModelViewSet2.models import Book2
from ModelViewSet2.serializers import BookSerializers


class Book2ModelViewSet(viewsets.ModelViewSet):
    queryset = Book2.objects.all()
    serializer_class = BookSerializers
    lookup_field = 'id'