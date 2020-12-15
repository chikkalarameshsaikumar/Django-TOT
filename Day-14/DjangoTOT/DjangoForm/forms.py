from django import forms

gender_choices = [('Male',"Male"),('FeMale',"FeMale")]
langs = [('Python','Python'),('Java','Java'),('Django','Django')]
class DynamicHtmlFormGen(forms.Form):
	fullname = forms.CharField()
	lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Last Name",'class':"lastname row col-sm-8 card form-control"}))
	age = forms.CharField(widget= forms.NumberInput())
	gender  = forms.ChoiceField(widget=forms.RadioSelect,choices=gender_choices)
	select_gender  = forms.ChoiceField(widget= forms.Select,choices=gender_choices)
	selectLang  = forms.MultipleChoiceField(widget= forms.CheckboxSelectMultiple,choices=langs)