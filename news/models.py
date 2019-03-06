from django.db import models

# Create your models here.
class News(models.Model):
	title = models.TextField()
	image = models.TextField()
	url = models.TextField()
	time = models.DateTimeField(auto_now=False, auto_now_add=True)
	website = models.TextField()

	def __str__(self):
		return self.title
