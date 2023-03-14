from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from time import sleep

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    # tasks = Task.objects.order_by('title')
    # tasks = Task.objects.order_by('-id')[:1]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('count')
        else:
            error = "Форма была неверной"

    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/task.html', context)

def about(request):
    return render(request, 'main/about.html')

def blog(request):
    return render(request, 'main/blog.html')

def count(request):
    tasks = Task.objects.all()
    return render(request, 'main/count.html', {'title': 'Расчет', 'tasks': tasks})


stocks = ['Аэрофлот', 'Альфабанк', 'Мосбиржа']
num = [100, 200, 300]

for i in range(len(stocks)):
    tasks = Task.objects.create(title=stocks[i], task=num[i])

