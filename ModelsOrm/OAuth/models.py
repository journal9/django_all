from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    client_id = models.CharField(max_length=10)
    client_secret = models.CharField(max_length=40)
    created_at = models.DateTimeField(default=now)

class Interns(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email_id = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    college = models.CharField(max_length=70)
    graduation_year = models.IntegerField()
    passed = models.BooleanField(null=True)

    def __str__(self):
        return self.name