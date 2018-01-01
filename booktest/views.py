from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import AreaInfo

def index(request):
    return render(request,'booktest/index.html')

def pro(request):
    prolist =list(AreaInfo.objects.filter(parea__isnull=True).values())
    return JsonResponse({'data':prolist})

def city(request,id):
    citylist= list(AreaInfo.objects.filter(parea_id=id).values())
    return JsonResponse({'data':citylist})

def dis(requset,id):
    dislist = list(AreaInfo.objects.filter(parea_id=id).values())
    return JsonResponse({'data':dislist})