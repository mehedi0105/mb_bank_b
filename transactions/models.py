from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account
from .constraints import TRANSACTION_TYPE, LOAN_TYPE
from django.utils import timezone
# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12,default=0)
    transaction_type = models.CharField(max_length=100, choices=TRANSACTION_TYPE)
    transaction_status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date']

class Loan(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    loan_type = models.CharField(max_length=100, choices=LOAN_TYPE)
    loan_status = models.BooleanField(default=False)
    loan_approve = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.account.first_name} {self.account.last_name}"

    