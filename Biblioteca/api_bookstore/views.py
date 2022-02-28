from rest_framework.viewsets import ModelViewSet
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# ##### rest auth
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# @api_view(['GET'])
# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def welcome(request):
#     context = {"mensaje":"Biemvienido a la libreria!"}
#     return JsonResponse(context)


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

