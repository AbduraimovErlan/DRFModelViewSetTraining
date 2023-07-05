from django.shortcuts import render
from ModelViewSet3.serializers import ModelSerializersBooks3
from ModelViewSet3.models import Book3
from rest_framework.viewsets import ModelViewSet






class ModelViewSetBooks33(ModelViewSet):
    queryset = Book3.objects.all()
    serializer_class = ModelSerializersBooks3
    lookup_field = 'id'

