from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.models import *


class AddFavoriteBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        book_pk = kwargs.get("book_pk")
        try:
            book_object = Book.objects.get(pk=book_pk)
        except Book.DoesNotExist as e:
            return Response(data="Объект не найден", status=404)
        book_object.favorite_for.add(request.user)
        book_object.save()
        return Response(data="Книга успешно добавлена в избранное")
