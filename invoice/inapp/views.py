from django.shortcuts import render
from . serializers import InvoiceSerializers,InvoiceDetailSerializers,UserSerializer
from rest_framework import viewsets
from . models import Invoice,InvoiceDetail
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

# Create your views here.
class InvoiceViewset(viewsets.ModelViewSet):
    permissions_classes=(IsAuthenticated,)
    queryset=Invoice.objects.all().order_by('date')
    serializer_class=InvoiceSerializers


class InvoiceDetailViewset(viewsets.ModelViewSet):
    permissions_classes=(IsAuthenticated,)
    queryset = InvoiceDetail.objects.all().order_by('invoice')
    serializer_class = InvoiceDetailSerializers

class CreateuserView(CreateAPIView):
    model=get_user_model()
    permissions_classes=(AllowAny,)
    serializer_class=UserSerializer