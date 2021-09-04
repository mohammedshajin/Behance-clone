from django.shortcuts import redirect, render
from .models import Work
from .forms import Workform
from django.contrib.auth.decorators import login_required
from users.models import Profile
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage


def work(request):
    works = Work.objects.all()
    page = request.GET.get('page')
    results = 6
    paginator =Paginator(works, results)
    try:
        works = paginator.page(page)
    except PageNotAnInteger:
        page=1
        works = paginator.page(page)
    except EmptyPage:
        page= Paginator.num_pages
        works = paginator.page(page)

    context = {'works':works, 'paginator':paginator}
    return render(request, 'work/work.html', context)

def work_single(request, pk):
    work = Work.objects.get(id=pk)
    context = {'work':work}
    return render(request, 'work/work_single.html', context)

@login_required(login_url="login")
def creatework(request):
    profile = request.user.profile
    form = Workform()
    if request.method == 'POST':
        form=Workform(request.POST, request.FILES)
        if form.is_valid():
            work = form.save(commit=False)
            work.profile = profile
            work.save()
            return redirect('work')
    
    context = {'form':form}
    return render(request, 'work/creatework.html', context)

def search(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query= request.GET.get('search_query')
        works = Work.objects.distinct().filter(Q(title__icontains = search_query))
        
    
    context = {'works': works, 'search_query': search_query}

    return render(request, 'work/search.html', context)
    