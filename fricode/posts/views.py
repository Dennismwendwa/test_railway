from django.shortcuts import render
from django.urls import path

def post(request):

	return render(request, "post/index.html", {})

# Create your views here.
