from functools import partial
from multiprocessing import context
from re import T
from unicodedata import category
from urllib import response
from django.shortcuts import render,redirect
from .models import *
from .serializers import BookEntrySerializer
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
import json
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import permission_classes,authentication_classes,api_view
from rest_framework.authentication import TokenAuthentication

from django.http import HttpResponse
from django.http import JsonResponse
import requests
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from datetime import datetime,date
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.


def home(request):
    bk = BookEntry.objects.filter()
    print(bk)
    books = []
    for i in bk:
        books.append([i.name,i.author])
        
    context = {
        "books":books,
    }
    return render(request, 'app1/home.html',context)

@login_required
def index(request):
    return render(request, 'app1/index.html')

@login_required
def add_book(request):
    key  =  Token.objects.get(user=request.user)
    context = {"key":key,'user':request.user}
    return render(request, 'app1/book_entry.html',context)

login_required
@api_view(http_method_names=['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def enter_book(request):
    print("enter book---------")
       

    serializer = BookEntrySerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save(library_admin=request.user)
    else:
        print(serializer.errors)

        return render(request, 'app1/index.html')  
    
    

login_required
@api_view(http_method_names=['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def get_all_books(request):
    print("-------------get all books, ", request.user)

    bk = BookEntry.objects.filter(library_admin=request.user)

    serializer = BookEntrySerializer(bk,many=True)
   
    return Response(serializer.data)

login_required  
def list(request):
    key  =  Token.objects.get(user=request.user)
    context = {"key":key,'user':request.user}
    
    return render(request,'app1/show_book.html',context)


login_required
@api_view(http_method_names=['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def save_update_book(request,pk):
    print("updates",pk)
    
    id = int(pk)
    book = BookEntry.objects.get(id = id,library_admin=request.user)
    key  =  Token.objects.get(user=request.user)
    
    book_detail = {
        'id' : book.id,
        'name':book.name,
        'author':book.author,
        'isbn':book.isbn,
        'key':key
        
    }
    
    context = {
        'book_detail':book_detail
    }
    return render(request,'app1/update_book.html',context)

    
    
    
    

login_required
@api_view(http_method_names=['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def update_book(request,pk):
    print("updates",pk)
    
    id = int(pk)
    task = BookEntry.objects.get(id = id,library_admin=request.user)
    print("task before--------",task)
    print(request.data)
    serializer = BookEntrySerializer(instance=task, data=request.data,partial=True)
    
    
    if serializer.is_valid():
        serializer.save(library_admin=request.user)
        print(serializer.data)

    else:
        print("error _____",serializer.errors)
        
        
    return Response(serializer.data)



login_required
@api_view(http_method_names=['DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def delete_book(request,pk):
    print("updates",pk)
    
    id = int(pk)
    book = BookEntry.objects.get(id = id,library_admin=request.user)
    print("task before--------",book)
    
    
    book.delete()
        
    return Response('Item succsesfully delete!')



def create_user(request):
    print("in sign up111--------")
    print(request)

    if request.method == 'POST':
        print("in sign up")
        username = request.POST['email']
        password = request.POST['password']
        print(username,password)
        myuser = User.objects.create_user(username, password=password)
        myuser.save()
        return redirect('app1:login_view')
    return render(request,'app1/signup.html')

def login_view(request):
    print("in login-------")
    print(request)
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['email']
        loginpassword=request.POST['password']
        print(loginusername,loginpassword)

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
        return redirect("app1:index")
        # else:
        #     print("*************invalid credeentials")
        #     return render(request,'bus_data_app/errors.html')

    return render(request,'app1/logins.html')
@login_required
def logout_view(request):
    print("in logout")
    print(request)
    logout(request)
    return redirect('app1:home')