from django.shortcuts import render
from register.models import Client
from .models import Orders
from django.template import loader
from django.http import HttpResponse

#this will be user home page 


def index(request):

	client_list= Client.objects.order_by('-name')[:5]
	#template = loader.get_template('smart/index.html')
	context = {

	'client_list':client_list,
	}

	return render(request, 'smart/index.html', context)




def index(request):

	client_list= Client.objects.order_by('-name')[:5]
	#template = loader.get_template('smart/index.html')
	context = {

	'orders_list':orders_list,
	}

	return render(request, 'smart/index.html', context)