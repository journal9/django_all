from django.db import models
from django.utils.timezone import now
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
import datetime

# Create your models here.
class GenderChoices(models.TextChoices):
    FEMALE = 'female'
    MALE = 'male'
    OTHER = 'other'

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    gender = models.TextField(choices=GenderChoices.choices,default=GenderChoices.MALE)
    joined_date = models.DateField(default=datetime.date.today)

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    comment_text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=now)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)    #field content_type is connected to the ContentType we imported at first via foreign key
    object_id = models.CharField(max_length=50)                                #object_id is provided with a character field
    content_object = GenericForeignKey('content_type', 'object_id')   
    
class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    captian = models.TextField()
    author = models.ForeignKey(Users,verbose_name='user',on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    com = GenericRelation(Comments)         #field content_object is connected to the fields content_type and object_id