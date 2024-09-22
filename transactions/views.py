from typing import Any
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Transaction, Loan
from rest_framework.views import APIView
from .constraints import TRANSACTION_TYPE
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .serializers import TransactionSerializers, LoanSerializers
from decimal import Decimal
from accounts.models import Account
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


# Create your views here.
class Statement(APIView):

    def get(self,request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializers(transactions, many = True)
        return Response(serializer.data)

    def post(self,requst):
        serializer = TransactionSerializers(data = requst.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




# class YourView(APIView):
#  # ইউসার লগইন না থাকলে request ব্লক হবে

#     def post(self, request):
#         # user = request.user  # এখানে ইউসার পাওয়া যাবে
#         user = Account.objects.get(user=11)
#         return Response({'message': f'Hello {user}'})
    
class Deposit(APIView):

    def post(self, request):
        amount = request.data.get('amount')
        account_no = request.data.get('account_no')
        id = request.data.get('id')
        user = User.objects.get(id=id)
        account = Account.objects.get(account_no=account_no)
        if amount is not None:
            balance = Decimal(amount)
            account.account_balance += balance
            account.save()

            transactions = Transaction.objects.create(
                account = user,
                amount = balance,
                transaction_type='deposit',
                transaction_status = True

            )
            transactions.save()
            return Response({"success": "Deposit Success"}, status=status.HTTP_200_OK)
        return Response({"error": "Amount is None."}, status=status.HTTP_400_BAD_REQUEST)
    

class Withdraw(APIView):

    def post(self, request):
        amount = request.data.get('amount')
        account_no = request.data.get('account_no')
        id = request.data.get('id')
        user = User.objects.get(id=id)
        account = Account.objects.get(account_no=account_no)
        if amount is not None:
            balance = Decimal(amount)
            account.account_balance -= balance
            account.save()

            transactions = Transaction.objects.create(
                account = user,
                amount = balance,
                transaction_type='withdraw',
                transaction_status = True

            )
            transactions.save()
            return Response({"success": "Withdraw Success"}, status=status.HTTP_200_OK)
        return Response({"error": "Amount is None."}, status=status.HTTP_400_BAD_REQUEST)

class TransferMoney(APIView):

    def post(self,request):
        amount = request.data.get("amount")
        account_no = request.data.get('recipent_account_no')
        id = request.data.get('id')
        user = User.objects.get(id=id)
        sender_account_no = Account.objects.get(user=id)
        recipent_account_no = Account.objects.get(account_no=account_no)
        if sender_account_no == recipent_account_no:
            return Response({"error":""},status=status.HTTP_400_BAD_REQUEST)
        if amount is not None:
            print(sender_account_no," A-> ",recipent_account_no)
            balance = Decimal(amount)
            sender_account_no.account_balance -= balance
            recipent_account_no.account_balance += balance
            sender_account_no.save()
            recipent_account_no.save()

            transactions = Transaction.objects.create(
                account = user,
                amount = balance,
                transaction_type='transfer_money',
                transaction_status = True

            )
            transactions.save()
            return Response({"success": "Transfer Money Success"}, status=status.HTTP_200_OK)
        return Response({"error": "Amount is None."}, status=status.HTTP_400_BAD_REQUEST)


class Loan(APIView):
    # def get(self,request,pk=None):
    # #     loans = Loan.objects.all()
    # #     seializer = LoanSerializers(loans , many = True)
    # #     return Response (seializer.data)
    #     loans = Loan.objects.get()
    #     serializer = LoanSerializers(loans, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = LoanSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









    