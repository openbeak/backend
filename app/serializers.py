from rest_framework import serializers
from .models import *

class AlgoReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgoReader
        fields = '__all__'
