from django.shortcuts import render
from django.http import HttpResponse
from .models import Message,User2
from .forms import MsgForm,User2Form
msgs_list = []
def home(request):
    if request.method == "POST":
        msg=request.POST["user1"]
        msgs_list.append(str(msg))
    
    return render(request,'home2.html',{'msgs':msgs_list})
def client1(request):
    if request.method == "POST":
        msg = request.POST["user2"]
        msgs_list.append("_"+str(msg))
   
    return render(request,"client.html",{'msgss':msgs_list})

