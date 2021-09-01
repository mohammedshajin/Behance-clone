from django.shortcuts import render

def profile(request):
    return render(request, 'users/profile.html')
