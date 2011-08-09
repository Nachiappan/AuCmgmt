# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Order.deliver_visited'
        db.delete_column('order_order', 'deliver_visited')

        # Adding field 'Order.delivery_visited'
        db.add_column('order_order', 'delivery_visited', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Order.deliver_visited'
        db.add_column('order_order', 'deliver_visited', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Deleting field 'Order.delivery_visited'
        db.delete_column('order_order', 'delivery_visited')


    models = {
        'order.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cust_type': ('django.db.models.fields.CharField', [], {'default': "'G'", 'max_length': '1'}),
            'email_id': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'reference': ('django.db.models.fields.TextField', [], {'blank': 'True'})
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
            'Meta': {'object_name': 'ItemOrder'},
            'delivery_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 8, 8, 15, 26, 19, 615546)', 'null': 'True', 'blank': 'True'}),
            'delivery_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1', 'blank': 'True'}),
            'delivery_visited': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diamond_variation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gold_variation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'goldprice': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'goldsmith': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.GoldSmith']", 'null': 'True', 'blank': 'True'}),
            'goldsmith_tracker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.GoldSmithItemOrder']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Item']"}),
            'item_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'item_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'making_charge': ('django.db.models.fields.FloatField', [], {}),
            'new_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Order']", 'blank': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'totel_item_cost': ('django.db.models.fields.FloatField', [], {}),
            'wastage': ('django.db.models.fields.FloatField', [], {})
        },
        'order.order': {
            'Meta': {'object_name': 'Order'},
            'balance_amount': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Customer']", 'null': 'True', 'blank': 'True'}),
            'delivery_visited': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'final_cost': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['order.Item']", 'through': "orm['order.ItemOrder']", 'symmetrical': 'False'}),
            'new_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 8, 8, 15, 26, 19, 613066)'}),
            'paid_amount': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'reduction': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'total_cost': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        'order.payment': {
            'Meta': {'object_name': 'Payment'},
            'cash_value': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'gold_price': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'gold_weight': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Order']"}),
            'others_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'others_value': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'payment_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 8, 8, 15, 26, 19, 614309)'}),
            'payment_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'})
        }
    }

    complete_apps = ['order']
