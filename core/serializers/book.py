from django.db.models import Avg
from rest_framework import serializers
from core.models import Book


class BooksListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'name', 'genre', 'author', 'avg_rating']
    
    def get_avg_rating(self, book_object):
        return book_object.feedback.aggregate(Avg('rating'))['rating__avg']
