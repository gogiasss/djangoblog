from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
	blog_image = models.ImageField(upload_to='blog_images/')
	blog_text = models.CharField(max_length=3000)
	blog_title = models.CharField(max_length=30)
	blog_date = models.DateField()