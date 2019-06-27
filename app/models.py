from django.db import models

class AlgoReader(models.Model):
    problemNum      = models.IntegerField(primary_key = True)
    problemName     = models.CharField(max_length = 200)
    category        = models.CharField(max_length = 200)
    answerRate      = models.IntegerField()

# Create your models here.