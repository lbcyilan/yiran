from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 查询字符串传参
def index(request):

    print(request.GET.get('a'))
    print(request.GET.get('b'))
    print(request.GET.getlist('b'))

    return HttpResponse('获取查询字符串参数成功')
