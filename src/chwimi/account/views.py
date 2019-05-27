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
                profile = Profile(user = user)
                profile.email = request.POST['input_email']

                ## Todo: 선택사항(성별, 전화번호) 저장
                profile.save()
                messages.add_message(request, messages.SUCCESS, '환영합니다!')
                return redirect('home')
            except:
                messages.add_message(request, messages.ERROR, '이미 존재하는 id입니다.')
                return redirect('signup')
        messages.add_message(request, messages.ERROR, '비밀번호가 일치하지 않습니다.')   
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['input_userid']
        password = request.POST['input_userpw']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, '환영합니다!')
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, '로그인에 실패하였습니다. 아이디 또는 비밀번호를 확인해주세요.')
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, '성공적으로 로그아웃 되었습니다.')
        return redirect('home')
        
    return render(request, 'login.html')

