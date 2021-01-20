from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator


class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100, unique=True)
    acoount_no = models.CharField(max_length=220, unique=True)
    password = models.CharField(max_length=100)
    current_balance = models.FloatField(
        validators=[MinValueValidator(3000.00)])


class Transfer(models.Model):
    tx_from = models.ForeignKey(
        Customers, related_name="tx_from", on_delete=models.CASCADE, null=True)
    tx_to = models.ForeignKey(
        Customers, related_name="tx_to", on_delete=models.CASCADE, null=True)
    amount = models.FloatField(validators=[MaxValueValidator(100000.00)])
