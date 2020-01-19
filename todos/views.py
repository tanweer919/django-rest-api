from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from .serializers import TodoSerializer

# Create your views here.
def fetchtodos(request):
    todos = Todo.objects.all()
    data = {
        "todos": list(todos.values(
            "todo", "done", "id"
        ))
    }
    return JsonResponse(data)
def fetchtodo(request, id):
    todo = get_object_or_404(Todo, pk = id)
    data = {
        "todo": todo.todo,
        "done": todo.done
    }
    return JsonResponse(data)

@csrf_exempt
def modifyTodo(request, id):
    if request.method == 'POST':
        done = request.POST.get('done')
        todo = Todo.objects.get(pk=id)
        todo.done = done
        todo.save()
        serializedTodo = TodoSerializer(todo).data
        result = {
            "message": "Todo has been updated",
            "payload": serializedTodo
        }
        return JsonResponse(result)
@csrf_exempt
def createtodo(request):
    if request.method == 'POST':
        todo = request.POST.get('todo', '')
        done = request.POST.get('done', False)
        newTodo = Todo(todo=todo, done = done)
        newTodo.save()
        serializedTodo = TodoSerializer(newTodo).data
        result = {
            "message": "Todo have been successfully created",
            "payload": serializedTodo
        }
        return JsonResponse(result)
