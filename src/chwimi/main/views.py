from django.shortcuts import render
from subscribe.models import Subscribe
from hobbytest.models import Hobby
from django.contrib.auth.models import User

# 홈 페이지
def home(request):
    # 구독 정보 존재하는 경우 교육 비디오 출력
    if request.user.is_authenticated:
        subscribes = Subscribe.objects.filter(account=request.user)
        return render(request, 'home.html', {'subscribes':subscribes})
    return render(request, 'home.html')

# 서비스 설명 페이지
def about(request):
    return render(request, 'about.html')

# 마이페이지
def mypage(request):
    subscribes = Subscribe.objects.filter(account=request.user)
    hobbies = Hobby.objects.filter(user=request.user)
    return render(request, 'mypage.html', {'subscribes':subscribes, 'hobbies':hobbies})