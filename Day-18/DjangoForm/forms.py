from django import forms
from .models import Register
# from django.forms import ModelForm

# class RegisterForm(forms.ModelForm):
# 	class Meta:
# 		model = Register
# 		fields = '__all__'
# 		#fields = ["name","age"]

# 		widgets = {
# 			"name":forms.TextInput(attrs={"placeholder":"Enter Name"}),
# 			"mobile_no":forms.TextInput(attrs={"placeholder":"Enter Mobile Number"}),
# 			"age":forms.NumberInput(attrs={"required":False,"placeholder":"Enter Age"}),
# 			"gender":forms.RadioSelect(attrs={'class':'radio-inline form-group','type':'radio'})
# 		}




gender_choices = [('Male',"Male"),('FeMale',"FeMale")]
langs = [('Python','Python'),('Java','Java'),('Django','Django')]
class DynamicHtmlFormGen(forms.Form):
	fullname = forms.CharField()
	lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Last Name",'class':"lastname row col-sm-8 card form-control"}))
	age = forms.CharField(widget= forms.NumberInput())
	gender  = forms.ChoiceField(widget=forms.RadioSelect,choices=gender_choices)
	select_gender  = forms.ChoiceField(widget= forms.Select,choices=gender_choices)
	selectLang  = forms.MultipleChoiceField(widget= forms.CheckboxSelectMultiple,choices=langs)


class Reg(forms.ModelForm):
	class Meta:
		model = Register
		fields = ["name","mobile_no","age","gender"]
		widgets ={
		"name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter your name",
			}),
		"mobile_no":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter your mobile number",
			}),
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter your age",
			}),
		"gender":forms.Select(attrs={
			'class':'form-control',
			'type':"radio",
			"placeholder":"select Gender",
			}),
		}
