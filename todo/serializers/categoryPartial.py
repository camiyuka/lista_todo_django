from rest_framework import serializers
from todo.models.category import CategoryEntity

class CategoryDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model= CategoryEntity
        fields =['descriptioon']
