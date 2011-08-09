# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Customer'
        db.create_table('order_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('email_id', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('cust_type', self.gf('django.db.models.fields.CharField')(default='G', max_length=1)),
        ))
        db.send_create_signal('order', ['Customer'])

        # Adding model 'Item'
        db.create_table('order_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('item_type', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('order', ['Item'])

        # Adding model 'Order'
        db.create_table('order_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total_cost', self.gf('django.db.models.fields.FloatField')()),
            ('final_cost', self.gf('django.db.models.fields.FloatField')()),
            ('balance_amount', self.gf('django.db.models.fields.FloatField')()),
            ('payment_status', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
            ('order_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('order', ['Order'])

        # Adding M2M table for field customer on 'Order'
        db.create_table('order_order_customer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('order', models.ForeignKey(orm['order.order'], null=False)),
            ('customer', models.ForeignKey(orm['order.customer'], null=False))
        ))
        db.create_unique('order_order_customer', ['order_id', 'customer_id'])

        # Adding model 'Payment'
        db.create_table('order_payment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Order'])),
            ('payment_type', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('status', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
        ))
        db.send_create_signal('order', ['Payment'])

        # Adding model 'ItemOrder'
        db.create_table('order_itemorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Item'])),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Order'])),
            ('goldsmith', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.GoldSmith'])),
            ('Goldweight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Diamondweight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('wastage', self.gf('django.db.models.fields.FloatField')()),
            ('making_charge', self.gf('django.db.models.fields.FloatField')()),
            ('totel_item_cost', self.gf('django.db.models.fields.FloatField')()),
            ('goldsmith_tracker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.GoldSmithItemOrder'])),
            ('order_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('delivery_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('delivery_status', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
        ))
        db.send_create_signal('order', ['ItemOrder'])

        # Adding model 'GoldSmith'
        db.create_table('order_goldsmith', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('order', ['GoldSmith'])

        # Adding model 'GoldSmithItemOrder'
        db.create_table('order_goldsmithitemorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.ItemOrder'])),
            ('goldsmith', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.GoldSmith'])),
            ('wage', self.gf('django.db.models.fields.FloatField')()),
            ('order_rcvd_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('order_del_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('order_status', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
            ('payment_status', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
        ))
        db.send_create_signal('order', ['GoldSmithItemOrder'])


    def backwards(self, orm):
        
        # Deleting model 'Customer'
        db.delete_table('order_customer')

        # Deleting model 'Item'
        db.delete_table('order_item')

        # Deleting model 'Order'
        db.delete_table('order_order')

        # Removing M2M table for field customer on 'Order'
        db.delete_table('order_order_customer')

        # Deleting model 'Payment'
        db.delete_table('order_payment')

        # Deleting model 'ItemOrder'
        db.delete_table('order_itemorder')

        # Deleting model 'GoldSmith'
        db.delete_table('order_goldsmith')

        # Deleting model 'GoldSmithItemOrder'
        db.delete_table('order_goldsmithitemorder')


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
            'Diamondweight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Goldweight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'ItemOrder'},
            'delivery_date': ('django.db.models.fields.DateTimeField', [], {}),
            'delivery_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Order']"}),
            'payment_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'})
        }
    }

    complete_apps = ['order']
