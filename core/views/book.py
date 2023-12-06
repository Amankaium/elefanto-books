from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Book
from core.serializers import BooksListSerializer, BookDetailSerializer
from core.filters import BookFilter


class BooksListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksListSerializer
    filterset_class = BookFilter


class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
