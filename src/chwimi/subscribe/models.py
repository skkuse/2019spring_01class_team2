from django.db import models
from django.contrib.auth.models import User
from main.models import ListProduct

# Create your models here.
class Subscribe(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(ListProduct, on_delete=models.CASCADE)
    relationship = models.IntegerField(default=3)
    timeperiod = models.IntegerField(default=3)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.item.name