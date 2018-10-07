from django.db import models

class Client(models.Model):
	name = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	device_serial = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	supplier_id = models.CharField(max_length=15)
	password = models.CharField(max_length=200)
	service_date = models.DateTimeField(auto_now_add=True)



class Devices(models.Model):
	name = models.CharField(max_length=200)
	device_serial = models.CharField(max_length=200)
	owner = models.ForeignKey(Client, on_delete=models.PROTECT)
	size = models.CharField(max_length=200)