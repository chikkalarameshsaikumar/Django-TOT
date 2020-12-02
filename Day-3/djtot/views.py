from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse("This is HomePage")

def abts(r):
	return HttpResponse("<h2 style='background-color:green;color:white;padding:3px;margin-left:230px;margin-right:230px'>This is AboutPage</h2>")

def rc(y,n):
	return HttpResponse("<h2>Hi Welcome {}</h2>".format(n))