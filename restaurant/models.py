from django.db import models

class Booking(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	name = models.CharField(max_length=255, db_column='Name')
	no_of_guests = models.IntegerField(db_column='No_of_guests')
	booking_date = models.DateTimeField(db_column='BookingDate')

class Menu(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	name = models.CharField(max_length=255, db_column='Name')
	price = models.DecimalField(max_digits=10, decimal_places=2, db_column='Price')
	inventory = models.IntegerField(db_column='Inventory')

	def __str__(self):
		return f'{self.name} : {self.price}'
