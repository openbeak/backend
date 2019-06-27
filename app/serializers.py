from rest_framework import serializers
from .models import *

class TotalProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalProblems
        fields = '__all__'
