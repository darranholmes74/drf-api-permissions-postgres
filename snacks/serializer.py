from rest_framework import serializers
from .models import Snacks


class SnacksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'description', 'updated_at')
        model = Snacks
