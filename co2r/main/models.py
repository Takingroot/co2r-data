from django.db import models

LANGUAGE_CHOICES = (('en', 'English'), ('fr', 'French'))


class TranslatedModelMixin(object):
    """
    Given a translated model, overwrites the original language with
    the one requested
    """

    def set_language(self, language_code):
        if language_code == 'en':
            return

        self.language_code = language_code

        for field in self.translated_fields:
            translated_field_key = field + '_' + language_code
            translated_field = getattr(self, translated_field_key)
            setattr(self, field, translated_field)

        return


class Faq(models.Model, TranslatedModelMixin):
    slug = models.SlugField(max_length=100, unique=True)
    question = models.CharField(max_length=500, help_text='Supports Html')
    question_fr = models.CharField(max_length=500, help_text='Accepte l\'Html')
    answer = models.TextField(max_length=500, help_text='Supports Html')
    answer_fr = models.TextField(max_length=500, help_text='Accepte l\'Html')
    order = models.IntegerField()

    translated_fields = ['question', 'answer']

    class Meta:
        ordering = ['order']

    def serialize_fields(self):
        return ['slug', 'question', 'answer']

    def __unicode__(self):
        return self.slug


class Co2Equivalents(models.Model, TranslatedModelMixin):
    active = models.BooleanField(default=True)
    phrase = models.CharField(max_length=500)
    phrase_fr = models.CharField(max_length=500)
    co2_amount_unit = models.CharField(max_length=100)
    co2_amount_unit_fr = models.CharField(max_length=100)
    co2_amount = models.FloatField()

    translated_fields = ['phrase', 'co2_amount_unit']

    class Meta:
        verbose_name_plural = 'Co2 Equivalents'

    def serialize_fields(self):
        return ['phrase', 'co2_amount_unit', 'co2_amount']

    def __unicode__(self):
        return self.phrase


class DefinedTerms(models.Model):
    term_name = models.SlugField(max_length=100)
    title = models.CharField(max_length=500)
    content = models.TextField(help_text="Wrap the text in an html p element")
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)

    class Meta:
        verbose_name_plural = 'Defined Terms'

    def serialize_fields(self):
        return ['term_name', 'title', 'content']

    def __unicode__(self):
        return u'%s - %s' % (self.term_name, self.language)


class Locale(models.Model):
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, unique=True)
    co2r = models.CharField(max_length=100, blank=True, null=True, verbose_name='Directory Nav Text')
    shoot = models.CharField(max_length=100, blank=True, null=True, verbose_name='Send Feedback Button')
    our_mission = models.CharField(max_length=100, blank=True, null=True, verbose_name='About nav text')
    faq = models.CharField(max_length=100, blank=True, null=True)
    switch_language = models.CharField(max_length=200, blank=True, null=True)
    register_your_product = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    other_things_you_can_do = models.CharField(max_length=100, blank=True, null=True, verbose_name='Can Do Nav Text')
    give_us_feedback = models.CharField(max_length=100, blank=True, null=True, verbose_name='Feedback Nav Text')
    feedback_message_prompt = models.CharField(max_length=100, blank=True, null=True)
    learn_more_about_co2r = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    learn_more = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html', verbose_name='Learn more Button')
    trees_planted = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    inquire = models.CharField(max_length=100, blank=True, null=True)
    name_or_organization = models.CharField(max_length=100, blank=True, null=True)
    your_message = models.CharField(max_length=100, blank=True, null=True, verbose_name='Register Message Prompt')
    register_introduction = models.CharField(max_length=500, blank=True, null=True, help_text='Supports Html')
    introduction_title = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html and co2r-tags')
    introduction_text = models.TextField(blank=True, null=True, help_text='Supports Html and co2r-tags')
    directory_filter_input_prompt = models.CharField(max_length=100, blank=True, null=True)
    can_do_feedback_title = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    can_do_feedback_description = models.TextField(blank=True, null=True, help_text='Supports Html')
    can_do_spread_word_title = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    can_do_spread_word_description = models.TextField(blank=True, null=True, help_text='Supports Html')
    spread_the_word_default_message = models.TextField(blank=True, null=True)
    spread_the_word_button_label = models.CharField(max_length=100, blank=True, null=True)
    register_artifact_left_column = models.TextField(blank=True, null=True, help_text='Supports Html')
    register_artifact_right_body = models.TextField(blank=True, null=True, help_text='Supports Html')
    can_do_recruit_company_title = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    can_do_recruit_company_description = models.TextField(blank=True, null=True, help_text='Supports Html')
    can_do_sponsor_co2r_title = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    can_do_sponsor_co2r_description = models.TextField(blank=True, null=True, help_text='Supports Html')
    artifact_share_default_message = models.TextField(blank=True, null=True)
    artifact_download_report = models.CharField(max_length=100, blank=True, null=True)
    artifact_business_card_contact_lead_in = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    artifact_offset_since = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    artifact_report_section_title = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    artifact_other_eco_actions = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    artifact_total_vs_offset = models.CharField(max_length=500, blank=True, null=True, help_text='Supports Html')
    artifact_co2_sources = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    artifact_co2_per_thing_made = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    about_tab_label_map = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html and co2r-tags')
    about_tab_label_video = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html and co2r-tags')
    about_topic_1_title = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html and co2r-tags')
    about_topic_1_text = models.TextField(blank=True, null=True, help_text='Supports Html and co2r-tags')
    about_topic_2_title = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html and co2r-tags')
    about_topic_2_text = models.TextField(blank=True, null=True, help_text='Supports Html and co2r-tags')
    about_topic_3_title = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html and co2r-tags')
    about_topic_3_text = models.TextField(blank=True, null=True, help_text='Supports Html and co2r-tags')
    about_community_title = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html and co2r-tags')
    about_community_text = models.TextField(blank=True, null=True, help_text='Supports Html and co2r-tags')
    footer_sponsor_name = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    footer_sponsor_description = models.TextField(blank=True, null=True, help_text='Supports Html')
    footer_sponsor_link = models.CharField(max_length=100, blank=True, null=True)
    footer_taking_root = models.CharField(max_length=100, blank=True, null=True, help_text='Supports Html')
    footer_taking_root_description = models.TextField(blank=True, null=True, help_text='Supports Html')
    footer_colofon = models.TextField(blank=True, null=True, help_text='Supports Html')

    def __unicode__(self):
        return 'Site %s Locale' % self.language
