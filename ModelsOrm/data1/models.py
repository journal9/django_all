from django.db import models
from django.utils.timezone import now

# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    experience = models.IntegerField()

    def get_author(self):
        return {
            "id":self.id,
            "name":self.name,
            "experience":self.experience
        }


class ReachChoices(models.TextChoices):
    IN = "in"
    UN = "un"
    AUS = "aus"


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.IntegerField()
    start_date = models.DateTimeField(default=now)
    published_date = models.DateTimeField(null=True)
    time_taken = models.DateTimeField(null=True)
    time_diff = models.IntegerField(null=True)
    reach = models.TextField(choices=ReachChoices.choices,default=ReachChoices.UN)
    rating = models.FloatField(null=True)
    updated_at = models.DateTimeField(default=now)
    
    class Meta:
        unique_together = ('author','title','published_date')

    def get_book(self):
        return {
            "id":self.id,
            "title":self.title,
            "author_id":self.author.id,
            "author_name":self.author.name,
            "pages":self.pages,
            "price":self.price,
            "start_date":self.start_date,
            "published_date":self.published_date,
            "rating":self.rating,
            "reach":self.reach,
            "updated_at":self.updated_at
        }

