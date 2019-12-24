from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)  # you have to declare max_length field - compulsory
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=50)
    summary = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank= True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank= True, null=True)

