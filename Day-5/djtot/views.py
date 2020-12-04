from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse("This is HomePage")

def abts(r):
	return HttpResponse("<h2 style='background-color:green;color:white;padding:3px;margin-left:230px;margin-right:230px'>This is AboutPage</h2>")

def rc(y,n):
	return HttpResponse("<h2>Hi Welcome {}</h2>".format(n))

def tblpnt(request,y):
	j = ""
	for m in range(1,11):
		j += "{} X {:02} = {:02}".format(y,m,y*m)+"<br/>"
	# print(j)
	return HttpResponse(j)

def rcds(request,name,age):
	# print(name,age)
	p = {'n':name,'a':age}
	return render(request,'fy/usrdt.html',p)

def sample(request):
	return render(request,'fy/demo.html')