from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo.models.task import TaskEntity
from todo.serializers.task import TaskSerializer


class CategoryTaskView(APIView):
    """
    List all tasks for a given category.
    """
    def get(self, request, pk, format=None):
        tasks = TaskEntity.objects.get(category_id=pk)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    
