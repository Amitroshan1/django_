from rest_framework import serializers
from .models import children

class childserializer(serializers.ModelSerializer):
    class Meta:
        model = children
        fields = '__all__'