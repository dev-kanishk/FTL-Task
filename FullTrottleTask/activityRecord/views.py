from django.shortcuts import render
from .serializers import UserSerializer, testSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User


class UsersList(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = testSerializer(users)
        return Response(serializer.data)


