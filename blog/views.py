from django.shortcuts import render
from .models import Post
# Create your views here.

def showblog(request):
	post = Post.objects
	return render(request, 'blog/blog.html', {'post': post})