# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Locale.about_nav_text_description'
        db.delete_column('main_locale', 'about_nav_text_description')

        # Deleting field 'Locale.can_do_nav_text_description'
        db.delete_column('main_locale', 'can_do_nav_text_description')

        # Deleting field 'Locale.other_things_you_can_do'
        db.delete_column('main_locale', 'other_things_you_can_do')

        # Adding field 'Locale.our_mission_nav_text_description'
        db.add_column('main_locale', 'our_mission_nav_text_description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Locale.participate'
        db.add_column('main_locale', 'participate',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Locale.participate_nav_text_description'
        db.add_column('main_locale', 'participate_nav_text_description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Locale.about_nav_text_description'
        db.add_column('main_locale', 'about_nav_text_description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Locale.can_do_nav_text_description'
        db.add_column('main_locale', 'can_do_nav_text_description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Locale.other_things_you_can_do'
        db.add_column('main_locale', 'other_things_you_can_do',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Locale.our_mission_nav_text_description'
        db.delete_column('main_locale', 'our_mission_nav_text_description')

        # Deleting field 'Locale.participate'
        db.delete_column('main_locale', 'participate')

        # Deleting field 'Locale.participate_nav_text_description'
        db.delete_column('main_locale', 'participate_nav_text_description')


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
            'about_carbon_farmers_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'about_carbon_farmers_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'artifact_no_data': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact_offset_since': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact_other_eco_actions': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact_report_section_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'artifact_share_default_message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'artifact_total_vs_offset': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'branding_subtext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_feedback_button_label': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_feedback_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_feedback_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'can_do_recruit_company_button_label': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_recruit_company_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_recruit_company_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'can_do_sponsor_co2r_button_label': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_sponsor_co2r_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_sponsor_co2r_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'can_do_spread_word_button_label': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_spread_word_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_spread_word_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'co2r': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'directory': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'directory_action_body_one': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'directory_action_body_three': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'directory_action_body_two': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'directory_action_title_one': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'directory_action_title_three': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'directory_action_title_two': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'directory_filter_input_prompt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'directory_nav_text_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'faq': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'faq_nav_text_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'feedback_message_prompt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'footer_colofon': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'footer_sponsor_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'footer_sponsor_link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'footer_sponsor_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'footer_taking_root': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'footer_taking_root_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'give_us_feedback': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'heroshot_home': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'heroshot_mission': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inquire': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'introduction_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'introduction_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'learn_more': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'learn_more_about_co2r': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mission_map_help_tip': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_or_organization': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'our_mission': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'our_mission_nav_text_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'participate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'participate_nav_text_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'register_artifact_left_column': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_artifact_right_body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_introduction': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'register_your_product': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'register_your_product_nav_text_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'shoot': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'social_bar_artifact_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'social_bar_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'spread_the_word_button_label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'spread_the_word_default_message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'switch_language': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'trees_planted': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'your_message': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']