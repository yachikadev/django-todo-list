from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {
        'todos': todos,
        'form': form,
        'remaining': todos.filter(completed=False).count(),
    })

@require_POST
def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

@require_POST
def delete_todo(request, pk):
    get_object_or_404(Todo, pk=pk).delete()
    return redirect('todo_list')
