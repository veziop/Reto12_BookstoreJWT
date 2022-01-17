from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'created_date', 'added_by_id']


class AuthorSerializer(serializers.ModelSerializer):
    # books = BookSerializer(many=True)
    #
    # def create(self, validated_data):
    #     books_data = validated_data.pop("books")
    #     author = Author.objects.create(**validated_data)
    #     for book_data in books_data:
    #         Book.objects.create(author=author, book=book_data)
    #         return author

    class Meta:
        model = Author
        fields = ['id', 'name', 'created_date', 'added_by_id'] #, 'books']
