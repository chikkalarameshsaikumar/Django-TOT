from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from DjangoForm.forms import DynamicHtmlFormGen, RegisterForm

def registerForm(request):
	f = RegisterForm()
	return render(request,'DjangoForm/registerForm.html',{"f":f})



def dynamicHtmlFormGen(request):
	 # return HttpResponse("hi i am working fine")
	 t = DynamicHtmlFormGen()
	 return render(request,'DjangoForm/dynamicHtmlFormGen.html',{'form':t})