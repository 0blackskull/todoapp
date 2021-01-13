"""
For crearing forms we started by creating this file and importing forms from django 
Create a class that inherits Form from forms
Extract data from HTML through this class
Incorporate this form in views.py to bring it to front end
"""
from django import forms 

class TodoListForm(forms.Form):
	text = forms.CharField(max_length = 45,		#Maximum input is 45 letters
		widget = forms.TextInput(				#Widget handles the data extraction from HTML
			attrs = {'class':'form-control','placeholder':'Enter anything!','aria-label':'Todo','aria-describeby':'add-btn'}))	#attr is a dictionary