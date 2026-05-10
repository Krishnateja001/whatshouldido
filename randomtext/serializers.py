from rest_framework import serializers

from .models import ShortText


class ShortTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortText
        fields = ['id', 'text']
