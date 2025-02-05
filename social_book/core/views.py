from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth


def index(request):
    return render(request,'index.html')
    

def signup(request):
    
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"This email is already taken")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"This username is already taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
        else:
            messages.info(request,"password is not match ")
            return redirect('signup')
    
    return render(request,'signup.html')