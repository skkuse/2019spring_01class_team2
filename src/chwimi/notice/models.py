from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Notice(models.Model):
    admin = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

