from rest_framework.serializers import ModelSerializer

from api.models import Books


class BookSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

