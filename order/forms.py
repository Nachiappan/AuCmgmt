from django import forms
from django.forms import ModelForm
from datetime import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple
from models import *

ITEM_TYPE_CHOICES = (
   ('O', 'Open'),
   ('C', 'Closed'),
)

CUSTOMER_TYPE_CHOICES = (
   ('G', 'General Customer'),
   ('T', 'Trader'),
)

CHECKBOX_CHOICES = (
    ('C','Customer'),
    ('D','Date'),
    ('T','ItemType')
)

class ItemOrderForm(forms.Form):
   item = forms.CharField()
   item_description = forms.CharField(max_length = 300)
   item_type = forms.ChoiceField(widget =forms.RadioSelect,choices =ITEM_TYPE_CHOICES ) 
   gold_weight = forms.FloatField()
   gold_price = forms.FloatField()
   diamond_count = forms.IntegerField()
   diamond_weight = forms.FloatField()
   diamond_price = forms.FloatField()
   wastage = forms.FloatField()
   making_charge = forms.FloatField()
   order_date = forms.DateField(widget=SelectDateWidget())
   delivery_date = forms.DateField(widget=SelectDateWidget())


class OrderForm(forms.Form):
   customer_name = forms.CharField(max_length = 30)
   customer_place = forms.CharField()
   customer_phone = forms.CharField()
   customer_address = forms.CharField(max_length = 300)
   customer_reference = forms.CharField(max_length = 300)
   customer_email = forms.EmailField()
   customer_type = forms.ChoiceField(choices = CUSTOMER_TYPE_CHOICES)
   order_date = forms.DateField(widget=SelectDateWidget())
   
class PaymentForm(ModelForm):
   class Meta:
       model=Payment
       exclude = ('order',)  

#class SelectViewForm(forms.Form):
 #   view_type = forms.MultipleChoiceField(required=False,widget=CheckboxSelectMultiple, choices=CHECKBOX_CHOICES) 
    
   


