from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render
from .models import Supplies_fict

# Create your views here.

def Home(request):
    suply = Supplies_fict.objects.all()
    context = {'suply':suply}

    return render(request, 'comlog/home.html', context)
    #return HttpResponse('<h1>Hello World</h1>')
