from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, AuthorViewSet


router = routers.DefaultRouter()
router.register('author', AuthorViewSet, 'author')
router.register('book', BookViewSet, 'book')


urlpatterns = [
    path('', include(router.urls))
]

