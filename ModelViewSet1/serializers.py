from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions
from ModelViewSet1.models import Book


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"



