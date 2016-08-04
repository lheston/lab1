from django import forms
from .models import Input

class InputForm(forms.ModelForm):
	class meta:
		model = Input
		fields = ('inURL')