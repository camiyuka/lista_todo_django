from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo.models.category import CategoryEntity
from todo.models.task import TaskEntity
from todo.serializers.task import TaskSerializer

class TaskView(APIView):
    """
    List all tasks, or create a new task.
    """    
    def get_category(self, pk):
        try:
            return CategoryEntity.objects.get(pk=pk)
        except CategoryEntity.DoesNotExist:
            raise Http404
        
    def get(self, request, format=None):
        tasks = TaskEntity.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        category = self.get_category(request.data.get("category"))
        serializer = TaskSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save(category=category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
