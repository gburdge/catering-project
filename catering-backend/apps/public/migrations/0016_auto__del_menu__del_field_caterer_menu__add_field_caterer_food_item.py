# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Menu'
        db.delete_table(u'public_menu')

        # Deleting field 'Caterer.menu'
        db.delete_column(u'public_caterer', 'menu_id')

        # Adding field 'Caterer.food_item'
        db.add_column(u'public_caterer', 'food_item',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.FoodItem'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Menu'
        db.create_table(u'public_menu', (
            ('FoodItem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.FoodItem'], null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Menu'])

        # Adding field 'Caterer.menu'
        db.add_column(u'public_caterer', 'menu',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Menu'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Caterer.food_item'
        db.delete_column(u'public_caterer', 'food_item_id')


    models = {
        u'public.caterer': {
            'Meta': {'object_name': 'Caterer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'food_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.FoodItem']", 'null': 'True', 'blank': 'True'}),
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
            'FoodItem': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'Meta': {'object_name': 'FoodOrder'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        u'public.order': {
            'Meta': {'object_name': 'Order'},
            'delivery_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'delivery_time': ('django.db.models.fields.TimeField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.TextField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['public']