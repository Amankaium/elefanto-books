from django.urls import path
from core.views import BooksListAPIView, BookDetailAPIView, AddFavoriteBookAPIView

app_name = 'core'

urlpatterns = [
    path('', BooksListAPIView.as_view(), name='books-list'),
    path('book/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('add-favorite/<int:book_pk>/', AddFavoriteBookAPIView.as_view(), name='add-favorite'),
]
