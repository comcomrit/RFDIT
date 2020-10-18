from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def HomePage(request):
    #return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'school/home.html')

def AboutPage(request):
    #return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'school/about.html')

def ContactUs(request):
    #return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'school/contactus.html')

def ShowScore(request):
	score = ExamScore.objects.all() #ดึงค่ามาจาก database ทั้งหมด

	context = {'score':score}

	return render(request, 'school/showscore.html', context)

def Register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        newuser = User()
        newuser.username = email
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.email = email
        newuser.set_password(password)
        newuser.save()
        return redirect('home-page')

    return render(request, 'school/register.html')