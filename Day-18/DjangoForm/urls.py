from django.urls import path
from DjangoForm import views

urlpatterns = [
	path('dynamichtmlform/',views.dynamicHtmlFormGen,name='dhfg'),
	# path('register/',views.registerForm,name='register'),
	# path('fetchAll/',views.fetchAll,name='fetchAll'),
	path('',views.home,name="hm"),
	path('rg/',views.rgform,name="reg"),
	path('ft/',views.fetchall,name="ftc"),
	path('up/<int:id>/',views.upd,name="p"),
]