from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.views import view



class First(view):
    def get(self,request):
        return HttpResponse("First Page")



class Second(view):
    def get(self,request):
        return HttpResponse("Second Page")
