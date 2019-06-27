from django.db import models

class Total_problems(models.Model):
    problemNum      = models.IntegerField(primary_key = True)
    problemName     = models.CharField(max_length = 200)
    category        = models.CharField(max_length = 200)
    answerRate      = models.CharField(max_length = 10)

# Create your models here.

