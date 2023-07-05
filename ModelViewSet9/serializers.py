from rest_framework import serializers
from ModelViewSet9.models import Book9



class SerializerBooks9(serializers.ModelSerializer):
    class Meta:
        model = Book9
        fields = '__all__'