from rest_framework import serializers
from ModelViewSet10.models import Book10


class SerializersBook10(serializers.ModelSerializer):
    class Meta:
        model = Book10
        fields = '__all__'