from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Books
from .serializer import BookSerializer


class BooksAPI(APIView):
    def get(self, request, id=None):
        if id:
            books_instance = Books.objects.filter(id=id).first()
            if not books_instance:
                return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer_data = BookSerializer(books_instance).data
            return Response(serializer_data)

        books_instance = Books.objects.all()
        serializer_data = BookSerializer(books_instance, many=True).data
        return Response(serializer_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "book created successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        book_instance = Books.objects.filter(id=id).first()

        if not book_instance:
            return Response({"error": "book not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({"success": "book edited successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        book_instance = Books.objects.filter(id=id).first()

        if not book_instance:
            return Response({"error": "book not found"}, status=status.HTTP_404_NOT_FOUND)

        book_instance.delete()
        return Response({"success": "book deleted successfully"}, status=status.HTTP_200_OK)