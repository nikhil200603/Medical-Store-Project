from django.db import models
from datetime import date

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    class Meta:
        db_table="medicine_category_table"

class Medicine(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.IntegerField()
    date_of_manufacture=models.DateField(auto_now_add = True)
    expiry=models.CharField(max_length=100)
    power_in_mg=models.IntegerField()
    manufactured_by=models.CharField(max_length=100)

    # class Meta:
    #     db_table="medicine_table"

class Check(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
