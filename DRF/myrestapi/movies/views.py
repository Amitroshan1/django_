from django.shortcuts import render
from rest_framework import viewsets
from .serializers import movieserializer
from .models import moviedata
# Create your views here.

class movieviewset(viewsets.ModelViewSet):
    queryset = moviedata.objects.all()
    serializer_class = movieserializer
    
    
class actionmovie(viewsets.ModelViewSet):
    queryset = moviedata.objects.filter(typ = 'action')
    serializer_class = movieserializer
    
class comedymovie(viewsets.ModelViewSet):
    queryset = moviedata.objects.filter(typ = 'comedy')
    serializer_class = movieserializer