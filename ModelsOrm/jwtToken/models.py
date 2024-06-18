from django.db import models

# Create your models here.

class Cookies(models.Model):
    cookie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    flavour = models.CharField(max_length=30)