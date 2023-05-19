from django.shortcuts import render,HttpResponse,redirect
#from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def HomePage(request):
    return render(request,'index.html')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get("username")
        email=request.POST.get("email")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password didnt match")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()

            return redirect('login')

    return render(request,'signuppage.html')
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        #print(email,password)
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorect!!!")
    return  render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')