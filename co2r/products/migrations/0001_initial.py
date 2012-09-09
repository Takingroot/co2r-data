# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CarbonSource'
        db.create_table('products_carbonsource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('products', ['CarbonSource'])

        # Adding model 'Product'
        db.create_table('products_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('internal_name', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('unit_quantity', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('unit_verbose', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
        ))
        db.send_create_signal('products', ['Product'])

        # Adding model 'Footprint'
        db.create_table('products_footprint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('co2_per_unit', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2)),
            ('total_tons_produced', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2)),
            ('total_offset_tons', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2)),
            ('total_trees_planted', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('ton_offset_per_tree', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2)),
            ('annual_report', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('products', ['Footprint'])

        # Adding model 'FootprintCarbonSource'
        db.create_table('products_footprintcarbonsource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('footprint', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Footprint'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.CarbonSource'])),
            ('percent', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('products', ['FootprintCarbonSource'])


    def backwards(self, orm):
        # Deleting model 'CarbonSource'
        db.delete_table('products_carbonsource')

        # Deleting model 'Product'
        db.delete_table('products_product')

        # Deleting model 'Footprint'
        db.delete_table('products_footprint')

        # Deleting model 'FootprintCarbonSource'
        db.delete_table('products_footprintcarbonsource')


    models = {
        'products.carbonsource': {
            'Meta': {'object_name': 'CarbonSource'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'products.footprint': {
            'Meta': {'object_name': 'Footprint'},
            'annual_report': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'carbon_sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.CarbonSource']", 'through': "orm['products.FootprintCarbonSource']", 'symmetrical': 'False'}),
            'co2_per_unit': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'ton_offset_per_tree': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'total_offset_tons': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'total_tons_produced': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'total_trees_planted': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'products.footprintcarbonsource': {
            'Meta': {'object_name': 'FootprintCarbonSource'},
            'footprint': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Footprint']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent': ('django.db.models.fields.IntegerField', [], {}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.CarbonSource']"})
        },
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'internal_name': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'unit_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'unit_verbose': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['products']