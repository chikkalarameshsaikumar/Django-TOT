from django.shortcuts import render,redirect
from .forms import Usreg
from django.contrib import messages 

# Create your views here.

def home(request):
	return render(request,'ht/home.html')

def about(request):
	return render(request,'ht/about.html')

def contact(request):
	return render(request,'ht/contact.html')

def regi(request):
	if request.method == "POST":
		m=Usreg(request.POST)
		if m.is_valid():
			e = m.save(commit=False)
			e.save()
			messages.warning(request,"Hi {} you are successfully registered".format(e.username))
			return redirect("/")
	m = Usreg()
	return render(request,'ht/registration.html',{'y':m})