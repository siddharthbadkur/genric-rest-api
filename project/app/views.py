from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import generics
from django.shortcuts import render


class StudentList(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
