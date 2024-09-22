from django.shortcuts import render, redirect
from rest_framework.views import APIView
from . import serializers as src
from rest_framework.response import Response 
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from rest_framework.authtoken.models import Token
from .models import Account
from decimal import Decimal

# Create your views here.

class OpenAccount(APIView):
    serializer_class = src.OpenAccountSerializers

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/is_activeate/{uid}/{token}/"
            name = f"Hello {user.first_name} {user.last_name}"
            email_subject = "Verify Your Email Address - Complete Your Registration"
            email_body = render_to_string('./openaccount.html',{
                'confirm_link':confirm_link,
                'name':name
                })
            email = EmailMultiAlternatives(email_subject,to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response({"message": "Check your email for confirmation"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def is_activeate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk = uid)
    except User.DoesNotExist():
        user = None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('https://phitron.gitbook.io/django/module_1/module_1_1')
    else:
        return HttpResponse("Activation link is invalid!", status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self,request):
        serializer = src.LoginSerializers(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            # print(password)
            
            user = authenticate(username=username,password=password)
            if user:
                token,_=Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token':token.key,'user_id':user.id})
            return Response({'error':'Invalid Cradintial'})
        return Response(serializer.data)

class Logout(APIView):
    def get(self,request):
        token = Token.objects.get(user = request.user)
        token.delete()
        logout(request)
        return redirect('https://phitron.gitbook.io/django/module_1/module_1_1')
