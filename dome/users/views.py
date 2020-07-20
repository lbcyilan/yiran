from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    print('我来了')

    return HttpResponse('lala')
