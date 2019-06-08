import json
import random

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
        return redirect('../test_5')
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
    # 객체 변수 값이 -1인 경우 객체 삭제
    hobby = get_user_hobby(request.user)
    category, item = recommend(hobby)
    item = item[1]

    return render(request, 'result.html', {'hobby':hobby, 'item':item, 'category':category})

def recommend(hobby):
    client = RecombeeClient('skku-testinguser', 'L1zVNlMZfzgizO0C0bqB3DA87xEpSmH01DdXos7ZyZoJHzvsyuwDAtOu5bLZqyIs')
    
    user_O = hobby.test_2 # Openness          (외향성 - 오락형)
    user_A = hobby.test_3 # Agreeableness     (친화성 - 감성형)
    user_E = hobby.test_4 # Extraversion      (개방성 - 창작형)
    user_C = hobby.test_5 # Conscientiousness (성실성 - 제작형)
    account = hobby.user
    
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

    # filtering
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

    client.send(SetUserValues(account,
    {
        "Result": result,
    },
    cascade_create = True))
    recommendation = client.send(RecommendItemsToUser (account, 3,
        filter = "'categories' in context_user[\"Result\"]"
                        ))

    # print(recommendation)
    recommitems = recommendation['recomms']
    items = []
    for j in range(len(recommitems)):
        temp_num = recommitems[j]['id']
        temp = client.send(GetItemValues(str(temp_num)))
        items.append(temp['title'])
    user = client.send(GetUserValues(account))
    recommended = user['recommenditems']
    recommended.append(random.choice(items))
    client.send(SetUserValues(account,
        {
            "recommenditems": recommended,
        },
        cascade_create = True))

    user_current = client.send(GetUserValues(account))
    user_item = user_current['recommenditems']
    user_type = user_current['Result']
    # print(user_item)
    # print(user_type)

    give = [account,user_item[0]]

    for idx in range(len(user_type)):
        if user_type[idx] == 'Make':
            user_type[idx] = '제작형'
        elif user_type[idx] == 'Create':
            user_type[idx] = '창작형'
        elif user_type[idx] == 'Fun':    
            user_type[idx] = '오락형'
        elif user_type[idx] == 'Gamsung':
            user_type[idx] = '감성형'
        
    return user_type, give
