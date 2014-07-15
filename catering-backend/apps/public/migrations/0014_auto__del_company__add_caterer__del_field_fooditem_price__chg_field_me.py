# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'public_company')

        # Adding model 'Caterer'
        db.create_table(u'public_caterer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Menu'], null=True, blank=True)),
        ))
        db.send_create_signal(u'public', ['Caterer'])

        # Deleting field 'FoodItem.price'
        db.delete_column(u'public_fooditem', 'price')


        # Changing field 'Menu.FoodItem'
        db.alter_column(u'public_menu', 'FoodItem_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.FoodItem'], null=True))

    def backwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'public_company', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Menu'])),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=60)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'public', ['Company'])

        # Deleting model 'Caterer'
        db.delete_table(u'public_caterer')


        # User chose to not deal with backwards NULL issues for 'FoodItem.price'
        raise RuntimeError("Cannot reverse this migration. 'FoodItem.price' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'FoodItem.price'
        db.add_column(u'public_fooditem', 'price',
                      self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Menu.FoodItem'
        raise RuntimeError("Cannot reverse this migration. 'Menu.FoodItem' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Menu.FoodItem'
        db.alter_column(u'public_menu', 'FoodItem_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.FoodItem']))

    models = {
        u'public.caterer': {
            'Meta': {'object_name': 'Caterer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Menu']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'public.fooditem': {
            'Meta': {'object_name': 'FoodItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "'no image'", 'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'public.foodorder': {
            'FoodItem': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'Meta': {'object_name': 'FoodOrder'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        u'public.menu': {
            'FoodItem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.FoodItem']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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