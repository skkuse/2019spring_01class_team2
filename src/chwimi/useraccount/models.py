from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'None'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username 

