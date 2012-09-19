# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrganizationTranslation'
        db.create_table('organizations_organization_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['organizations.Organization'])),
        ))
        db.send_create_signal('organizations', ['OrganizationTranslation'])

        # Adding unique constraint on 'OrganizationTranslation', fields ['language_code', 'master']
        db.create_unique('organizations_organization_translation', ['language_code', 'master_id'])

        # Deleting field 'Organization.name'
        db.delete_column('organizations_organization', 'name')


    def backwards(self, orm):
        # Removing unique constraint on 'OrganizationTranslation', fields ['language_code', 'master']
        db.delete_unique('organizations_organization_translation', ['language_code', 'master_id'])

        # Deleting model 'OrganizationTranslation'
        db.delete_table('organizations_organization_translation')


        # User chose to not deal with backwards NULL issues for 'Organization.name'
        raise RuntimeError("Cannot reverse this migration. 'Organization.name' and its values cannot be restored.")

    models = {
        'organizations.contactinfo': {
            'Meta': {'object_name': 'ContactInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organizations.Organization']"})
        },
        'organizations.organization': {
            'Meta': {'object_name': 'Organization'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'organizations.organizationtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'OrganizationTranslation', 'db_table': "'organizations_organization_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['organizations.Organization']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['organizations']