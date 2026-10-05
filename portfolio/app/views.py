from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views import View

class AboutAPI(View):
    def get(self,request):
        data={'id':101,'name':'abhi','title':'zoro','DOB':'11/11/2003','email':'jithu7203@gmail.com','location':'kollam','github url':'https://github.com/jithu7203zoro','linkedin':'linkedin.123.jithu'}

        return JsonResponse(data)


class EducationAPI(View):
    def get(self,request):
        data={'id':102,'institution':'luminar','course':'full stack','university':'kerala','location':'ekm','startyear':'2026','endyear':'2027','grade':'A','description':'onumila'}
        return JsonResponse(data)

class ProjectAPI(View):
    def get(self,request):
        data=[

            {'id':'103','projectname':'PORTFOLIO','description':'WOWW','technologies':'victus','duration':'2hr','liveurl':'https://github.com/jithu7203zoro/portfolio.git'}

        ]

        return JsonResponse(data,safe=False)

