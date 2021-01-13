from django.shortcuts import render, redirect

from .models import Todolist
from .forms import TodoListForm

from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
	link_items = Todolist.objects.order_by('id')#Id for seuqential order
	context = {'link_items' : link_items}
	return render(request, 'index.html', context)

@require_POST
def addTodoItem(request):
	form = TodoListForm(request.POST)
	
	if form.is_valid(): 
		newTodo = Todolist(text = request.POST['text'])
		newTodo.save()
		return redirect('index')
