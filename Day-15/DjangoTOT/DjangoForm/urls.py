from django.urls import path
from DjangoForm import views

urlpatterns = [
	path('dynamichtmlform/',views.dynamicHtmlFormGen,name='dhfg'),
	path('register/',views.registerForm,name='register'),
]