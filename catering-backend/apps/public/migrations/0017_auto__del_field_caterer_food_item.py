# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Caterer.food_item'
        db.delete_column(u'public_caterer', 'food_item_id')

        # Adding M2M table for field food_item on 'Caterer'
        m2m_table_name = db.shorten_name(u'public_caterer_food_item')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('caterer', models.ForeignKey(orm[u'public.caterer'], null=False)),
            ('fooditem', models.ForeignKey(orm[u'public.fooditem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['caterer_id', 'fooditem_id'])


    def backwards(self, orm):
        # Adding field 'Caterer.food_item'
        db.add_column(u'public_caterer', 'food_item',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.FoodItem'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field food_item on 'Caterer'
        db.delete_table(db.shorten_name(u'public_caterer_food_item'))


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