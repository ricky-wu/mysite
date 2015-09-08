#-*- coding:utf-8 -*-
'''
Created on 2015年9月7日

@author: wupeng
'''
from django.http import  HttpResponse

def hello(request):
    return HttpResponse("Hello world")
pass
