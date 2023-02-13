from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import *
# Create your views here.
data={}
def addAdvertisingcampaign(request):
    return render(request,template_name="addadvertisingcampaign.html",context=data)






@csrf_exempt

@csrf_exempt
def createAdvertisingcampaign(request):
    name=request.POST["name"]
    createdate=request.POST["createdate"]
    totalbudget = request.POST["totalbudget"]
    dailybudget = request.POST["dailybudget"]
    advertisingcampaignimg  = request.FILES.get("image")
    print(advertisingcampaignimg)
    a = Advertisingcampaign.objects.create(name=name,createdate=createdate,totalbudget=totalbudget,dailybudget=dailybudget,image=advertisingcampaignimg)
    return redirect("listAdvertisingcampaign")
    




def listAdvertisingcampaign(request):
    data={}
    data["advertisingcampaign"]=Advertisingcampaign.objects.all()
    return render(request,template_name="advertisingcampaign.html",context=data)



def editAdvertisingcampaign(request,id):
    data={}
    advertisingcampaign=Advertisingcampaign.objects.get(id=id)
    data["advertisingcampaign"]=advertisingcampaign
    return render(request,template_name="editadvertisingcampaign.html",context=data)







@csrf_exempt
def updateAdvertisingcampaign(request):
    id = request.POST['id']
    name=request.POST["name"]
    createdate=request.POST["createdate"]
    totalbudget = request.POST["totalbudget"]
    dailybudget = request.POST["dailybudget"]
    a = Advertisingcampaign.objects.get(id=id)
    a.name=name
    a.createdate=createdate
    a.totalbudget=totalbudget
    a.dailybudget=dailybudget
    a.save()
    return redirect("listAdvertisingcampaign")




#delete record
def deleteAdvertisingcampaign(request,id):
    article=Advertisingcampaign.objects.get(id=id)
    article.delete()
    return redirect("listAdvertisingcampaign")


   
