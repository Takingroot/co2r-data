# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Organization.partner_description'
        db.add_column('organizations_organization', 'partner_description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Organization.partner_description_fr'
        db.add_column('organizations_organization', 'partner_description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Organization.partner_description'
        db.delete_column('organizations_organization', 'partner_description')

        # Deleting field 'Organization.partner_description_fr'
        db.delete_column('organizations_organization', 'partner_description_fr')


    models = {
        'organizations.contactinfo': {
            'Meta': {'object_name': 'ContactInfo'},
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organizations.Organization']"})
        },
        'organizations.organization': {
            'Meta': {'object_name': 'Organization'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_partner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'logo_mark': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'partner_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'partner_description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'twitter_handle_fr': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'})
        }
    }

    complete_apps = ['organizations']