# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'FoodOrder.FoodItem'
        db.delete_column(u'public_foodorder', 'FoodItem')

        # Adding field 'FoodOrder.order'
        db.add_column(u'public_foodorder', 'order',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['public.Order']),
                      keep_default=False)

        # Adding field 'FoodOrder.food_item'
        db.add_column(u'public_foodorder', 'food_item',
                      self.gf('django.db.models.fields.related.OneToOneField')(default='', to=orm['public.FoodItem'], unique=True),
                      keep_default=False)

        # Deleting field 'Order.order'
        db.delete_column(u'public_order', 'order')

        # Adding field 'Order.delivery_location'
        db.add_column(u'public_order', 'delivery_location',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'FoodOrder.FoodItem'
        raise RuntimeError("Cannot reverse this migration. 'FoodOrder.FoodItem' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'FoodOrder.FoodItem'
        db.add_column(u'public_foodorder', 'FoodItem',
                      self.gf('django.db.models.fields.CharField')(max_length=25),
                      keep_default=False)

        # Deleting field 'FoodOrder.order'
        db.delete_column(u'public_foodorder', 'order_id')

        # Deleting field 'FoodOrder.food_item'
        db.delete_column(u'public_foodorder', 'food_item_id')


        # User chose to not deal with backwards NULL issues for 'Order.order'
        raise RuntimeError("Cannot reverse this migration. 'Order.order' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Order.order'
        db.add_column(u'public_order', 'order',
                      self.gf('django.db.models.fields.TextField')(max_length=100),
                      keep_default=False)

        # Deleting field 'Order.delivery_location'
        db.delete_column(u'public_order', 'delivery_location')


    models = {
        u'public.caterer': {
            'Meta': {'object_name': 'Caterer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'food_item': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['public.FoodItem']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'public.fooditem': {
            'Meta': {'object_name': 'FoodItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "'no image'", 'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'public.foodorder': {
            'Meta': {'object_name': 'FoodOrder'},
            'food_item': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['public.FoodItem']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Order']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        u'public.order': {
            'Meta': {'object_name': 'Order'},
            'delivery_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'delivery_location': ('django.db.models.fields.TextField', [], {}),
            'delivery_time': ('django.db.models.fields.TimeField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['public']