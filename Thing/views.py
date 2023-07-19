from django.shortcuts import render

from rest_framework import generics
from .models import Thing,Blog
from .serializers import Thingserializer,Blogserializer
from rest_framework.permissions import IsAuthenticated ,AllowAny
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# ListAPIView
class Thing_list(generics.ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = Thingserializer
    permission_classes = [IsAuthenticated]

# RetrieveAPIView
class Thing_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = Thingserializer
    permission_classes = [IsOwnerOrReadOnly]

class Blog_list(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blogserializer
    permission_classes = [AllowAny]

class Blog_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blogserializer
    permission_classes = [AllowAny]