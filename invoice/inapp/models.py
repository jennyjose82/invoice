from django.db import models


# Create your models here.
class Invoice(models.Model):
    date = models.DateField()
    invoice_number = models.IntegerField()
    customer_name = models.CharField(max_length=200)


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
