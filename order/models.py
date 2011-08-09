from django.db import models
from datetime import datetime,date

CUSTOMER_TYPE_CHOICES = (
   ('G', 'General Customer'),
   ('T', 'Trader'),
)

ITEM_TYPE_CHOICES = (
   ('O', 'Open'),
   ('C', 'Closed'),
)

PAYMENT_TYPE_CHOICES = (
   ('G', 'Gold'),
   ('C', 'Cash'),
)

STATUS_CHOICES = (
   ('P', 'Pending'),
   ('D', 'Delivered'),
)

class Customer(models.Model):
  name = models.CharField(max_length=30)
  phone_no = models.CharField(max_length=15,blank=True)
  email_id = models.EmailField(max_length=50, blank=True)
  place = models.CharField(max_length=50,blank=True)
  address = models.TextField(blank=True)
  reference = models.TextField(blank = True)
  cust_type = models.CharField(max_length = 1, choices = CUSTOMER_TYPE_CHOICES, default='G')
  def __unicode__(self):
       return self.name

class Item(models.Model):
  name = models.CharField(max_length = 50)
  desc = models.TextField()
  picture = models.ImageField(upload_to = '/photos/', blank = True, null = True)
  def __unicode__(self):
       return self.name
  def __str__(self):
       return self.name
       
class Order(models.Model):
  item = models.ManyToManyField(Item, through = 'ItemOrder')
  customer = models.ForeignKey(Customer,blank =True,null =True)
  total_cost = models.FloatField(default = 0)
  final_cost = models.FloatField(default = 0,blank =True)
  reduction = models.FloatField(default = 0,blank =True)
  balance_amount = models.FloatField(default = 0,blank=True)
  payment_status = models.CharField(max_length = 1, choices = STATUS_CHOICES, default = 'P')
  order_date = models.DateField('OrderDate', default=datetime.now())
  paid_amount = models.FloatField(default = 0,blank =True)
  new_total =models.FloatField(null = True, blank = True)
  reduced = models.BooleanField(default=False,blank=True,editable=False)
  def __unicode__(self):
       return str(self.id)+str(self.customer)+str(self.total_cost)
        
class Payment(models.Model):
  order = models.ForeignKey(Order)
  payment_type = models.CharField(max_length = 1, choices = PAYMENT_TYPE_CHOICES, default='C')
  cash_value = models.FloatField(null = True, blank = True,default=0)
  gold_weight = models.FloatField(null = True, blank = True,default=0)
  gold_price = models.FloatField(null = True, blank = True,default=0)
  others_desc = models.TextField(null =True, blank =True)
  others_value = models.FloatField(null =True, blank=True,default =0)
  status = models.CharField(max_length = 1, choices = STATUS_CHOICES, default = 'P')
  payment_date = models.DateField('PaymentDate',default = datetime.now())
  def __unicode__(self):
       return "Cash"+str(cash_value)+" | Gold "+str(gold_weight)+" grams"
       
class ItemOrder(models.Model):
  item = models.ForeignKey(Item)
  item_description = models.TextField(null=True, blank=True)
  item_type = models.CharField(max_length = 1, choices = ITEM_TYPE_CHOICES, default='C')
  order = models.ForeignKey(Order,blank = True)
  goldsmith = models.ForeignKey('GoldSmith',blank = True,null = True)
  Goldweight = models.FloatField(null = True, blank = True)
  goldprice = models.FloatField(null = True, blank = True)
  Diamond_count = models.IntegerField(null = True, blank = True)
  Diamondweight = models.FloatField(null = True, blank = True)
  Diamondprice = models.FloatField(null = True, blank = True)
  wastage = models.FloatField()
  making_charge = models.FloatField()
  totel_item_cost = models.FloatField()
  goldsmith_tracker = models.ForeignKey('GoldSmithItemOrder', blank = True,null =True)
  order_date = models.DateField('OrderDate',blank = True)
  delivery_date = models.DateField('DeliveryDate',default = datetime.now(),blank =True, null = True)
  delivery_status = models.CharField(max_length = 1, choices = STATUS_CHOICES, default = 'P',blank = True)
  gold_variation = models.FloatField(null = True, blank = True)
  diamond_variation =models.FloatField(null = True, blank = True)
  new_total =models.FloatField(null = True, blank = True)
  delivery_visited = models.BooleanField(default=False,blank=True)
  def __unicode__(self):
       return str(self.item) + str(self.order)
          
class GoldSmith(models.Model):
  name = models.CharField(max_length=30)
  phone_no = models.CharField(max_length=15)
  place = models.CharField(max_length=50)
  address = models.TextField()
  def __unicode__(self):
       return self.name
       
class GoldSmithItemOrder(models.Model):
  item = models.ForeignKey(ItemOrder)
  goldsmith = models.ForeignKey('GoldSmith')
  wage = models.FloatField()
  order_rcvd_date = models.DateField('OrderPlacementDate')
  order_del_date = models.DateField('OrderDeliveryDate') 
  order_status = models.CharField(max_length = 1, choices = STATUS_CHOICES, default = 'P')
  payment_status = models.CharField(max_length = 1, choices = STATUS_CHOICES, default = 'P')
  def __unicode__(self):
       return str(self.id) + "|"+str(self.item)+"|"+  str(self.goldsmith)
