from django.shortcuts import render
from datetime import date
from datetime import datetime, timedelta
import jwt
from decouple import config
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render
from passlib.hash import django_pbkdf2_sha256 as handler
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from django.db.models import Avg
from django.db.models import Max
from django.db.models import FloatField
from django.db.models import Count
from django.db.models import Avg, Max, Min,Sum
from django.db.models import F, Q, When
from django.db.models import Case, CharField, Value, When
import api.CalDis as cl  
import random


 #Role Post_Api
class client(APIView):
    def get(self, request):
      # data = Client.objects.values('name','registered_on') 
      # data =  Client.objects.annotate(discount=Case(When(account_type=Client.GOLD, then=Value('5%')),When(account_type=Client.PLATINUM, then=Value('10%')),default=Value('0%'),output_field=CharField(),),).values_list('name', 'discount')   
      
      data = Client.objects.values('name')
           
      return Response({'status':True, 'data': data})
    def post(self,request):
        Client.objects.create(name='ALI',account_type=Client.REGULAR,registered_on=date.today() - timedelta(days=5))
        Client.objects.create(name='KHAN',account_type=Client.GOLD,registered_on=date.today() - timedelta(days=36))
        Client.objects.create(name='RAZA',account_type=Client.PLATINUM,registered_on=date.today() - timedelta(days=10 * 365))
        data = Client.objects.values()    
        return Response({'status':True, 'data': data})
class product(APIView):
   def get(self,request):
      data = Product.objects.values()
      return Response({'status':True,'Data':data})
   def post(self,request):
      Product.objects.create(name = 'PEPSI',price = 250,account_type=Product.REGULAR)
      Product.objects.create(name = 'COMPUTERS',price = 7500,account_type=Product.DIMOND)
      Product.objects.create(name = 'LAPTOPS',price = 12000,account_type=Product.DIMOND)
      Product.objects.create(name = 'LED',price = 2500,account_type=Product.GOLD)
      Product.objects.create(name = 'MOBILES',price = 5000,account_type=Product.PLATINUM)
      data = Product.objects.values()    
      return Response({'status':True, 'data': data})
   

class ProductOfClient(APIView):
   def get(self,request):
      Clnt = Client.objects.values('name')      
      Pr = Product.objects.values('name','price')      
      data =  Client.objects.annotate(discount=Case(When(account_type=Client.GOLD, then=Value('5%')),When(account_type=Client.PLATINUM, then=Value('10%')),default=Value('0%'),output_field=CharField(),),).values_list('name', 'discount','account_type')         
      return Response({'status':True,'Client':data}) 

   
   
class CalcDiscount(APIView):   
   def post(self,request):
      a = int(request.data.get('a'))
      b = int(request.data.get('b'))
      percentage = (b * a)/100
      # percentage =  b /a 
      dis = b-percentage      
      return Response({'status':True,'Discounted_Value':dis})

   


class productdiscount(APIView):
   def get(self,request):
      # data = Product.objects.values()  
      data =  Product.objects.annotate(discount=Case(When(account_type=Product.GOLD, then=Value('5%')),When(account_type=Product.PLATINUM, then=Value('10%')),When(account_type=Product.DIMOND, then=Value('10%')),default=Value('0%'),output_field=CharField(),),).values_list('name', 'discount','account_type')              
      return Response({'status':True,'Data':data})

class Clientproduct(APIView):
   def get(self,request):
      clint = Client.objects.all().values('name')
      for i in range(len(clint)):
         pro = Product.objects.all().values('name','price')
         if clint:
            clint[i]['clint'] = pro
         else:   
            clint[i]['clint'] = ''

      return Response({'status':True,'Data':clint})


class discounted(APIView):
   def post(self,request):
      p = Product.objects.values('price')
      a = int(request.data.get('a'))
      b = int(request.data.get('b'))            
      data =  Product.objects.annotate(discount=Case(When(account_type=Product.GOLD, then=Value('25%')),When(account_type=Product.PLATINUM, then=Value('50%')),When(account_type=Product.DIMOND, then=Value('10%')),default=Value('0%'),output_field=CharField(),),).values_list('name','price', 'discount','account_type')              
      dicount = cl.calculatediscount(a,b)
      return Response({'status':True,'Discount':dicount,"data":data})
class Show(APIView):
   def get(self,request):
    data1 =  Client.objects.aggregate(regular=Count('pk', filter=Q(account_type=Client.REGULAR)),gold=Count('pk', filter=Q(account_type=Client.GOLD)),platinum=Count('pk', filter=Q(account_type=Client.PLATINUM)),)
    return Response({'status':True,"data":data1})



from django.db.models import Case, When, Value, IntegerField

discounted_products = Product.objects.annotate(discounted_price=Case(When(on_sale=True, then=Value(0.9)*F('price')),default=Value(F('price')),output_field=IntegerField()
    )
)