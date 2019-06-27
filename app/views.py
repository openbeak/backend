from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

import requests
from bs4 import BeautifulSoup

import logging

@api_view(['GET'])
def TotalProblems_list(request):
    logging.error("totalProblems GET method")
    queryset = TotalProblems.objects.all()
    serializer = TotalProblemsSerializer(queryset, many = True)
    return Response(serializer.data)

@api_veiw(['GET'])
def getSolvedProblems(request):
    user_id = "mor2222"

    res = requests.get('https://www.acmicpc.net/user/'+user_id)
    soup = BeautifulSoup(res.content, 'html.parser')

    problem_numbers = soup.select('.problem_number')

    user_num = []

    for num in problem_numbers:
        user_num.append(numgetTexti())

    logging.error(res)
    logging.error(soup)
    logging.error(problem_numbers)
    logging.error(user_num)

# Create your views here.
