from django.shortcuts import render
from django.urls import path
from . models import Post

def post(request):

	posts = Post.objects.all()




	return render(request, "post/index.html", {
			'posts': posts,
			})

def detail(request, pk):

	return render(request, "post/detail.html", {})

def category(request):

	return render(request, "post/category.html", {})
