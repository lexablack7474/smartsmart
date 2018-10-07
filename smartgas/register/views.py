from django.shortcuts import render, get_object_or_404
from register.models import Client
from django.template import loader
from django.urls import reverse
from register.forms import RegForm

#This view deals with regestering 


def register(request):
	if request.method == 'POST':
		form = RegForm(request.POST)
		if form.is_valid():
			form.save()
			# How can i redirect the client of he successed regestering can i use HttpResponseRedirect()
			#how can i check if the emailis valid 
			#how can i hash the password 
			
	else:
		form = RegForm()
	return render(request, 'smart/register.html', {'form':form})
