from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import *
from .serializers import *
from .models import *


@api_view(['GET'])
def get_users(request):
    users = SchoolUser.objects.all()
    serializer = SchoolUserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_user(request):
    data = request.data
    serializer = SchoolUserSerializer(data=data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)