from typing import Match
from django.db import models


# Create your models here.
class Todolist(models.Model):

    thing =models.CharField(max_length=50)

    done=models.BooleanField(default=True)

    level=models.IntegerField(default=0)

    details=models.CharField(max_length=5000,default="")

    def __str__(self):

        return self.thing