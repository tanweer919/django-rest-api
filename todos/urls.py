from django.urls import path
from .views import createtodo, fetchtodo, fetchtodos, modifyTodo

urlpatterns = [
    path('todos/', fetchtodos, name="todos"),
    path('todo/<int:id>', fetchtodo, name="todo"),
    path('todo/new', createtodo, name= 'newtodo'),
    path('todo/<int:id>/modify', modifyTodo, name='modifyTodo')
]