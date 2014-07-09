# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FoodItems'
        db.create_table(u'public_fooditems', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.IntegerField')(max_length=9)),
            ('image', self.gf('django.db.models.fields.CharField')(default='no image', max_length=500)),
        ))
        db.send_create_signal(u'public', ['FoodItems'])

        # Adding model 'Company'
        db.create_table(u'public_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=9)),
            ('cuisine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Cuisine'])),
            ('menu', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['public.Menu'], unique=True, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.CharField')(default='no image', max_length=500)),
        ))
        db.send_create_signal(u'public', ['Company'])

        # Adding model 'Menu'
        db.create_table(u'public_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Menu'])

        # Adding model 'Cuisine'
        db.create_table(u'public_cuisine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Cuisine'])


    def backwards(self, orm):
        # Deleting model 'FoodItems'
        db.delete_table(u'public_fooditems')

        # Deleting model 'Company'
        db.delete_table(u'public_company')

        # Deleting model 'Menu'
        db.delete_table(u'public_menu')

        # Deleting model 'Cuisine'
        db.delete_table(u'public_cuisine')


    models = {
        u'public.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'cuisine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Cuisine']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "'no image'", 'max_length': '500'}),
            'menu': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['public.Menu']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '9'})
        },
        u'public.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.fooditems': {
            'Meta': {'object_name': 'FoodItems'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "'no image'", 'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.IntegerField', [], {'max_length': '9'}),
            'type': ('django.db.models.fields.TextField', [], {})
        },
        u'public.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['public']