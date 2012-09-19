# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Organization.internal_name'
        db.delete_column('organizations_organization', 'internal_name')

        # Adding field 'Organization.slug'
        db.add_column('organizations_organization', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='asdf', max_length=100),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Organization.internal_name'
        raise RuntimeError("Cannot reverse this migration. 'Organization.internal_name' and its values cannot be restored.")
        # Deleting field 'Organization.slug'
        db.delete_column('organizations_organization', 'slug')


    models = {
        'organizations.organization': {
            'Meta': {'object_name': 'Organization'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['organizations']