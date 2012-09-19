# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CarbonSource'
        db.create_table('artifacts_carbonsource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('artifacts', ['CarbonSource'])

        # Adding model 'Artifact'
        db.create_table('artifacts_artifact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('icon_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('unit_quantity', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2, blank=True)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('unit_verbose', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organizations.Organization'])),
        ))
        db.send_create_signal('artifacts', ['Artifact'])

        # Adding model 'Footprint'
        db.create_table('artifacts_footprint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artifact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artifacts.Artifact'])),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('co2_per_unit', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2, blank=True)),
            ('total_tons_produced', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2, blank=True)),
            ('total_offset_tons', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2, blank=True)),
            ('total_trees_planted', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ton_offset_per_tree', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2, blank=True)),
            ('annual_report', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('artifacts', ['Footprint'])

        # Adding model 'FootprintCarbonSource'
        db.create_table('artifacts_footprintcarbonsource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('footprint', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artifacts.Footprint'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artifacts.CarbonSource'])),
            ('percent', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('artifacts', ['FootprintCarbonSource'])


    def backwards(self, orm):
        # Deleting model 'CarbonSource'
        db.delete_table('artifacts_carbonsource')

        # Deleting model 'Artifact'
        db.delete_table('artifacts_artifact')

        # Deleting model 'Footprint'
        db.delete_table('artifacts_footprint')

        # Deleting model 'FootprintCarbonSource'
        db.delete_table('artifacts_footprintcarbonsource')


    models = {
        'artifacts.artifact': {
            'Meta': {'object_name': 'Artifact'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'icon_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organizations.Organization']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'unit_quantity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2', 'blank': 'True'}),
            'unit_verbose': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'artifacts.carbonsource': {
            'Meta': {'object_name': 'CarbonSource'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'artifacts.footprint': {
            'Meta': {'object_name': 'Footprint'},
            'annual_report': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artifacts.Artifact']"}),
            'carbon_sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['artifacts.CarbonSource']", 'through': "orm['artifacts.FootprintCarbonSource']", 'symmetrical': 'False'}),
            'co2_per_unit': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ton_offset_per_tree': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2', 'blank': 'True'}),
            'total_offset_tons': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2', 'blank': 'True'}),
            'total_tons_produced': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2', 'blank': 'True'}),
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
        'organizations.organization': {
            'Meta': {'object_name': 'Organization'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['artifacts']