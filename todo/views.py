from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def home(request):
    author = request.user
    todos = Todo.objects.filter(author=author).order_by('-created_at')
    search = request.GET.get('search')
    search = request.GET.get('search')
    post = request.GET.get('q')
    if post:
        todos = todos.filter(status=post)
    if search:
        todos = todos.filter(title__icontains=search)
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)


def create(request):
    user = request.user
    form = TodoForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = user
        obj.save()
        # messages.success(request, 'successfully created')
        return redirect('/')

    return render(request, 'create.html', {'form': form})


def update(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        return redirect('/')
    ctx = {
        'form': form
    }
    return render(request, 'single.html', ctx)


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method=='POST':
        todo.delete()
        return redirect('/')
    return render(request, 'delete.html')







