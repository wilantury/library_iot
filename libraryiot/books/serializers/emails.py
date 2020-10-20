"""Books serializers"""
from rest_framework import serializers

from books.models.models import Alertemail

class EmailModelSerializer(serializers.ModelSerializer):
    """Email model serializer"""
    class Meta:
        """Meta Class"""
        model = Alertemail
        fields = (
            'email',
        )
