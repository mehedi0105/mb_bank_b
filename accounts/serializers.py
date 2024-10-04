from rest_framework import serializers
from . import models as acc
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class OpenAccountSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required = True)
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True)
    confirm_password = serializers.CharField(required = True)

    class Meta:
        model = acc.Account
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
            'account_no',
            'account_balance',
            'date_of_birth',
            'nid_no',
            'account_type',
            'district',
            'city',
            'country',
            'street_address',
            )
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        account_no = self.validated_data['account_no']
        account_balance = self.validated_data['account_balance']
        date_of_birth = self.validated_data['date_of_birth']
        nid_no = self.validated_data['nid_no']
        account_type = self.validated_data['account_type']
        district = self.validated_data['district']
        city = self.validated_data['city']
        country = self.validated_data['country']
        street_address = self.validated_data['street_address']

        if password != confirm_password:
            return serializers.ValidationError({'error':"password doesn't match"})
        
        if User.objects.filter(username = username).exists():
            return serializers.ValidationError({'error':'username is already exsits'})
        
        if User.objects.filter(email = email).exists():
            return serializers.ValidationError({'error':'email is already exists'})
        
        account = User(username = username, first_name = first_name, last_name = last_name, email = email)
        account.set_password(password)
        account.save()

        acc.Account.objects.create (
            user = account,
            account_no = account_no,
            account_balance = account_balance,
            date_of_birth = date_of_birth,
            nid_no = nid_no,
            account_type = account_type,
            district = district,
            city = city,
            country = country,
            street_address = street_address
        )
        return account


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = acc.Account
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'