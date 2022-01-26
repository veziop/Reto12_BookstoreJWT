from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    added_by_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    added_by_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
