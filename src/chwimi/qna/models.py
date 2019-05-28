from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from account.models import Profile


# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now())
    files = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

class Comment_question(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='comments')
    content = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now())
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content[:20]
