from random import sample

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

    queryset = Algoreader.objects.all()
    serializer = AlgoreaderSerializer(queryset, many=True)
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

    queryset = Algoreader.objects.filter(pk__in=user_num)
    serializer = AlgoreaderSerializer(queryset, many=True)

    users_average_rate = Algoreader.objects.filter(problemNum__in=user_num).aggregate(Avg('answerRate'))[
        "answerRate__avg"]

    print(type(users_average_rate))
    print(users_average_rate)

    lower_bound = int(users_average_rate - 500)
    upper_bound = int(users_average_rate + 500)

    # bound_list = Algoreader.objects.filter(answerRate__range=(lower_bound, upper_bound))
    bound_list = Algoreader.objects.filter(answerRate__lt=upper_bound, answerRate__gt=lower_bound).exclude(problemNum__in=user_num)
    bound_list_serializers = AlgoreaderSerializer(bound_list, many=True)

    top5_list = sample(bound_list_serializers.data, 5)
    print(top5_list)

    user_info = {
        "ranking": ranking,
        "solving_count": solving_count,
        "soling_problems": serializer.data,
        "top5_list": top5_list
    }

    logging.info(user_num)
    return Response(user_info)
# Create your views here.
