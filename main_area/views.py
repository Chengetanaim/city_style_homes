from django.shortcuts import render, redirect
from .forms import QuestionForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .models import Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def index(request):
    object_list = Review.objects.order_by('-date_added')
    paginator = Paginator(object_list, 3) # 3 categories in each page
    page = request.GET.get('page')
    try:
        reviews = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        reviews = paginator.page(1)
        
    except EmptyPage:
        # If page is out of range deliver last page of results
        reviews = paginator.page(paginator.num_pages)
        
    context = {'reviews': reviews}
    return render(request, 'main_area/index.html', context)


@login_required
def about_us(request):
    return render(request, 'main_area/about_us.html')


@login_required
def contact_us(request):
    if request.method != 'POST':
        form = QuestionForm()
    else:
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_us')     
    context = {'form': form}
    return render(request, 'main_area/contact_us.html', context)


@login_required
def review(request):
    if request.method != 'POST':
        form = ReviewForm()
    else:
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')     
    context = {'form': form}
    return render(request, 'main_area/review.html', context)