from django.contrib import admin
from co2r.main.models import Co2Equivalents, DefinedTerms, Faq, Locale


class LocaleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('language',)}),
        ('Header', {
            'classes': ('wide',),
            'fields': ('co2r', 'branding_subtext',)
            }),
        ('Images', {
            'classes': ('wide',),
            'fields': ('heroshot_home', 'heroshot_mission')
            }),
        ('Directory', {
            'classes': ('wide',),
            'fields': ('directory', 'introduction_title', 'introduction_text',
                'learn_more', 'directory_action_title_one', 'directory_action_body_one',
                'directory_action_title_two', 'directory_action_body_two',
                'directory_action_title_three', 'directory_action_body_three',
                'directory_filter_input_prompt')
            }),
        ('Artifacts', {
            'classes': ('wide',),
            'fields': ('location', 'artifact_offset_since', 'learn_more_about_co2r',
                'artifact_business_card_contact_lead_in', 'artifact_co2_per_thing_made',
                'artifact_total_vs_offset', 'artifact_total_trees_planted', 'trees_planted', 'artifact_co2_sources',
                'artifact_other_eco_actions', 'artifact_report_section_title',
                'artifact_download_report', 'artifact_share_default_message',
                'artifact_no_data', 'artifact_organization_label')
            }),
        ('About', {
            'classes': ('wide',),
            'fields': ('our_mission', 'our_mission_intro', 'mission_map_help_tip', 'about_community_title', 'about_community_text',
                'about_carbon_farmers_title', 'about_carbon_farmers_text',
                'about_tab_label_map', 'about_tab_label_video', 'about_topic_1_title',
                'about_topic_1_text', 'about_topic_2_title', 'about_topic_2_text', 'about_topic_3_title',
                'about_topic_3_text')
            }),
        ('FAQ', {
            'classes': ('wide',),
            'fields': ('faq',)
            }),
        ('Register', {
            'classes': ('wide'),
            'fields': ('register_your_product', 'register_introduction',
                'your_message', 'name_or_organization', 'email', 'phone',
                'inquire', 'register_artifact_left_column', 'register_artifact_right_body')
            }),
        ('Participate', {
            'classes': ('wide'),
            'fields': ('participate', 'can_do_feedback_title', 'can_do_feedback_description',
                'can_do_feedback_button_label', 'can_do_spread_word_title', 'can_do_spread_word_description',
                'can_do_spread_word_button_label', 'can_do_recruit_company_title', 'can_do_recruit_company_description', 'can_do_recruit_company_button_label',
                'can_do_sponsor_co2r_title', 'can_do_sponsor_co2r_description', 'can_do_sponsor_co2r_button_label')
            }),
        ('Feedback', {
            'classes': ('wide'),
            'fields': ('give_us_feedback', 'feedback_message_prompt', 'shoot')
            }),
        ('Share tool', {
            'classes': ('wide'),
            'fields': ('spread_the_word_default_message', 'spread_the_word_button_label')
            }),
        ('Footer', {
            'classes': ('wide'),
            'fields': ('social_bar_text', 'social_bar_artifact_text', 'footer_partners_title', 'footer_colofon')
            }),
        )

admin.site.register(Co2Equivalents, admin.ModelAdmin)
admin.site.register(DefinedTerms, admin.ModelAdmin)
admin.site.register(Faq, admin.ModelAdmin)
admin.site.register(Locale, LocaleAdmin)
