from django.shortcuts import render
from .serializers import DoctorSerializer
from rest_framework import generics
from .models import Doctor
from .permissions import IsOwnerOrReadOnly
# from rest_framework.permissions import IsAuthenticated

# Create your views here.

class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # permission_classes = [IsAuthenticated]


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsOwnerOrReadOnly]
