







import re
from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import note
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'index.html')
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        email =request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username already exists')
                return redirect('signin')
            elif User.objects.filter(email =email).exists():
                messages.info(request,'Email  already exists')
                return redirect('signin')
            else:
                messages.info(request,'Successfully signin')
                user = User.objects.create_user(username = username,password=password1,email=email)
                user.save()
        else:
            messages.info(request,"Password does'nt match")
            return redirect('signin')
        return redirect('login')
    else:
        return render(request,'signin.html')

def login(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url="/login")
def home(request):
    context = {
        'success':False
    }
    if request.user.is_authenticated:
        user =request.user
        if request.method =="POST":
            title = request.POST['title']
            desc = request.POST['desc']
            ins = note(title = title,desc = desc,user=user)
            
            ins.user = user
            ins.save()            
            context = {
            'success':True
            
            }
            print(title)
        
    return render(request, 'home.html',context)
@login_required(login_url="login")
def notes(request):
    if request.user.is_authenticated:
        user =request.user

        allnotes = note.objects.filter(user =user)
        colors =['secondary','success','warning','light']
        context = {
            'notes':allnotes,
            'color':colors
        }
       
        
        return render(request,'notes.html',context=context)
    
def delete(request,id):
    note_user = note.objects.get(id=id)
    note_user.delete()
    return HttpResponseRedirect(reverse('notes'))



def edit(request,id):
    note_user = note.objects.get(id=id)
    tit = note_user.title
    des =note_user.desc
    if request.method == "POST":
        note_user = note.objects.filter(id = id)
        title =request.POST['title']
        desc = request.POST['desc']
        note_user.update(title=title, desc = desc)
        

        return HttpResponseRedirect(reverse('notes'))
    print(note_user.title)
        
        
    
    

    
    return render(request,'edit.html')


   
    
    