from django import forms
from gasdelivers.models import Client

class RegForm(forms.ModelForm):

	class Meta:
		model = Client
		fields = ['name','phone','email','device_serial','location','supplier_id','password']
