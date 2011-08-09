# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Order.customer'
        db.add_column('order_order', 'customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Customer'], null=True, blank=True), keep_default=False)

        # Removing M2M table for field customer on 'Order'
        db.delete_table('order_order_customer')

        # Changing field 'Order.order_date'
        db.alter_column('order_order', 'order_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'ItemOrder.goldsmith_tracker'
        db.alter_column('order_itemorder', 'goldsmith_tracker_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.GoldSmithItemOrder'], null=True))

        # Changing field 'ItemOrder.delivery_date'
        db.alter_column('order_itemorder', 'delivery_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'ItemOrder.goldsmith'
        db.alter_column('order_itemorder', 'goldsmith_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.GoldSmith'], null=True))


    def backwards(self, orm):
        
        # Deleting field 'Order.customer'
        db.delete_column('order_order', 'customer_id')

        # Adding M2M table for field customer on 'Order'
        db.create_table('order_order_customer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('order', models.ForeignKey(orm['order.order'], null=False)),
            ('customer', models.ForeignKey(orm['order.customer'], null=False))
        ))
        db.create_unique('order_order_customer', ['order_id', 'customer_id'])

        # Changing field 'Order.order_date'
        db.alter_column('order_order', 'order_date', self.gf('django.db.models.fields.DateTimeField')())

        # User chose to not deal with backwards NULL issues for 'ItemOrder.goldsmith_tracker'
        raise RuntimeError("Cannot reverse this migration. 'ItemOrder.goldsmith_tracker' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'ItemOrder.delivery_date'
        raise RuntimeError("Cannot reverse this migration. 'ItemOrder.delivery_date' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'ItemOrder.goldsmith'
        raise RuntimeError("Cannot reverse this migration. 'ItemOrder.goldsmith' and its values cannot be restored.")


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
            'delivery_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 8, 3, 11, 16, 13, 764068)', 'null': 'True', 'blank': 'True'}),
            'delivery_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1', 'blank': 'True'}),
            'goldprice': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'goldsmith': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.GoldSmith']", 'null': 'True', 'blank': 'True'}),
            'goldsmith_tracker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.GoldSmithItemOrder']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Item']"}),
            'item_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'making_charge': ('django.db.models.fields.FloatField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Order']", 'blank': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'totel_item_cost': ('django.db.models.fields.FloatField', [], {}),
            'wastage': ('django.db.models.fields.FloatField', [], {})
        },
        'order.order': {
            'Meta': {'object_name': 'Order'},
            'balance_amount': ('django.db.models.fields.FloatField', [], {}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Customer']", 'null': 'True', 'blank': 'True'}),
            'final_cost': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['order.Item']", 'through': "orm['order.ItemOrder']", 'symmetrical': 'False'}),
            'order_date': ('django.db.models.fields.DateField', [], {}),
            'payment_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'total_cost': ('django.db.models.fields.FloatField', [], {'default': '0'})
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
