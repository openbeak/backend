from rest_framework import serializers

from .models import *


class TotalProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total_problems
        fields = '__all__'
