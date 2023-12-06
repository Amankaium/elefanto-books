from django_filters import rest_framework as filters
from core.models import Book


class BookFilter(filters.FilterSet):
    publicated_date_from = filters.DateFilter(
        field_name='publicated_date',
        lookup_expr='gte',   
        label='Дата публикации с'
    )

    publicated_date_to = filters.DateFilter(
        field_name='publicated_date',
        lookup_expr='lte', 
        label='Дата публикации до'  
    )

    class Meta:
        model = Book
        fields = (
            'genre',
            'author',
            'publicated_date_from',
            'publicated_date_to',
        )

