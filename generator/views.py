from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    character = list('asdfghjklzxcvbnmqwertyuiop')
    length = int(request.GET.get('length', 12))
    thepassword = ''

    if request.GET.get('uppercase'):
        character.extend(list('ASDFGHJKLZXCVBNMQWERTYUIOP'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*(){}[]?'))
    if request.GET.get('numbers'):
        character.extend(list('0123456789'))

    for x in range(length):
        thepassword += random.choice(character)

    return render(request, 'generator/password.html', {'password': thepassword})
