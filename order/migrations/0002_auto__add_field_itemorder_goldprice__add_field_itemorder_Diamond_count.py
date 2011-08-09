# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ItemOrder.goldprice'
        db.add_column('order_itemorder', 'goldprice', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'ItemOrder.Diamond_count'
        db.add_column('order_itemorder', 'Diamond_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'ItemOrder.Diamondprice'
        db.add_column('order_itemorder', 'Diamondprice', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'Payment.cash_value'
        db.add_column('order_payment', 'cash_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'Payment.gold_weight'
        db.add_column('order_payment', 'gold_weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'Payment.gold_price'
        db.add_column('order_payment', 'gold_price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ItemOrder.goldprice'
        db.delete_column('order_itemorder', 'goldprice')

        # Deleting field 'ItemOrder.Diamond_count'
        db.delete_column('order_itemorder', 'Diamond_count')

        # Deleting field 'ItemOrder.Diamondprice'
        db.delete_column('order_itemorder', 'Diamondprice')

        # Deleting field 'Payment.cash_value'
        db.delete_column('order_payment', 'cash_value')

        # Deleting field 'Payment.gold_weight'
        db.delete_column('order_payment', 'gold_weight')

        # Deleting field 'Payment.gold_price'
        db.delete_column('order_payment', 'gold_price')


    models = {
        'order.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'cust_type': ('django.db.models.fields.CharField', [], {'default': "'G'", 'max_length': '1'}),
            'email_id': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'order.goldsmith': {
            'Meta': {'object_name': 'GoldSmith'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'order.goldsmithitemorder': {
            'Meta': {'object_name': 'GoldSmithItemOrder'},
            'goldsmith': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.GoldSmith']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.ItemOrder']"}),
            'order_del_date': ('django.db.models.fields.DateTimeField', [], {}),
            'order_rcvd_date': ('django.db.models.fields.DateTimeField', [], {}),
            'order_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'wage': ('django.db.models.fields.FloatField', [], {})
        },
        'order.item': {
            'Meta': {'object_name': 'Item'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'order.itemorder': {
            'Diamond_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Diamondprice': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Diamondweight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Goldweight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'ItemOrder'},
            'delivery_date': ('django.db.models.fields.DateTimeField', [], {}),
            'delivery_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'goldprice': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'goldsmith': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.GoldSmith']"}),
            'goldsmith_tracker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.GoldSmithItemOrder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Item']"}),
            'making_charge': ('django.db.models.fields.FloatField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Order']"}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {}),
            'totel_item_cost': ('django.db.models.fields.FloatField', [], {}),
            'wastage': ('django.db.models.fields.FloatField', [], {})
        },
        'order.order': {
            'Meta': {'object_name': 'Order'},
            'balance_amount': ('django.db.models.fields.FloatField', [], {}),
            'customer': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['order.Customer']", 'symmetrical': 'False'}),
            'final_cost': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['order.Item']", 'through': "orm['order.ItemOrder']", 'symmetrical': 'False'}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {}),
            'payment_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'total_cost': ('django.db.models.fields.FloatField', [], {})
        },
        'order.payment': {
            'Meta': {'object_name': 'Payment'},
            'cash_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gold_price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gold_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Order']"}),
            'payment_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'})
        }
    }

    complete_apps = ['order']
