from django.db.models import Avg
from rest_framework import serializers
from core.models import Book
from .feedback import FeedbackSerializer


class BooksListSerializer(serializers.HyperlinkedModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    count_favorite = serializers.SerializerMethodField()
    
    url = serializers.HyperlinkedIdentityField(view_name="core:book-detail")
    genre = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    author = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['url', 'id', 'name', 'genre', 'author',
                  'avg_rating', 'count_favorite']
    
    def get_avg_rating(self, book_object):
        return book_object.feedback.aggregate(Avg('rating'))['rating__avg']

    def get_count_favorite(self, book_object):
        return book_object.favorite_for.count()


class BookDetailSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    feedback = FeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'name', 'genre', 'author', 'avg_rating',
            'publicated_date', 'description', 'feedback',
        ]
    
    def get_avg_rating(self, book_object):
        return book_object.feedback.aggregate(Avg('rating'))['rating__avg']
