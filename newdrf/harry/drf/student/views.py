from django.shortcuts import render
from .serializer import childserializer
from.models import children
from rest_framework.renderers import JSONRenderer
from django.http  import HttpResponse, JsonResponse
# Create your views here.


def student_info(request):
    stu = children.objects.all()
    serialize = childserializer(stu,many=True)
    return JsonResponse(serialize.data, safe=False)