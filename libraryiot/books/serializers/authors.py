"""Authors serializers"""
from rest_framework import serializers

from books.models.models import Authors

class AuthorsModelSerializer(serializers.ModelSerializer):
    """Authors model serializer"""
    class Meta:
        """Meta Class"""
        model = Authors
        fields = (
            'nationality',
            'name'
        )
