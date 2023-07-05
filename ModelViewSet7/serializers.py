from rest_framework import serializers
from ModelViewSet7.models import Book7



class SerializerBook7(serializers.ModelSerializer):
    class Meta:
        model = Book7
        fields = '__all__'