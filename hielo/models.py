from django.db import models

# Create your models here.

#Creating model
class Todolist(models.Model):
	text = models.CharField(max_length = 45)
	completed  = models.BooleanField(default = False)

	def __sdr__(self):
		return self.text