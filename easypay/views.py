from django.http import HttpResponse
from django.shortcuts import render
from .models import payments
import requests
mc_url="https://api.thingspeak.com/update?api_key=8R3CO2HRXMICK3VK&field1="
def index(request):
    return render(request,'index.html')

def payment(request):
    if request.method=='POST':
        name=request.POST.get('username')
        amount=request.POST.get('ammount')
        requests.get(mc_url+name+"&field2="+amount)
        insertdb=payments(username=name,ammount=amount)
        insertdb.save()
        return render(request,'pay_sucess.html')
    else:
        return HttpResponse("something wend wrong ")

def getdata(requests):
    name=payments.objects.last().username
    ammount=payments.objects.last().ammount
    return HttpResponse(f"{name} {ammount}")
    