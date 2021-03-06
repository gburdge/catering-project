# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Food_order'
        db.delete_table(u'public_food_order')

        # Adding model 'FoodOrder'
        db.create_table(u'public_foodorder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('food_item', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
        ))
        db.send_create_signal(u'public', ['FoodOrder'])

        # Deleting field 'Company.image'
        db.delete_column(u'public_company', 'image')


    def backwards(self, orm):
        # Adding model 'Food_order'
        db.create_table(u'public_food_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('food_item', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'public', ['Food_order'])

        # Deleting model 'FoodOrder'
        db.delete_table(u'public_foodorder')

        # Adding field 'Company.image'
        db.add_column(u'public_company', 'image',
                      self.gf('django.db.models.fields.CharField')(default='image', max_length=500),
                      keep_default=False)


    models = {
        u'public.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Menu']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        u'public.fooditem': {
            'Meta': {'object_name': 'FoodItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "'no image'", 'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'price': ('django.db.models.fields.IntegerField', [], {'max_length': '9'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'public.foodorder': {
            'Meta': {'object_name': 'FoodOrder'},
            'food_item': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        u'public.menu': {
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