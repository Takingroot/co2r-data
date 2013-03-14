# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organization'
        db.create_table('organizations_organization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('organizations', ['Organization'])

        # Adding model 'ContactInfo'
        db.create_table('organizations_contactinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organizations.Organization'])),
        ))
        db.send_create_signal('organizations', ['ContactInfo'])


    def backwards(self, orm):
        # Deleting model 'Organization'
        db.delete_table('organizations_organization')

        # Deleting model 'ContactInfo'
        db.delete_table('organizations_contactinfo')


    models = {
        'organizations.contactinfo': {
            'Meta': {'object_name': 'ContactInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organizations.Organization']"})
        },
        'organizations.organization': {
            'Meta': {'object_name': 'Organization'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['organizations']