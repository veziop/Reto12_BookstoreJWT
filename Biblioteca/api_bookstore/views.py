from rest_framework.viewsets import ModelViewSet
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

