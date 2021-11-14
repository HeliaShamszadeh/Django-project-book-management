import datetime
from django.db import models
from django.utils import timezone



class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Owner = models.CharField(max_length=200)
    city = models.CharField(max_length=200, null = True, blank = True, default=False)
    email = models.CharField(max_length=200)
    Description = models.TextField(null = True, blank = True)
    borrowed= models.BooleanField(default=False)
    pubdate = models.DateTimeField('date published', null=True)
    def __str__(self):
        return self.name
    def was_published_recently(self):
        return self.pubdate >= timezone.now() - datetime.timedelta(days=1)


# Create your models here.
