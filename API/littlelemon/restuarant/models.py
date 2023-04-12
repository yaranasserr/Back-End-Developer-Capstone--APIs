from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    BookingDate = models.DateField()
    No_of_guests = models.SmallIntegerField()
   

# Add code to create Menu model
class Menu(models.Model):
   Title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10, decimal_places=2)
   inventory=models.IntegerField()
   
class MenuItem(models.Model):
    Title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    def get_item(self):
        
        return f'{self.title} : {str(self.price)}'
