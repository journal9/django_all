from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    Intro= models.CharField(max_length=100)

class Clientsz(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    capital = models.BigIntegerField()

    def __str__(self):
        return self.name

