from django.shortcuts import render, redirect
from .models import Hobby

# Create your views here.
def hobbytest(request):
    return render(request, 'start.html')

def get_user_hobby(user):
    count = Hobby.objects.filter(user=user).count()
    hobby = Hobby.objects.filter(user=user)[count-1]
    return hobby

def is_middle(ans):
    return True if (ans >= 4 and ans <= 6) else False

def test_1(request):
    if request.method == 'POST':
        hobby = Hobby(user=request.user)
        hobby.test_1 = request.POST['ans_1'] 
        hobby.save()
        return redirect('../test_2')
    return render(request, 'test_1.html')

def test_2(request):
    if request.method == 'POST':
        hobby = get_user_hobby(request.user)
        ans_2 = int(request.POST['ans_2'])

        # 4~6의 응답값이 나오면 추가 문항 제공
        if is_middle(ans_2):
            return redirect('../test_2_1')
        hobby.test_2 = ans_2 
        hobby.save()
        return redirect('../test_3')
    return render(request, 'test_2.html')

def test_2_1(request):
    if request.method == 'POST':
        ans_2_1_1 = int(request.POST['ans_2_1_1'])
        ans_2_1_2 = int(request.POST['ans_2_1_2'])
        ans_2_1_3 = int(request.POST['ans_2_1_3'])
        ans_2_1_4 = int(request.POST['ans_2_1_4'])
        average = int((ans_2_1_1 + ans_2_1_2 + ans_2_1_3 + ans_2_1_4) / 4) * 2

        hobby = get_user_hobby(request.user)
        hobby.test_2 = average
        hobby.save()
        return redirect('../test_3')
    return render(request, 'test_2_1.html')

def test_3(request):
    if request.method == 'POST':
        hobby = get_user_hobby(request.user)
        ans_3 = int(request.POST['ans_3'])

        if is_middle(ans_3):
            return redirect('../test_3_1')
        hobby.test_3 = ans_3
        hobby.save()
        return redirect('../test_4')
    return render(request, 'test_3.html')

def test_3_1(request):
    if request.method == 'POST':
        ans_3_1_1 = int(request.POST['ans_3_1_1'])
        ans_3_1_2 = int(request.POST['ans_3_1_2'])
        ans_3_1_3 = int(request.POST['ans_3_1_3'])
        average = int((ans_3_1_1 + ans_3_1_2 + ans_3_1_3) / 3) * 2

        hobby = get_user_hobby(request.user)
        hobby.test_3 = average
        hobby.save()
        return redirect('../test_4')
    return render(request, 'test_3_1.html')

def test_4(request):
    if request.method == 'POST':
        hobby = get_user_hobby(request.user)
        ans_4 = int(request.POST['ans_4'])

        if is_middle(ans_4):
            return redirect('../test_4_1')
        hobby.test_4 = ans_4
        hobby.save()
        return redirect('../test5')
    return render(request, 'test_4.html')

def test_4_1(request):
    if request.method == 'POST':
        ans_4_1_1 = int(request.POST['ans_4_1_1'])
        ans_4_1_2 = int(request.POST['ans_4_1_2'])
        average = int((ans_4_1_1 + ans_4_1_2) / 2) * 2

        hobby = get_user_hobby(request.user)
        hobby.test_4 = average
        hobby.save()
        return redirect('../test_5')
    return render(request, 'test_4_1.html')

def test_5(request):
    if request.method == 'POST':
        hobby = get_user_hobby(request.user)
        ans_5 = int(request.POST['ans_5'])

        if is_middle(ans_5):
            return redirect('../test_5_1')
        hobby.test_5 = ans_5
        hobby.save()
        return redirect('../result')
    return render(request, 'test_5.html')

def test_5_1(request):
    if request.method == 'POST':
        ans_5_1_1 = int(request.POST['ans_5_1_1'])
        ans_5_1_2 = int(request.POST['ans_5_1_2'])
        ans_5_1_3 = int(request.POST['ans_5_1_3'])
        average = int((ans_5_1_1 + ans_5_1_2 + ans_5_1_3) / 3) * 2

        hobby = get_user_hobby(request.user)
        hobby.test_5 = average
        hobby.save()
        return redirect('../result')
    return render(request, 'test_5_1.html')

def result(request):
    # Recombee 함수 삽입
    # 객체 변수 값이 -1인 경우 객체 삭제
    hobby = get_user_hobby(request.user)
    return render(request, 'result.html', {'hobby':hobby})