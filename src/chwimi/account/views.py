from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Profile


def signup(request):
    if request.method == 'POST':
        if request.POST['input_userpw'] == request.POST['input_userpw_check']:
            try:
                user = User.objects.create_user(
                    username = request.POST['input_userid'],
                    password = request.POST['input_userpw']
                )
                user.save()
                # print('user id: '+user.username)
                profile = Profile(user = user)
                profile.email = request.POST['input_email']
                # print('profile email: '+profile.email)
                ## Todo: 선택사항(성별, 전화번호) 저장
                profile.save()
                
                return redirect('home')
            except:
                print('*** 이미 존재하는 id ***')
                return redirect('signup')
                
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['input_userid']
        password = request.POST['input_userpw']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout(request):
    pass
