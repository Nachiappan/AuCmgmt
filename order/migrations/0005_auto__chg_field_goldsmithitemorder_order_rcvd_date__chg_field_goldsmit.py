# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'GoldSmithItemOrder.order_rcvd_date'
        db.alter_column('order_goldsmithitemorder', 'order_rcvd_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'GoldSmithItemOrder.order_del_date'
        db.alter_column('order_goldsmithitemorder', 'order_del_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'ItemOrder.order_date'
        db.alter_column('order_itemorder', 'order_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'ItemOrder.delivery_date'
        db.alter_column('order_itemorder', 'delivery_date', self.gf('django.db.models.fields.DateField')())


    def backwards(self, orm):
        
        # Changing field 'GoldSmithItemOrder.order_rcvd_date'
        db.alter_column('order_goldsmithitemorder', 'order_rcvd_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'GoldSmithItemOrder.order_del_date'
        db.alter_column('order_goldsmithitemorder', 'order_del_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'ItemOrder.order_date'
        db.alter_column('order_itemorder', 'order_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'ItemOrder.delivery_date'
        db.alter_column('order_itemorder', 'delivery_date', self.gf('django.db.models.fields.DateTimeField')())


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
            'order_del_date': ('django.db.models.fields.DateField', [], {}),
            'order_rcvd_date': ('django.db.models.fields.DateField', [], {}),
            'order_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'wage': ('django.db.models.fields.FloatField', [], {})
        },
        'order.item': {
            'Meta': {'object_name': 'Item'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'order.itemorder': {
            'Diamond_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Diamondprice': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Diamondweight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Goldweight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'unique_together': "(['item', 'order'],)", 'object_name': 'ItemOrder'},
            'delivery_date': ('django.db.models.fields.DateField', [], {}),
            'delivery_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'goldprice': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'goldsmith': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.GoldSmith']"}),
            'goldsmith_tracker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.GoldSmithItemOrder']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Item']"}),
            'item_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'making_charge': ('django.db.models.fields.FloatField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Order']"}),
            'order_date': ('django.db.models.fields.DateField', [], {}),
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
