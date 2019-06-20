import json
import random
import time

from django.shortcuts import redirect, render
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import (AddItemProperty, AddPurchase,
                                              AddRating, AddUserProperty,
                                              Batch, DeleteItem,
                                              GetItemPropertyInfo,
                                              GetItemValues,
                                              GetUserPropertyInfo,
                                              GetUserValues, ListUsers,
                                              RecommendItemsToItem,
                                              RecommendItemsToUser,
                                              RecommendUsersToItem,
                                              ResetDatabase, SetItemValues,
                                              SetUserValues)
from recombee_api_client.exceptions import APIException

from .models import Hobby
from subscribe.models import Subscribe
from main.models import ListProduct


# 취미테스트 페이지 호출
def hobbytest(request):
    return render(request, 'start.html')

# 사용자의 최근 취미 객체 호출
def get_user_hobby(user):
    count = Hobby.objects.filter(user=user).count()
    hobby = Hobby.objects.filter(user=user)[count-1]
    return hobby

# 테스트 응답값 체크 (중앙 범위의 값일 경우 추가 질문 호출)
def is_middle(ans):
    return True if (ans >= 4 and ans <= 6) else False

# 1번
def test_1(request):
    if request.method == 'POST':
        hobby = Hobby(user=request.user)
        hobby.test_1 = request.POST['ans_1'] 
        hobby.save()
        return redirect('../test_2')
    return render(request, 'test_1.html')

# 2번
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

# 2-1번(추가질문)
def test_2_1(request):
    if request.method == 'POST':
        ans_2_1_1 = int(request.POST['ans_2_1_1'])
        ans_2_1_2 = int(request.POST['ans_2_1_2'])
        ans_2_1_3 = int(request.POST['ans_2_1_3'])
        ans_2_1_4 = int(request.POST['ans_2_1_4'])
        average =   int((ans_2_1_1 + ans_2_1_2 + ans_2_1_3 + ans_2_1_4) / 4) * 2

        hobby = get_user_hobby(request.user)
        hobby.test_2 = average
        hobby.save()
        return redirect('../test_3')
    return render(request, 'test_2_1.html')

# 3번
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

# 3-1번(추가질문)
def test_3_1(request):
    if request.method == 'POST':
        ans_3_1_1 = int(request.POST['ans_3_1_1'])
        ans_3_1_2 = int(request.POST['ans_3_1_2'])
        ans_3_1_3 = int(request.POST['ans_3_1_3'])
        average   = int((ans_3_1_1 + ans_3_1_2 + ans_3_1_3) / 3) * 2

        hobby = get_user_hobby(request.user)
        hobby.test_3 = average
        hobby.save()
        return redirect('../test_4')
    return render(request, 'test_3_1.html')

# 4번
def test_4(request):
    if request.method == 'POST':
        hobby = get_user_hobby(request.user)
        ans_4 = int(request.POST['ans_4'])

        if is_middle(ans_4):
            return redirect('../test_4_1')
        hobby.test_4 = ans_4
        hobby.save()
        return redirect('../test_5')
    return render(request, 'test_4.html')

# 4-1번(추가질문)
def test_4_1(request):
    if request.method == 'POST':
        ans_4_1_1 = int(request.POST['ans_4_1_1'])
        ans_4_1_2 = int(request.POST['ans_4_1_2'])
        average   = int((ans_4_1_1 + ans_4_1_2) / 2) * 2

        hobby = get_user_hobby(request.user)
        hobby.test_4 = average
        hobby.save()
        return redirect('../test_5')
    return render(request, 'test_4_1.html')

# 5번
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

# 5-1번(추가질문)
def test_5_1(request):
    if request.method == 'POST':
        ans_5_1_1 = int(request.POST['ans_5_1_1'])
        ans_5_1_2 = int(request.POST['ans_5_1_2'])
        ans_5_1_3 = int(request.POST['ans_5_1_3'])
        average   = int((ans_5_1_1 + ans_5_1_2 + ans_5_1_3) / 3) * 2

        hobby = get_user_hobby(request.user)
        hobby.test_5 = average
        hobby.save()
        return redirect('../result')
    return render(request, 'test_5_1.html')

# 분석 결과 페이지
def result(request):
    hobby = get_user_hobby(request.user)
    category, item = recommend(hobby)
    item = item[1]
    hobby.result_category = category
    hobby.result_product = item
    hobby.save()

    return render(request, 'result.html', {'hobby':hobby})

# Recombee API를 사용한 결과 반환
def recommend(hobby):
    client = RecombeeClient('se2-dev', '4qkJhisOw38DRWE1MmQ3xhJeY7k68qdjV2O5gjHaxsuBVCQX4VnkLboU5R0K7DQu')
    
    # Hobbytest에서 입력받은 결과를 변수로 설정
    user_O  = hobby.test_2 # Openness          (외향성 - 오락형)
    user_A  = hobby.test_3 # Agreeableness     (친화성 - 감성형)
    user_E  = hobby.test_4 # Extraversion      (개방성 - 창작형)
    user_C  = hobby.test_5 # Conscientiousness (성실성 - 제작형)
    account = hobby.user
    
    try:
        time.sleep(0.2)
        # 입력받은 변수와 계정정보를 서버에 전송
        client.send(SetUserValues(account,
            {
                "Openness": user_O,
                "Agreeableness": user_A,
                "Extraversion": user_E,
                "Conscientiousness": user_C,
                "Result": [],
                "recommenditems": [],
            },
            cascade_create = True))
        time.sleep(0.2)

        # filtering 후 결과를 서버의 result에 전송
        result = filtering(user_O, user_A, user_E, user_C)

        client.send(SetUserValues(account,
        {
            "Result": result,
        },
        cascade_create = True))
        # RecommendItemsToUser, 해당 유저의 Result 값을 참조하여 Item DB의 Categories와 일치하는 아이템을 추천
        recommendation = client.send(RecommendItemsToUser (account, 3,
            filter = "'categories' in context_user[\"Result\"]"
                            ))

        # 추천 결과를 Parse하여 아이템id 리스트만 변수로 별도 선언
        recommitems = recommendation['recomms']
        items = []

        # 아이템id를 통해 아이템DB에 있는 해당 아이템의 이름을 받는다
        for j in range(len(recommitems)):
            temp_num = recommitems[j]['id']
            temp = client.send(GetItemValues(str(temp_num)))
            items.append(temp['title'])
        
        # 유저 정보를 불러와 추천 아이템 리스트에 결과를 append 한다.
        user = client.send(GetUserValues(account))
        recommended = user['recommenditems']
        recommended.append(random.choice(items))
        client.send(SetUserValues(account,
            {
                "recommenditems": recommended,
            },
            cascade_create = True))

        # 결과 변수
        user_current = client.send(GetUserValues(account))
        user_item = user_current['recommenditems']
        user_type = user_current['Result']

        give = [account,user_item[0]]

        user_type = type_to_string(user_type)

    except ApiTimeoutException as e:
        # 서버 요청 시 문제가 발생했을 때 대안
        items_fun = ['클레이 만들기','슬라임 만들기','브릭픽셀아트']
        items_gamsung = ['애착인형','프랑스자수 액자','이끼 테라리움']
        items_create = ['캘리그라피 에코백','아트토이','탄생석모양 수제비누']
        items_make = ['아크릴 무드등','프레임형 네온사인','가죽공예 카드지갑']
        
        user_item = []
        result = filtering(user_O, user_A, user_E, user_C)
        if (result[0] == "Gamsung"):
            user_item.append(random.choice(items_gamsung))
            user_type = result
        elif(result[0] == "Fun"):
            user_item.append(random.choice(items_fun))
            user_type = result
        elif(result[0] == "Create"):
            user_item.append(random.choice(items_create))
            user_type = result
        elif(result[0] == "Make"):
            user_item.append(random.choice(items_make))
            user_type = result

        user_type = type_to_string(user_type)
        give = [account,user_item[0]]

    finally:
        return user_type, give

# 결과값(영어)를 한글로 변환
def type_to_string(user_type):
    for idx in range(len(user_type)):
        if user_type[idx] == 'Make':
            user_type[idx] = '제작형'
        elif user_type[idx] == 'Create':
            user_type[idx] = '창작형'
        elif user_type[idx] == 'Fun':    
            user_type[idx] = '오락형'
        elif user_type[idx] == 'Gamsung':
            user_type[idx] = '감성형'
    return user_type

# 취향 필터링 함수
def filtering(user_O, user_A, user_E, user_C):
    result = []
    if((user_A >= user_C) and (user_A >= user_O) and (user_A >= user_E)):
        result =  ["Gamsung"]
        if(user_A == user_C):
            result.append("Make")
        if(user_A == user_O):
            result.append("Fun")
        if(user_A == user_E):
            result.append("Create")
    elif((user_C >= user_A) and (user_C >= user_O) and (user_C >= user_E)):
        result =  ["Make"]
        if(user_C == user_A):
            result.append("Gamsung")
        if(user_C == user_O):
            result.append("Fun")
        if(user_C == user_E):
            result.append("Create")
    elif((user_O >= user_A) and (user_O >= user_C) and (user_O >= user_E)):
        result =  ["Fun"]
        if(user_O == user_A):
            result.append("Gamsung")
        if(user_O == user_C):
            result.append("Make")
        if(user_O == user_E):
            result.append("Create")
    else:
        result =  ["Create"]
        if(user_E == user_A):
            result.append("Gamsung")
        if(user_E == user_C):
            result.append("Make")
        if(user_E == user_O):
            result.append("Fun")
    
    return result
