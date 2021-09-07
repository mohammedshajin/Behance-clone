from work.models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Follow

from .forms import ProfileForm, MessageForm

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    myprofile = request.user.profile
    
    follow = Follow.objects.filter(following=myprofile, follower=profile)
    if follow:
        followed = True
    else:
        followed = False
    context = {'profile': profile, 'followed': followed}
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

@login_required(login_url='login')
def viewmessage(request, pk):
    profile =  request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save
    context = {'message':message}
    return render(request, 'users/message.html', context) 

@login_required(login_url='login')
def createmessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    try:
        sender = request.user.profile
    except:
        sender = None
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit = False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name =sender.name
                
            message.save()
            return redirect('other_profile', pk=recipient.id)


    context = {'recipient':recipient, 'form':form}
    return render(request, 'users/message-form.html', context) 

@login_required(login_url='login')
def follow(request, pk):
    profile = request.user.profile
    follower = Profile.objects.get(id=pk)
    follow = Follow.objects.create(following=profile, follower=follower)


    return redirect('other_profile', pk=follower.id)

@login_required(login_url='login')
def unfollow(request, pk):
    profile = request.user.profile
    follower = Profile.objects.get(id=pk)
    follow = Follow.objects.filter(following=profile, follower=follower)
    follow.delete()
    return redirect('other_profile', pk=follower.id)
