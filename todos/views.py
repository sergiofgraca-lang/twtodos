from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Todo
from .forms import TodoForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("todos:list")

    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("todos:list")

    return render(request, "auth/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")





@login_required
def todo_list(request):
    todos = Todo.objects.all().order_by("-created_at")
    return render(request, "todos/todo_list.html", {"todos": todos})


@login_required
def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        form.save()
        todo.save()
        return redirect("todos:list")

    return render(request, "todos/todo_form.html", {"form": form})


@login_required
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)

    todo.delete()
    return redirect("todos:list")

@login_required
def todo_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid():
        form.save()
        return redirect("todos:list")

    return render(request, "todos/todo_form.html", {"form": form})

@login_required
def todo_complete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.completed = True
    todo.save()
    return redirect("todos:list")
