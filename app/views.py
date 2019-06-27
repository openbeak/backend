from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
import logging

@api_view(['GET'])
def TotalProblems_list(request):
    logging.error("totalProblems GET method")
    queryset = TotalProblems.objects.all()
    serializer = TotalProblemsSerializer(queryset, many = True)
    return Response(serializer.data)
# Create your views here.
