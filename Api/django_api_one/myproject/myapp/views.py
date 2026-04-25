# from django.shortcuts import render

# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("welcome to my page !")

from rest_framework.decorators import api_view
from .serializers import DataSerializer
from .models import Upload
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])

def data_list(requiest):
    if requiest.method=="GET":
        list = Upload.objects.all()
        serializer = DataSerializer(list, many = True)
        return Response(serializer.data)
    
    if requiest.method == 'POST':
        serializer = DataSerializer(data = requiest.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT', 'PATCH', 'DELETE'])
def updatelist(request, pk):
    try:
        obj = Upload. objects.get(pk = pk)
    except Upload.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DataSerializer(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DataSerializer(obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)