from rest_framework import serializers
from todo.models.category import CategoryEntity

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryEntity
        fields = ('id', 'name', 'description')