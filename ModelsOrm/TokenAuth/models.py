from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class UserInfo(models.Model):
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
    
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)