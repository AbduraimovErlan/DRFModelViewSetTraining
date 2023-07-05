from rest_framework import serializers
from ModelViewSet4.models import Book4


class BookSerializer4(serializers.ModelSerializer):
    class Meta:
        model = Book4
        fields = '__all__'