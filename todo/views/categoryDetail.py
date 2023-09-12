from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todo import serializers

from todo.models.category import CategoryEntity
from todo.serializers.category import CategorySerializer
from todo.serializers.categoryPartial import CategoryDescriptionSerializer

class CategoryDetailView(APIView):
    """
    Retrieve, update or delete a category instance.
    """
    def get_object(self, pk):
        try:
         return CategoryEntity.objects.get(pk=pk)
        except CategoryEntity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category= self.get_object(pk)
        serializer= CategorySerializer(category)
        return Response(serializer.data, status.status.HTTP_200_OK)

    def put(self, request, pk, format=None):
         category= self.get_object(pk)
         serializer= CategorySerializer(category, data=request.data)
         if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        category= self.get_object(pk)
        serializer= CategoryDescriptionSerializer(category, data=request.data, partial= True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
         category= self.get_object(pk)
         category.delete()
         return Response(status= status.HTTP_204_NO_CONTENT)
    
    