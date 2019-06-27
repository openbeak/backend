from django.db import models

class TotalProblems(models.Model):
    problemNum      = models.IntegerField()
    problemName     = models.CharField(max_length = 200)
    category        = models.CharField(max_length = 200)
    answerRate      = models.FloatField()

# Create your models here.
