from django.shortcuts import render
from subscribe.models import Subscribe
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def mypage(request):
    subscribes = Subscribe.objects.filter(account=request.user)
    return render(request, 'mypage.html', {'subscribes':subscribes})