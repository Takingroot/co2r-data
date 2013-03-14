# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Faq'
        db.create_table('main_faq', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('question_fr', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('answer_fr', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('main', ['Faq'])

        # Adding model 'Co2Equivalents'
        db.create_table('main_co2equivalents', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phrase', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('phrase_fr', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('co2_amount_unit', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('co2_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=2)),
        ))
        db.send_create_signal('main', ['Co2Equivalents'])

        # Adding model 'DefinedTerms'
        db.create_table('main_definedterms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term_name', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('main', ['DefinedTerms'])


    def backwards(self, orm):
        # Deleting model 'Faq'
        db.delete_table('main_faq')

        # Deleting model 'Co2Equivalents'
        db.delete_table('main_co2equivalents')

        # Deleting model 'DefinedTerms'
        db.delete_table('main_definedterms')


    models = {
        'main.co2equivalents': {
            'Meta': {'object_name': 'Co2Equivalents'},
            'co2_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '2'}),
            'co2_amount_unit': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
            'Meta': {'object_name': 'Faq'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'answer_fr': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'question_fr': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['main']