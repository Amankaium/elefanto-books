from rest_framework.generics import ListAPIView
from core.models import Book
from core.serializers import BooksListSerializer
from core.filters import BookFilter


class BooksListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksListSerializer
    filterset_class = BookFilter
