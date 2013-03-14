# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Locale'
        db.create_table('main_locale', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('co2r', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('shoot', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('our_mission', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('faq', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('register_your_product', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('other_things_you_can_do', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('give_us_feedback', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('feedback_message_prompt', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('learn_more_about_co2r', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('learn_more', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('trees_planted', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('inquire', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_or_organization', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('your_message', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('register_introduction', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('introduction_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('introduction_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('directory_filter_input_prompt', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('can_do_feedback_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('can_do_feedback_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('can_do_spread_word_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('can_do_spread_word_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('can_do_recruit_company_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('can_do_recruit_company_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('can_do_sponsor_co2r_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('can_do_sponsor_co2r_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('artifact_download_report', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('artifact_business_card_contact_lead_in', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('artifact_offset_since', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('artifact_report_section_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('artifact_other_eco_actions', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('artifact_total_vs_offset', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('artifact_co2_sources', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('artifact_co2_per_thing_made', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('about_tab_label_map', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('about_tab_label_video', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('about_topic_1_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('about_topic_1_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('about_topic_2_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('about_topic_2_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('about_topic_3_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('about_topic_3_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('about_community_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('about_community_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('footer_sponsor_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('footer_sponsor_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('footer_sponsor_link', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('footer_taking_root', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('footer_taking_root_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('footer_colofon', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('main', ['Locale'])


    def backwards(self, orm):
        # Deleting model 'Locale'
        db.delete_table('main_locale')


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
        },
        'main.locale': {
            'Meta': {'object_name': 'Locale'},
            'about_community_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'about_community_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'about_tab_label_map': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'about_tab_label_video': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'about_topic_1_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'about_topic_1_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'about_topic_2_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'about_topic_2_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'about_topic_3_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'about_topic_3_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact_business_card_contact_lead_in': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact_co2_per_thing_made': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact_co2_sources': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact_download_report': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact_offset_since': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact_other_eco_actions': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact_report_section_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact_total_vs_offset': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'can_do_feedback_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_feedback_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'can_do_recruit_company_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_recruit_company_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'can_do_sponsor_co2r_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_sponsor_co2r_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'can_do_spread_word_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_spread_word_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'co2r': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'directory_filter_input_prompt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'faq': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'feedback_message_prompt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'footer_colofon': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'footer_sponsor_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'footer_sponsor_link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'footer_sponsor_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'footer_taking_root': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'footer_taking_root_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'give_us_feedback': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inquire': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'introduction_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'introduction_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'learn_more': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'learn_more_about_co2r': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_or_organization': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'other_things_you_can_do': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'our_mission': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'register_introduction': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'register_your_product': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'shoot': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'trees_planted': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'your_message': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']