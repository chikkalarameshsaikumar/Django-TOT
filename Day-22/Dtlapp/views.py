from django.shortcuts import render,redirect
from .forms import Usreg,Updtl,ImPfl
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Upd
from Dj3 import settings
from django.core.mail import send_mail
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

@login_required
def mailsnd(request):
	p = User.objects.values_list("email",flat=True)
	if request.method == "POST":
		# rc = request.POST['rcv'].split(",")
		z = []
		a = request.user.email
		rs = list(filter(None,p))
		for n in rs:
			if n == "" or n == a:
				continue
			else:
				z.append(n)
		print(z)
		sb = request.POST['sub']
		mg = request.POST['msg']
		snd = settings.EMAIL_HOST_USER
		t = send_mail(sb,mg,snd,z)
		if t == 1:
			messages.success(request,"Mail send to {} successfully".format(z))
			return redirect('/ml')
		messages.warning(request,"Mail doesn't send because of invalid mail id {}".format(z))
	return render(request,'ht/mailsending.html')