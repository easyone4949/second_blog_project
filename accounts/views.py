from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request): 
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username= request.POST['username'])
                return render(request, 'signup.html',{'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                # create_user()쓰면 계정 생성됨
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'Password must match'})
    else:
        return render(request, 'signup.html')

def login(request): 
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(request, username=username, password= password)
            # auth.authenticate은 저 정보가 우리한테 실제로 있는 정보가 맞는지 우리 장고서버에 저장되어있는지 확인해주는 함수
                if user is not None:
                    # 만약 user가 이미 존재한 회원이라면..
                    auth.login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'login.html', {'error': 'username or password is incorrect.'})
        else:
            return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.hmtl')
