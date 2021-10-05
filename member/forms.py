from django import forms
from .models import Product_qna

class Writeproductqna(forms.ModelForm):
	class Meta:
		model = Product_qna
		fields = ['QTitle', 'Question']