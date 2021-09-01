from django.shortcuts import redirect, render
from .models import Work
from .forms import Workform

def work(request):
    works = Work.objects.all()
    context = {'works':works}
    return render(request, 'work/work.html', context)

def work_single(request, pk):
    work = Work.objects.get(id=pk)
    context = {'work':work}
    return render(request, 'work/work_single.html', context)

def creatework(request):
    form = Workform()
    if request.method == 'POST':
        form=Workform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work')
    
    context = {'form':form}
    return render(request, 'work/creatework.html', context)
    