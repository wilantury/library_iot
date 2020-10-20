"""Operations serializer"""
#DRF
from rest_framework import serializers

#Models
from books.models.models import Operations, Books

#Serializers
from .books import BooksModelSerializer

class OperationsModelSerializer(serializers.ModelSerializer):
    """Operations model serializer"""
    #books = serializers.StringRelatedField(many=True)
    books = BooksModelSerializer(many=True)
    id_user = serializers.StringRelatedField()
    class Meta:
        """Meta class"""
        model = Operations
        fields = (
            'id_user',
            'date_borrowed',
            'date_returned',
            "books"
        )
        #extra_kwargs = {'books':{'required':False}}
