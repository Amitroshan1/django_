from rest_framework import serializers
from .models import company

class companyserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= company
        fields = "__all__"