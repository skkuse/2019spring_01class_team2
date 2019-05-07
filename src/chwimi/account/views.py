from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile

def signup(request):
    if request.method == 'POST':
        if request.POST['input_userpw'] == request.POST['input_userpw_check']:
            try:
                user = User.objects.create_user(
                    username = request.POST['input_userid'],
                    password = request.POST['input_userpw']
                )
                profile = Profile(user = user)
                return redirect('home')
            except:
                print('*** 이미 존재하는 id ***')
                return redirect('signup')
                
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['input_userid'])
    return render(request, 'login.html')
