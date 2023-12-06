from django.urls import path
from core.views import BooksListAPIView, BookDetailAPIView

app_name = 'core'

urlpatterns = [
    path('', BooksListAPIView.as_view(), name='books-list'),
    path('book/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]
