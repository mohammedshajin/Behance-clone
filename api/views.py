from django.db.models import manager
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from work.models import Work
from .serializers import WorkSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/works'},
        {'GET': '/api/works/id'},
        {'POST': '/api/works/id/vote'},
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]

    return Response(routes)

@api_view(['GET'])
def getWorks(request):
    work = Work.objects.all()
    serializer = WorkSerializer(work, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWork(request, pk):
    work = Work.objects.get(id=pk)
    serializer = WorkSerializer(work, many=False)
    return Response(serializer.data)