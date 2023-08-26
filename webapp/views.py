from django.shortcuts import render, redirect
import datetime
from webapp.models import webuser, post
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    date = datetime.datetime.now()
    username = request.user.username

            # function for post
    posts = post.objects.all()
    
    data={
        'date':date,
        'username' : username,
        'posts':posts
    }
    return render(request, 'index.html', data)



def signup(request):
    if request.method== "POST":
            name=request.POST.get("name")
            username=request.POST.get("username")
            email=request.POST.get("email")
            password=request.POST.get("password")

            if User.objects.filter(username=username).exists():
                messages.warning(request, f'Username is already taken')
                return redirect('../signup')

            # Check if the email is already registered
            if User.objects.filter(email=email).exists():
                messages.warning(request, "Email is already registered")
                # return redirect('../signup')

            # Create the user
            user = User.objects.create_user(username=username, email=email, first_name=name, password=password)
            
            user.save()
            
            # return render(request, 'userlogin.html')
            return redirect('../userlogin')

    return render(request, 'signup.html')

def userlogin(request):
     if request.method == "POST":
          
        username = request.POST.get("username")
        password = request.POST.get("password")

        # log = User()

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            
            # return render(request, 'index.html')
            messages.success(request, "Login Successfully!")
            return redirect('../')

        else:
            messages.warning(request, "Bad credentials. Try again with vaild username & password! ")
            
            return render(request, 'userlogin.html')
        

     return render(request, 'userlogin.html')

@login_required
def update(request):
    #  return render(request, 'update.html')
    if request.user.is_authenticated:
        if request.method=='POST':
            name=request.POST.get("name")
            email=request.POST.get("email")
            provided_password =request.POST['password']

            
            # user password checking
            user = request.user
            password_is_currect = user.check_password(provided_password)
                
            if password_is_currect:
                
                # Check if the email is already registered
                if email:
                    if User.objects.filter(email=email).exclude(username = user.username).exists():
                        messages.warning(request, "Email is already registered. Try another email!")
                        return redirect('../profile')
                    user.email=email

                if name:
                    user.first_name=name
        
                user.save()
                messages.success(request, "Information updated successfully!")
                return redirect('../profile')
            else:
                messages.warning(request, "Password doesn't match!")
                
                return redirect('../')

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('../')
    
@login_required
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('../')

@login_required
def upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES.get('image'):
            name = request.POST.get('name')
            description = request.POST.get('description')
            p_image = request.FILES.get('image')
            date = request.POST.get('datetime')
            

            u_post = post()
            u_post.name = name
            u_post.discription = description
            u_post.postimage = p_image
            u_post.datetime = date
            
            
            u_post.save()
            messages.success(request, 'Content Uploaded Successfully!')
            # return render(request, 'index.html')
            return redirect('../')
        
        date = datetime.datetime.now()
        return render(request, 'upload.html', {'date':date})
    else:
        return redirect('../home')