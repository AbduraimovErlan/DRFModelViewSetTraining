from ModelViewSet1.models import Book
from ModelViewSet1.serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet





class BookAPIViewSet(ModelViewSet):
    queryset = Book.objects.all()
    lookup_field = 'id'
    serializer_class = BookSerializer












