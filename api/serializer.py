import uuid

from rest_framework.serializers import ModelSerializer

from api.models import Books


class BookSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        validated_data['id'] = uuid.uuid4()
        return Books.objects.create(**validated_data)
