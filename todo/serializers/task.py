from rest_framework import serializers
from todo.models.category import CategoryEntity
from todo.models.task import TaskEntity

class TaskSerializer(serializers.ModelSerializer):
   category= serializers.SlugRelatedField(
       read_only=True,
       slug_field='name'
   )
   class Meta:
        model = TaskEntity
        fields = ['id', 'name', 'category', 'description', 'percent', 'state']