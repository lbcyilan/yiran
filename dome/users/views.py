from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 定义视图函数
from django.urls import reverse


def index(request):

    print('ksks')


    return HttpResponse('lala')
# reverse 反解析
def index1(request):
    """index1函数"""

    # 获取本函数的路径:
    url = reverse('user:index1')
    print(url)      # /users/index

    # 在index1函数中获取say函数的路径
    url1 = reverse('user:say')
    print(url1)         # /users/say


    return HttpResponse('好的')

def say(request):
    """say函数"""

    return HttpResponse('say')
