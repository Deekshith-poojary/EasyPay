from django.http import HttpResponse
from django.shortcuts import render
from .models import payments
import requests
import time
mc_url="https://api.thingspeak.com/update?api_key=8R3CO2HRXMICK3VK&field1="
name=""
amount=0

def index(request):
    return render(request,'index.html')

def details(request):
    if request.method=='POST':
        name=request.POST.get('username')
        amount=request.POST.get('amount')
        insertdb=payments(username=name,ammount=amount)
        insertdb.save()
        params={'name':name , 'amount':amount}
        ''' 
        for i in r_list:
            if name==i:
                return HttpResponse("SUCH WORDS ARE NOT ALLOWED ")
        '''
        return render(request,'pin.html',params)

def payment(request):
    if request.method=='POST':
        name=payments.objects.last().username
        amount=payments.objects.last().ammount
        requests.get(mc_url+name+"&field2="+str(amount))
        time.sleep(3)
        return render(request,'pay_sucess.html')
    else:
        return HttpResponse("something went wrong ")


def getdata(request):
    name=payments.objects.last().username
    amount=payments.objects.last().ammount
    param={"name":name , "amount":amount}
    return render(request,'data.html',param)
