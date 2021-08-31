from django.shortcuts import render

def work(request):
    return render(request, 'work/work.html')
