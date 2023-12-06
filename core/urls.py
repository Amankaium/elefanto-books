from django.urls import path
from core.views import BooksListAPIView

app_name = 'core'

urlpatterns = [
    path('', BooksListAPIView.as_view(), name='books-list'),
]
