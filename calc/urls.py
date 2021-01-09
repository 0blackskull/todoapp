from django.urls import path

from . import views#Dot implies from same directory 

urlpatterns = [
	path('', views.home, name='home'),#Now go to views to define views.home
	path('add',views.add, name='add')
]
"""
But all this stuff stays in calc,
but the project still remains empty.
So now go to the urls.py of mysite
and specify a path to this file in 
the paths in it.
"""
"""
Now create a new folder named templates
in the todoapp directory create the html file there.
Next, change the setting to put the template path.
Then change the views.py.
"""