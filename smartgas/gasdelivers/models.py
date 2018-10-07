from django.db import models
from register.models import Client

#this models will be handling all orders made by  i client

class Orders(models.Model):
	 WALLET = 'WL'
	 CASH_ON_DELIVERY='COD'
	 PAYMENT_METHOD=((WALLET,'WL'),
	 	(CASH_ON_DELIVERY,'COD'))
	 Client_id = models.ForeignKey(Client, on_delete=models.PROTECT)
	 payment_method = models.CharField(max_length=2,choices=PAYMENT_METHOD,default=CASH_ON_DELIVERY,)
	 location= models.CharField(max_length=200)
	 order_date = models.DateTimeField(auto_now_add=True)