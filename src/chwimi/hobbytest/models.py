from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hobby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    test_1 = models.CharField(max_length=20, blank=True, default = "")
    test_2 = models.IntegerField(blank=True, default=-1)
    test_3 = models.IntegerField(blank=True, default=-1)
    test_4 = models.IntegerField(blank=True, default=-1)
    test_5 = models.IntegerField(blank=True, default=-1)
    result_category = models.CharField(max_length=10, blank=True, default='')
    result_product = models.CharField(max_length=20, blank=True, default='')

    def __str__(self):
        return self.test_1