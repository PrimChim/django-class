from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        print(password, password2)
        if password == password2:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=email,email=email,password=password)
            user.save()
            return render(request, 'signup.html', {"message":"User created Successfully!!!"})
        else:
            return render(request, 'signup.html', {"error":"Passwords didn't match !!!"})
    return render(request,'signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'login.html',{'error':'User or password is incorrect!!!'})
    return render(request, 'login.html')