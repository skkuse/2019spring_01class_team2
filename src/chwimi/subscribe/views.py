from django.shortcuts import render
from .models import Subscribe
from django.contrib.auth.models import User

# Create your views here.
def subscribe(request):
    return render(request, 'subscribe.html')