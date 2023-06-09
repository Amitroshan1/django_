from django.shortcuts import render
from rest_framework import viewsets
from .models import company
from. serializers import companyserializers

# Create your views here.
class comapnyvieset(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializers = companyserializers