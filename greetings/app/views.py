from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse


from django.views import View

class GoodMorningView(View):
    def get(self,request):
        data={"message":"GoodMorning"}


        return JsonResponse(data)

class GoodEveningView(View):
    def get(self,request):
        data={"message":"Good Evening"}

        return JsonResponse(data)

class HelloWorldView(View):
    def get(self,request):
        data={"message":"Hello world"}

        return JsonResponse(data)

class GoodNightView(View):
    def get(self,request):
        data={"message":"Good Night"}
        return JsonResponse(data)


class Userdetails(View):
    def get(self,request):
        data=[
            {'name':'arun','age':23,'place':'ekm'},
            {'name':'akhil','age':24,'place':'kollam'}


        ]
        return JsonResponse(data,safe=False)
