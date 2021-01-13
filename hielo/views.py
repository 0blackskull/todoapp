from django.shortcuts import render

from .models import Todolist

# Create your views here.

def index(request):
	link_items = Todolist.objects.order_by('id')#Id for seuqential order
	context = {'link_items' : link_items}
	return render(request, 'index.html', context)