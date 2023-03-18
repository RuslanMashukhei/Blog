from django.shortcuts import render
from rest_framework import generics

from .models import Admin
from .serializers import AdminSerializer


class AdminRegisterView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
