# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Artifact.twitter_feed_fr'
        db.delete_column('artifacts_artifact', 'twitter_feed_fr')

        # Deleting field 'Artifact.twitter_feed'
        db.delete_column('artifacts_artifact', 'twitter_feed')

        # Adding field 'Artifact.location'
        db.add_column('artifacts_artifact', 'location',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.location_fr'
        db.add_column('artifacts_artifact', 'location_fr',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Artifact.twitter_feed_fr'
        db.add_column('artifacts_artifact', 'twitter_feed_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.twitter_feed'
        db.add_column('artifacts_artifact', 'twitter_feed',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Artifact.location'
        db.delete_column('artifacts_artifact', 'location')

        # Deleting field 'Artifact.location_fr'
        db.delete_column('artifacts_artifact', 'location_fr')


    models = {
        'artifacts.artifact': {
            'Meta': {'object_name': 'Artifact'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'for_total_made': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'for_total_made_fr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'location_fr': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
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
            'total_offset_tons': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_tons_produced': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'artifacts.footprintcarbonsource': {
            'Meta': {'object_name': 'FootprintCarbonSource'},
            'co2_amount_tons': ('django.db.models.fields.FloatField', [], {}),
            'footprint': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artifacts.Footprint']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artifacts.CarbonSource']"})
        },
        'artifacts.image': {
            'Meta': {'object_name': 'Image'},
            'artifact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artifacts.Artifact']"}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'caption_fr': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'artifacts.offsetvariables': {
            'Meta': {'object_name': 'OffsetVariables'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offsets_per_co2_ton': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'trees_per_offset': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        'artifacts.otheraction': {
            'Meta': {'object_name': 'OtherAction'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_fr': ('django.db.models.fields.TextField', [], {}),
            'footprint': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artifacts.Footprint']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artifacts.OtherActionType']", 'null': 'True'})
        },
        'artifacts.otheractiontype': {
            'Meta': {'object_name': 'OtherActionType'},
            'icon_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'organizations.organization': {
            'Meta': {'object_name': 'Organization'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_partner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'logo_mark': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'twitter_handle_fr': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'})
        }
    }

    complete_apps = ['artifacts']