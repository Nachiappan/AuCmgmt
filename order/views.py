from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from forms import OrderForm,ItemOrderForm,PaymentForm
from django.db import models
from models import *
from datetime import datetime,date
from django.core.urlresolvers import reverse
from django.forms import *
import xlwt
import csv

count = 0
def index(request):
    if request.GET:
        order_list=""
        
        for c in request.GET:       
            print c
        #print request.GET["date"]
        if 'Customer' in request.GET:    
            customer_name =request.GET["cust_name"]
            customers_list = Customer.objects.filter(name=str(customer_name))
            for c in customers_list:
                order_list = Order.objects.filter(customer = c)       
                print order_list
        
        if 'Date' in request.GET:
            date = request.GET["date"]
            if order_list:
                order_list = order_list.filter(order_date =date)
                print order_list
            else:
                order_list = Order.objects.filter(order_date =date)
                print "No customer only Date"
                print order_list
        if 'ItemType' in request.GET:
            print request.GET["item_type"]
            typ=str(request.GET["item_type"])
            print typ
            if typ == "open":
                item_type='O'
                print item_type
            elif typ=="closed":
                item_type='C'
            if order_list:
                order_list = order_list.filter(itemorder__item_type =item_type)
                print order_list
            else:
                order_list = Order.objects.filter(itemorder__item_type =item_type)
                print order_list
        #if 'FinishedOrders' in request.GET:
         #   if order_list:
          #  for order in order_list:
           #     order_list=order_list.filter(
        return HttpResponseRedirect('/')
    else:
      return render(request,"order/selectview_form.html")
      
def create(request):
   
   if request.method == "GET":
        form = OrderForm()
        return render(request,"order/order_form.html", {"form": form})
   else :
        order = Order()
        try:
            customer = Customer.objects.get(name = request.POST["customer_name"],phone_no = request.POST["customer_phone"])
            print customer
            print "old"
        except:
            customer = Customer()
            customer.name = request.POST["customer_name"]
            customer.phone_no = request.POST["customer_phone"]
            customer.place = request.POST["customer_place"]
            customer.address = request.POST["customer_address"]
            customer.email_id = request.POST["customer_email"]
            customer.type = request.POST["customer_type"]
            customer.reference = request.POST["customer_reference"]
            customer.save()    
            print customer
        order.customer =customer
        order_month = request.POST["order_date_month"]
        order_year = request.POST["order_date_year"]
        order_day = request.POST["order_date_day"]
                    
        order.order_date = date(int(order_year),int(order_month),int(order_day))
        order.save()
        return HttpResponseRedirect(reverse('additems', args=[order.id]))   
      
def additems(request,oid):
    if request.method == "GET":
        order = Order.objects.get(id=oid) 
        print order
        form = ItemOrderForm()
        return render(request,"order/itemorder_form.html",{"form":form,"order":order})
    else :
        
        order = Order.objects.get(id=oid) 
        reqd_item = Item.objects.get(name = request.POST["item"])
        iform = ItemOrder()
        iform.item = reqd_item
        iform.item_description = request.POST["item_description"]
        iform.item_type = request.POST["item_type"]
        iform.Goldweight = request.POST["gold_weight"]
        iform.goldprice = request.POST["gold_price"]
        iform.Diamond_count = request.POST["diamond_count"]
        iform.Diamondweight = request.POST["diamond_weight"]
        iform.Diamondprice = request.POST["diamond_price"]
        iform.wastage = request.POST["wastage"]
        iform.making_charge = request.POST["making_charge"]
        order_month = request.POST["order_date_month"]
        order_year = request.POST["order_date_year"]
        order_day = request.POST["order_date_day"]
        delivery_month = request.POST["delivery_date_month"]
        delivery_year = request.POST["delivery_date_year"]
        delivery_day = request.POST["delivery_date_day"]
        iform.order_date = date(int(order_year),int(order_month),int(order_day))
        iform.delivery_date = date(int(delivery_year),int(delivery_month),int(delivery_day))
        iform.totel_item_cost = float(iform.making_charge)+((float(iform.Goldweight) + float(iform.wastage))*float(iform.goldprice) + (float(iform.Diamondweight)*float(iform.Diamondprice)))
        order.total_cost = order.total_cost+iform.totel_item_cost
        order.balance_amount = order.total_cost
        order.final_cost = order.total_cost
        order.new_total = 0
        iform.order = order
        iform.delivery_visited = False
        iform.save()
        order.save()
        print iform.totel_item_cost
        if 'Save and Add another' in request.POST:
            form = ItemOrderForm()       
            return render(request,"order/itemorder_form.html",{"form":form,"order":order})      
        elif 'Place order' in request.POST :
            print order
            return HttpResponseRedirect(reverse('makepayment',args=[order.id]))  

def makepayment(request,oid):            
    if request.method =="GET":      
        order = Order.objects.get(id=oid) 
        form = PaymentForm()
        return render(request,"order/make_payment.html",{"form":form,"order":order})
    else:
        order = Order.objects.get(id=oid)
        amount = float(request.POST["cash_value"])+(float(request.POST["gold_weight"])*float(request.POST["gold_price"]))
        order.balance_amount = order.final_cost-order.paid_amount - amount
        order.paid_amount = order.paid_amount+amount
        if order.paid_amount ==order.final_cost or request.POST["status"]=='D':
            order.payment_status ='D'
        order.save()
        print order.balance_amount
        return HttpResponseRedirect(reverse('view',args=[order.id]))
        
def view(request, oid):
    if request.method =="GET":
        order = Order.objects.get(id = oid)
        item_order = ItemOrder.objects.filter(order=order)
        return render(request,"order/vieworder.html",{"order":order,"item_order":item_order}) 
    else:
        order = Order.objects.get(id = oid)
        return HttpResponseRedirect(reverse('excel_export',args=[order.id]))
     
def excel_export(request,oid):
    order = Order.objects.get(id = oid)
    item_order = ItemOrder.objects.filter(order=order)
    response = HttpResponse(mimetype="text/csv")
    response['Content-Disposition'] = 'attachment; filename=order'+str(order.id)+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Order'+str(order.id),order.customer])
    writer.writerow(['Item','Gold Weight','Gold Price','Diamond Weight','Diamond Price','Total Amount'])
    for item in item_order:
        writer.writerow([item.item,item.Goldweight,item.goldprice,item.Diamondweight,item.Diamondprice,item.totel_item_cost])
    return response
    
def delivery(request,oid):
    if request.method =="GET":    
        order = Order.objects.get(id=oid)
        item_order = ItemOrder.objects.filter(order=order)
        return render(request,"order/delivery.html",{"order":order,"item_order":item_order}) 
    else:
        order = Order.objects.get(id=oid)
        item_order = ItemOrder.objects.filter(order=order)
        #print request.POST["gold_variation"]
      
        for i in item_order:
            print i.delivery_visited
            print "delvisi"
            if i.delivery_visited==False:
               i.new_total = i.totel_item_cost+ (float(request.POST["gold_variation"])*i.goldprice)+(float(request.POST["diamond_variation"])*i.Diamondprice)
               print "old item total"
               print i.totel_item_cost
               print "new item total"
               print i.new_total
               order.new_total = float(order.new_total)+float(i.new_total)
               i.delivery_visited == True
               i.save()
               print i.delivery_visited
        print order.reduced               
        if order.reduced == False:
            order.reduction = float(request.POST["reduction"])  
            order.new_total = order.new_total-order.reduction
            order.reduced == True
        print order.reduced
        order.save()
        print order.reduced
        order.balance_amount = order.new_total-order.paid_amount
        order.final_cost = order.total_cost
        gt = order.new_total+order.reduction
        print "order new total"
        print order.new_total
        order.save()
        return render(request,"order/delivery_final.html",{"order":order,"item_order":item_order,"gt":gt})
 #       else:
  #          print "Dont press Back or Refresh button"
   #         return render(request,"order/delivery.html",{"order":order,"item_order":item_order}) 

