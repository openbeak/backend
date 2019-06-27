from rest_framework import serializers
from .models import *

class AlgoreaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Algoreader
        fields = '__all__'
