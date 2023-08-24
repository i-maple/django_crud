from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import Task

# Create your views here.
@api_view(['GET'])
def home(request):
    apiUrls = {
        'Get All Tasks': '/all-tasks',
        'Get Task Detail': '/detail-task/:id',
        'Add a Task': '/add-task',
        'Update a task': '/update-task/:id',
        'Delete a task':'/delete-task/:id'
    }
    return Response(apiUrls)

@api_view(['GET'])
def allTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detailTask(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addTask(request):
    serializer = TaskSerializer(data = request.data, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateTask(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return Response("Successfully Deleted")