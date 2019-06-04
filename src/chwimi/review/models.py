from django.db import models
from datetime import datetime
from useraccount.models import Profile
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now())
    files = models.ImageField(upload_to='images/', blank=True)   
    rate_product = models.IntegerField(default=3, blank=True) 
    rate_delivery = models.IntegerField(default=3, blank=True) 
    rate_price = models.IntegerField(default=3, blank=True) 

    def __str__(self):
        return self.title

class Comment_review(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, related_name='comments')
    content = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now())
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content[:20]