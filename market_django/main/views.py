from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    # tasks = Task.objects.order_by('title')
    # tasks = Task.objects.order_by('-id')[:1]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def blog(request):
    return render(request, 'main/blog.html')
