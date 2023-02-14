from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    #print(':::::::', request)
    #print('::::::type(request):', type(request))
    #print('::::::request.environ:', request.environ)
    #print('::::::request.path_info:', request.path_info)
    #print('::::::request.path:', request.path)
    #print('::::::request.method:', request.method)
    #print('::::::request.headers():', request.headers())
    #return HttpResponse('Hello there')

    #content = {'password': 'JKhkjhKJlkjSl;k'}
    return render(request, 'passw/home.html')

def password(request):

    characters = list('abcdefghijklnmopqrstvuwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTVUWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+,.'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))


    thepassword = ''
    for x in range(length):
        thepassword+=random.choice(characters)

    return render(request, 'passw/password.html', {'password': thepassword})

def about(request):
    return render(request, 'passw/about.html')
