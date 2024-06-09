from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=50, blank=False)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, blank=False, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()


    def __str__(self) -> str:
        return self.name
    

STATUS_CHOICES = (
    ('pending','pending'),
    ('completed','completed'),
    ('canceled','canceled'),
)

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()


