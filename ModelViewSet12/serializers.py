from rest_framework import serializers
from ModelViewSet12.models import Book12




class SerializersBook12(serializers.ModelSerializer):
    class Meta:
        model = Book12
        fields = '__all__'