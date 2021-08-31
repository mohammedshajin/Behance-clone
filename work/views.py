from django.shortcuts import render
from .models import Work

def work(request):
    works = Work.objects.all()
    context = {'works':works}
    return render(request, 'work/work.html', context)

def work_single(request, pk):
    work = Work.objects.get(id=pk)
    context = {'work':work}
    return render(request, 'work/work_single.html', context)
