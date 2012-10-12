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
    question = models.CharField(max_length=500)
    question_fr = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    answer_fr = models.CharField(max_length=500)

    translated_fields = ['question', 'answer']

    def serialize_fields(self):
        return ['slug', 'question', 'answer']

    def __unicode__(self):
        return self.slug


class Co2Equivalents(models.Model, TranslatedModelMixin):
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
    content = models.TextField()
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)

    class Meta:
        verbose_name_plural = 'Defined Terms'

    def serialize_fields(self):
        return ['term_name', 'title', 'content']

    def __unicode__(self):
        return u'%s - %s' % (self.term_name, self.language)
