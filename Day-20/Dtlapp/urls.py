from django.urls import path
from Dtlapp import views
from django.contrib.auth import views as v

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('reg/',views.regi,name="rg"),
	path('dsh/',views.dashboard,name="ds"),
	path('lg/',v.LoginView.as_view(template_name="ht/login.html"),name="log"),
	path('lgo/',v.LogoutView.as_view(template_name="ht/logout.html"),name="lgot"),
]