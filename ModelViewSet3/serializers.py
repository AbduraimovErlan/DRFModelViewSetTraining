from ModelViewSet3.models import Book3
from rest_framework.serializers import ModelSerializer


class ModelSerializersBooks3(ModelSerializer):
    class Meta:
        model = Book3
        fields = '__all__'