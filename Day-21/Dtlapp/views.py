from django.shortcuts import render,redirect
from .forms import Usreg,Updtl,ImPfl
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Upd

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
			return redirect("/lg")
	m = Usreg()
	return render(request,'ht/registration.html',{'y':m})

@login_required
def dashboard(request):
	return render(request,'ht/dashboard.html')

@login_required
def profile(request):
	return render(request,'ht/profile.html')

@login_required
def updf(request):
	if request.method == "POST":
		c = Updtl(request.POST,instance=request.user)
		y = ImPfl(request.POST,request.FILES,instance=request.user.upd)
		if c.is_valid() and y.is_valid():
			c.save()
			y.save()
			messages.success(request,"{} your details updated Successfully".format(request.user.username))
			return redirect("/pf")
	c = Updtl(instance=request.user)
	y = ImPfl(instance=request.user.upd)
	return render(request,'ht/updateprofile.html',{'b':c,'q':y})