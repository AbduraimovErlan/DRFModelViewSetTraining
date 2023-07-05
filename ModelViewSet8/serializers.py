from rest_framework import serializers
from ModelViewSet8.models import Book8



class SerializerBook8(serializers.ModelSerializer):
    class Meta:
        model = Book8
        fields = '__all__'