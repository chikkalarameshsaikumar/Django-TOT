from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from DjangoForm.forms import DynamicHtmlFormGen, RegisterForm
from .models import Register

def registerForm(request):
	if request.method=='POST':
		#data  = request.POST
		#print(data)
		# name = data['name']
		# print(name)
		f = RegisterForm(request.POST)
		f.save()
		return HttpResponse("record inserted successfully...")
	f = RegisterForm()
	return render(request,'DjangoForm/registerForm.html',{"f":f})

def fetchAll(request):
	data  = Register.objects.all()
	#print(data)
	#return HttpResponse('check in cmd')
	return render(request,'DjangoForm/fetchAll.html',{'data':data})


def dynamicHtmlFormGen(request):
	 # return HttpResponse("hi i am working fine")
	 t = DynamicHtmlFormGen()
	 return render(request,'DjangoForm/dynamicHtmlFormGen.html',{'form':t})