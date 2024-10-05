from rest_framework import serializers
from . import models as md

class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = md.Transaction 
        fields = '__all__'  

class LoanSerializers(serializers.ModelSerializer):
    class Meta:
        model = md.Loan
        fields = '__all__'


