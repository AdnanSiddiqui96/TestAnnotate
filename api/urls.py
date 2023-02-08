from django.urls import path,include
from api.views import *

urlpatterns = [

#web urls  home
path('show',client.as_view()),
path('product',product.as_view()),
path('ProductOfClient',ProductOfClient.as_view()),
path('Discount',CalcDiscount.as_view()),
path('ProDiscount',productdiscount.as_view()),
path('clientproduct',Clientproduct.as_view()),
path('discountedvalue',discounted.as_view()),
path('show',Show.as_view()),

]