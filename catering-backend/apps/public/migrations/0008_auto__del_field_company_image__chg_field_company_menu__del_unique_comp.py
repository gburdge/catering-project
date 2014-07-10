# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Company', fields ['menu']
        db.delete_unique(u'public_company', ['menu_id'])

        # Deleting field 'Company.image'
        db.delete_column(u'public_company', 'image')


        # Changing field 'Company.menu'
        db.alter_column(u'public_company', 'menu_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Menu'], null=True))
        # Adding field 'Menu.FoodItem'
        db.add_column(u'public_menu', 'FoodItem',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.FoodItem'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Company.image'
        db.add_column(u'public_company', 'image',
                      self.gf('django.db.models.fields.CharField')(default='image', max_length=500),
                      keep_default=False)


        # Changing field 'Company.menu'
        db.alter_column(u'public_company', 'menu_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['public.Menu'], unique=True, null=True))
        # Adding unique constraint on 'Company', fields ['menu']
        db.create_unique(u'public_company', ['menu_id'])

        # Deleting field 'Menu.FoodItem'
        db.delete_column(u'public_menu', 'FoodItem_id')


    models = {
        u'public.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Menu']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        u'public.food_order': {
            'Meta': {'object_name': 'Food_order'},
            'food_item': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        u'public.fooditem': {
            'Meta': {'object_name': 'FoodItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "'no image'", 'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'price': ('django.db.models.fields.IntegerField', [], {'max_length': '9'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25'})
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