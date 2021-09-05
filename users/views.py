from work.models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render (request, 'users/other_profile.html', context)

def loginUser(request):


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

    return render(request, 'users/signin.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account created")

            login(request, user)

            return redirect('edit-account')
        else:
            messages.success(request, 'An error occured')

    context = {'form':form}

    return render(request, 'users/register.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    works = profile.work_set.all()


    context = {'profile':profile, 'works': works}

    return render(request, 'users/profile.html', context) 


@login_required(login_url='login')
def editAccount(request):
    profile=request.user.profile
    form = ProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context) 

@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageReq = profile.messages.all()
    unreadcount = messageReq.filter(is_read=False).count()
    context = {'messageReq': messageReq, 'unreadcount': unreadcount}
    return render(request, 'users/inbox.html', context) 


