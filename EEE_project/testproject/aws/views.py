from django.shortcuts import render, redirect
from aws.models import token
import json
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils.safestring import mark_safe
from django.http import JsonResponse
from .bin.nlp import NLP
from .bin.mapping import matchingSign 


def logout(request):
    auth.logout(request)

    return redirect('home')

# Create your views here.
def home(request):
    
    return render(request, 'home.html')


def result(request):
    if request.method =='POST':
        text = request.POST.get('text1')

        nlp = NLP()
        pre_text= nlp.relocateMorpheme(text)
        print(pre_text)

        result = matchingSign(pre_text)
        print(result)
        

        context={
            'q':result
        }
        return JsonResponse(context)

    return render(request, 'result.html')

ERROR_MSG = {
    'ID_EXIST': '이미 사용 중인 아이디 입니다.',
    'ID_NOT_EXIST': '존재하지 않는 아이디 입니다',
    'ID_PW_MISSING': '아이디와 비밀번호를 다시 확인해주세요.',
    'PW_CHECK': '비밀번호가 일치하지 않습니다.',
}

def signup(request):

    context = {
        'error': {
            'state': False,
            'msg': ''
        }
    }
    if request.method == 'POST':
        
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_pw_check = request.POST['user_pw_check']

        if (user_id and user_pw):

            user = User.objects.filter(username=user_id)

            if len(user) == 0:

                if (user_pw == user_pw_check):

                    created_user = User.objects.create_user(
                        username=user_id,
                        password=user_pw
                    )

                    auth.login(request, created_user)
                    return redirect('home')
                else:
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_EXIST']
        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']

    return render(request, 'signup.html', context)

def login(request):
    context = {
        'error': {
            'state': False,
            'msg': ''
        },
    }

    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        user = User.objects.filter(username=user_id)

        if (user_id and user_pw):
            if len(user) != 0:
                user = auth.authenticate(
                    username=user_id,
                    password=user_pw
                )

                if user != None:
                    auth.login(request, user)

                    return redirect('home')
                else:
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_NOT_EXIST']
        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']

    return render(request, 'login.html', context)
        