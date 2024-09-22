from django.db import models
from django.contrib.auth.models import User
from . import constraints
# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    account_no = models.IntegerField(unique=True)
    account_balance = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    date_of_birth = models.DateField()
    nid_no = models.CharField(max_length=12)
    account_type = models.CharField(max_length=100, choices=constraints.ACCOUNT_TYPE)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.account_no}"
