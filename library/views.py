from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from library.models import Manager

import jsonpickle

def login_view(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        name= request.POST.get('name')
        pwd  = request.POST.get('pwd')
        userList = Manager.objects.filter(user=name,pwd=pwd)
        message = '账号或密码有误'
        if userList:
            request.session["user"]=jsonpickle.dumps(userList[0])
            return redirect("/library/main/")
        return render(request,'login.html',{'message':message})

def main_view(request):
    return render(request,"main.html")

def library_modify_view(request):
    return render(request,"library_modify.html")

def readerType_view(request):
    return render(request,"readerType.html")

def reader_view(request):
    return render(request,"reader.html")

def bookType_view(request):
    return render(request,"bookType.html")

def book_view(request):
    return render(request,"book.html")

def bookBorrow_view(request):
    return render(request,"bookBorrow.html")

def bookRenew_view(request):
    return render(request,"bookRenew.html")

def bookBack_view(request):
    return render(request,"bookBack.html")

def bookQuery_view(request):
    return render(request,"bookQuery.html")

def borrowQuery_view(request):
    return render(request,"borrowQuery.html")

def bremind_view(request):
    return render(request,"bremind.html")

def pwd_Modify_view(request):
    return render(request,"pwd_Modify.html")