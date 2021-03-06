# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Co2Equivalents.active'
        db.add_column('main_co2equivalents', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Faq.order'
        db.add_column('main_faq', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


        # Changing field 'Faq.answer_fr'
        db.alter_column('main_faq', 'answer_fr', self.gf('django.db.models.fields.TextField')(max_length=500))

        # Changing field 'Faq.answer'
        db.alter_column('main_faq', 'answer', self.gf('django.db.models.fields.TextField')(max_length=500))

    def backwards(self, orm):
        # Deleting field 'Co2Equivalents.active'
        db.delete_column('main_co2equivalents', 'active')

        # Deleting field 'Faq.order'
        db.delete_column('main_faq', 'order')


        # Changing field 'Faq.answer_fr'
        db.alter_column('main_faq', 'answer_fr', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Faq.answer'
        db.alter_column('main_faq', 'answer', self.gf('django.db.models.fields.CharField')(max_length=500))

    models = {
        'main.co2equivalents': {
            'Meta': {'object_name': 'Co2Equivalents'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'co2_amount': ('django.db.models.fields.FloatField', [], {}),
            'co2_amount_unit': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'co2_amount_unit_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phrase': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'phrase_fr': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'main.definedterms': {
            'Meta': {'object_name': 'DefinedTerms'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'term_name': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'main.faq': {
            'Meta': {'ordering': "['order']", 'object_name': 'Faq'},
            'answer': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'answer_fr': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'question_fr': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['main']