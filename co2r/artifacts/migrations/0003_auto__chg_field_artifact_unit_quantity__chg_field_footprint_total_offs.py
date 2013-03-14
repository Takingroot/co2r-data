# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Artifact.unit_quantity'
        db.alter_column('artifacts_artifact', 'unit_quantity', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Footprint.total_offset_tons'
        db.alter_column('artifacts_footprint', 'total_offset_tons', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Footprint.total_tons_produced'
        db.alter_column('artifacts_footprint', 'total_tons_produced', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Footprint.co2_per_unit'
        db.alter_column('artifacts_footprint', 'co2_per_unit', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Footprint.ton_offset_per_tree'
        db.alter_column('artifacts_footprint', 'ton_offset_per_tree', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # Changing field 'Artifact.unit_quantity'
        db.alter_column('artifacts_artifact', 'unit_quantity', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2))

        # Changing field 'Footprint.total_offset_tons'
        db.alter_column('artifacts_footprint', 'total_offset_tons', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2))

        # Changing field 'Footprint.total_tons_produced'
        db.alter_column('artifacts_footprint', 'total_tons_produced', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2))

        # Changing field 'Footprint.co2_per_unit'
        db.alter_column('artifacts_footprint', 'co2_per_unit', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2))

        # Changing field 'Footprint.ton_offset_per_tree'
        db.alter_column('artifacts_footprint', 'ton_offset_per_tree', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2))

    models = {
        'artifacts.artifact': {
            'Meta': {'object_name': 'Artifact'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organizations.Organization']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'unit_quantity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'unit_verbose': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'unit_verbose_fr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'artifacts.carbonsource': {
            'Meta': {'object_name': 'CarbonSource'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'artifacts.footprint': {
            'Meta': {'object_name': 'Footprint'},
            'annual_report': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'annual_report_fr': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artifacts.Artifact']"}),
            'carbon_sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['artifacts.CarbonSource']", 'through': "orm['artifacts.FootprintCarbonSource']", 'symmetrical': 'False'}),
            'co2_per_unit': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ton_offset_per_tree': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_offset_tons': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_tons_produced': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_trees_planted': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'artifacts.footprintcarbonsource': {
            'Meta': {'object_name': 'FootprintCarbonSource'},
            'footprint': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artifacts.Footprint']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent': ('django.db.models.fields.IntegerField', [], {}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artifacts.CarbonSource']"})
        },
        'artifacts.image': {
            'Meta': {'object_name': 'Image'},
            'artifact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artifacts.Artifact']"}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'caption_fr': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'organizations.organization': {
            'Meta': {'object_name': 'Organization'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['artifacts']