"""Books serializers"""
from rest_framework import serializers

from books.models.models import Books
#Serializers
from .authors import AuthorsModelSerializer

class BooksModelSerializer(serializers.ModelSerializer):
    """Books model serializer"""
    id_author = serializers.StringRelatedField()
    class Meta:
        """Meta Class"""
        model = Books
        fields = (
            'id_tag_rfid',
            'title',
            'isbn',
            'language',
            'publisher',
            'status',
            'id_author',
            'alarm'
        )
