from django.shortcuts import render
from django.urls import path

def post(request):

	return render(request, "post/index.html", {})

def detail(request, pk):

	return render(request, "post/detail.html", {})

def category(request):

	return render(request, "post/category.html", {})
