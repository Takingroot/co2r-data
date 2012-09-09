# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.organization'
        db.add_column('products_product', 'organization',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['organizations.Organization']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.organization'
        db.delete_column('products_product', 'organization_id')


    models = {
        'organizations.organization': {
            'Meta': {'object_name': 'Organization'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'internal_name': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organizations.Organization']"}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'unit_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'unit_verbose': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['products']