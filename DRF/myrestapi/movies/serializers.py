from rest_framework import serializers
from .models import moviedata

class movieserializer(serializers.ModelSerializer):
    img = serializers.ImageField(use_url=True)
    class Meta:
        model = moviedata
        fields = ['id','name','duration','rating','typ','img']