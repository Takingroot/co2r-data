# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table('artifacts_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artifact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artifacts.Artifact'])),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('caption_fr', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('artifacts', ['Image'])

        # Deleting field 'Artifact.image'
        db.delete_column('artifacts_artifact', 'image')

        # Deleting field 'Artifact.icon_image'
        db.delete_column('artifacts_artifact', 'icon_image')

        # Adding field 'Artifact.thumbnail'
        db.add_column('artifacts_artifact', 'thumbnail',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table('artifacts_image')

        # Adding field 'Artifact.image'
        db.add_column('artifacts_artifact', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.icon_image'
        db.add_column('artifacts_artifact', 'icon_image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Artifact.thumbnail'
        db.delete_column('artifacts_artifact', 'thumbnail')


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
            'unit_quantity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2', 'blank': 'True'}),
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