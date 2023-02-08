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


def calculate_percentage(part, whole):
  Dis =  100 * float(part)/float(whole)
  return Response({'status':True,'Discount':Dis})



def calculatediscount(part, whole):
   a = int(part)
   b = int(whole)
   percentage = (b * a)/100   
   dis = b-percentage        
   return dis