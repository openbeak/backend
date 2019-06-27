from django.db.models import Avg
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
    queryset = AlgoReader.objects.all()
    serializer = AlgoReaderSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSolvedProblems(request, user_id):
    logging.error("getSolvedProblems GET method")

    res = requests.get('https://www.acmicpc.net/user/' + user_id)
    soup = BeautifulSoup(res.content, 'html.parser')

    problem_numbers = soup.select('.problem_number')

    statics = soup.select('#statics tr td')
    ranking = statics[0].getText()
    solving_count = statics[1].getText()

    user_num = []

    for num in problem_numbers:
        user_num.append(int(num.getText()))

    queryset = AlgoReader.objects.filter(pk__in=user_num)
    serializer = AlgoReaderSerializer(queryset, many=True)

    users_average_rate = AlgoReader.objects.filter(problemNum__in=problem_numbers).aggregate(Avg('price'))

    AlgoReader.objects.filter()

    user_info = {
        "ranking": ranking,
        "solving_count": solving_count,
        "soling_problems": serializer.data
    }

    logging.error(user_num)
    return Response(user_info)
# Create your views here.
