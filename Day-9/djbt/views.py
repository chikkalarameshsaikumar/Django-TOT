from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request,'bt/home.html')

def bttask(request):
	return render(request,'bt/boottask.html')

def logi(request):
	if request.method == "POST":
		u = request.POST['usname']
		p = request.POST['pswd']
		# print(u,p)
		# return HttpResponse("Hi Your Username is: {}".format(u))
		return render(request,'bt/details.html',{'us':u,'ps':p})
	return render(request,'bt/login.html')
