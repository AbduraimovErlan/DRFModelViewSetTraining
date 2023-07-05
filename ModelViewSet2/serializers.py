from rest_framework import serializers
from ModelViewSet2.models import Book2



class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book2
        fields = "__all__"