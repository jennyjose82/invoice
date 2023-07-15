from . models import Invoice,InvoiceDetail
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

class InvoiceSerializers(serializers.ModelSerializer):


    class Meta:
        model = Invoice
        fields = ['date', 'invoice_number', 'customer_name']


class InvoiceDetailSerializers(serializers.ModelSerializer):


    class Meta:
        model = InvoiceDetail
        fields = ['invoice', 'description', 'quantity', 'unit_price', 'price']
