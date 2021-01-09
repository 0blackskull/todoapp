from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
	#We need to return in a request format too
	#return HttpResponse("<h1>Hello World</h1>") #Can put text without tags too
	return render(request, 'home.html', {'name':'Utkarsh'})#Callin the template
"""
But if we put all html here,
it would be a disaster. 
So, we can create a separate html file.
Now would this make the page static again!
This is where django is useful, we can create 
templates in which the data stored changes 
dynamically. 
DTL - Django Template Language
"""

def add(request):

	#These are str by default
	#val1 = int(request.GET['num1'])
	#val2 = int(request.GET['num2'])
	val1 = int(request.POST['num1'])
	val2 = int(request.POST['num2'])
	res = val1 + val2

	return render(request, 'result.html', {'result': res})
	#result is between {{}} in result.html so the res 
	#content goes to {{result}})
