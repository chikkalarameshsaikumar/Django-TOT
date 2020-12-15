from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from DjangoForm.forms import DynamicHtmlFormGen

def dynamicHtmlFormGen(request):
	 # return HttpResponse("hi i am working fine")
	 t = DynamicHtmlFormGen()
	 return render(request,'DjangoForm/dynamicHtmlFormGen.html',{'form':t})