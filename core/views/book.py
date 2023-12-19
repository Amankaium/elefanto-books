from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Book
from core.serializers import BooksListSerializer, BookDetailSerializer
from rest_framework.permissions import IsAuthenticated
from core.filters import BookFilter


class BooksListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksListSerializer
    filterset_class = BookFilter
    # permission_classes = [IsAuthenticated]


class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
