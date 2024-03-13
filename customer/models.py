from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    mobile_no=models.CharField(max_length=13)
    address=models.CharField(max_length=200)
    
    class Meta:
        db_table = "customer_details"
