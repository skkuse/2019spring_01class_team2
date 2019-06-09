from django.shortcuts import render
from subscribe.models import Subscribe
from hobbytest.models import Hobby
from django.contrib.auth.models import User

def home(request):
    subscribes = Subscribe.objects.filter(account=request.user)
    return render(request, 'home.html', {'subscribes':subscribes})

def about(request):
    return render(request, 'about.html')

def mypage(request):
    subscribes = Subscribe.objects.filter(account=request.user)
    hobbies = Hobby.objects.filter(user=request.user)
    return render(request, 'mypage.html', {'subscribes':subscribes, 'hobbies':hobbies})