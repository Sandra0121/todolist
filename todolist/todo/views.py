from django.shortcuts import render, redirect
from .models import Todo
from django.http import JsonResponse

# Create your views here.
def index_view(request):
    todo =Todo.objects.all()
    
    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')
    return render (request, 'todo/index.html', {'todos':todo})

    # return render(request, 'index.html', {'todos': todo})
def getTodo(request):
    todo = Todo.objects.all()
    return JsonResponse({'todos': list(todo.values())})


def delete_view(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')
