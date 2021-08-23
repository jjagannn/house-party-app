from django.shortcuts import render
from api.models import Room
from rest_framework import generics
from api.serializers import RoomSerializer

# Create your views here.
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer