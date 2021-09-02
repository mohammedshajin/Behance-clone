from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def profile(request):
    return render(request, 'users/profile.html')

def loginUser(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect ('work')


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, "user doesnot exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')

        else:
            messages.error(request, "username or password incorrect")

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = "register"
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account created")

            login(request, user)

            return redirect('profile')
        else:
            messages.success(request, 'An error occured')

    context = {'page':page, 'form':form}

    return render(request, 'users/login_register.html', context)
    

