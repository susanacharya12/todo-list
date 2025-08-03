from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, TaskForm
from .models import Task

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('todo_list')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('todo_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def todo_list(request):
    query = request.GET.get('search', '')
    if query:
        tasks = Task.objects.filter(user=request.user, title__icontains=query)
    else:
        tasks = Task.objects.filter(user=request.user)
    
    incomplete_count = tasks.filter(completed=False).count()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo_list')
    else:
        form = TaskForm()
    
    context = {
        'tasks': tasks,
        'form': form,
        'incomplete_count': incomplete_count,
        'query': query,
    }
    return render(request, 'todo_list.html', context)

@login_required
def delete_task(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    task.delete()
    return redirect('todo_list')

@login_required
def complete_task(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('todo_list')
