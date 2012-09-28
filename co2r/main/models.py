from django.db import models

LANGUAGE_CHOICES = (('en', 'English'), ('fr', 'French'))


class Faq(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    question = models.CharField(max_length=500)
    question_fr = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    answer_fr = models.CharField(max_length=500)

    def __unicode__(self):
        return self.slug


class Co2Equivalents(models.Model):
    phrase = models.CharField(max_length=500)
    phrase_fr = models.CharField(max_length=500)
    co2_amount_unit = models.CharField(max_length=100)
    co2_amount = models.DecimalField(max_digits=14, decimal_places=2)

    def __unicode__(self):
        return self.phrase


class DefinedTerms(models.Model):
    term_name = models.SlugField(max_length=100)
    title = models.CharField(max_length=500)
    content = models.TextField()
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)

    def __unicode__(self):
        return u'%s - %s' % (self.term_name, self.language)
