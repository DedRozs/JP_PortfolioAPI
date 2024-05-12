from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import *

# Create your views here.

class Index(APIView):
    # permission_classes = [IsAuthenticated]
    """
    List all partners, or create a new partner.
    """
    def get(self, request, format=None):
       
        return Response({"Message":"Some Data"}, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     serializer = PartnerSerializer(data=request.data, context={"request":request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer