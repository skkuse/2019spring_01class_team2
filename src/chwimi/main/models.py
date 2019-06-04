from django.db import models
from django.contrib.auth.models import User

#Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.IntegerField(default=0, blank=True)
    name = models.CharField(max_length=30, default='', blank=True)
    company = models.CharField(max_length=30, default='', blank=True)
    price = models.IntegerField(default=0, blank=True)
    video = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.name

class ListProduct(models.Model):
    category = models.IntegerField(default=0, blank=True)
    name = models.CharField(max_length=30, default='', blank=True)
    company = models.CharField(max_length=30, default='', blank=True)
    price = models.IntegerField(default=0, blank=True)
    video = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.name
