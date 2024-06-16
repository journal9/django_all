from django.db import models
from django.contrib.auth.models import User

class UserInfoz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)

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