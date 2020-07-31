from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
	image = models.ImageField(upload_to='blog_images/')
	text = models.TextField()
	title = models.CharField(max_length=300)
	date = models.DateField()