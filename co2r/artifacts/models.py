import math

from django.db import models
from django.template.defaultfilters import linebreaksbr

from co2r.organizations.models import Organization
from co2r.main.models import TranslatedModelMixin


class Artifact(models.Model, TranslatedModelMixin):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100, help_text='Supports Html')
    name_fr = models.CharField(max_length=100, help_text='Accepte l\'Html')
    active = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True, help_text='Supports Html')
    description_fr = models.TextField(null=True, blank=True, help_text='Accepte l\'Html')
    thumbnail = models.ImageField(upload_to='artifacts/thumbnail', null=True, blank=True)
    unit_quantity = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    unit_verbose = models.CharField(max_length=50, null=True, blank=True)
    unit_verbose_fr = models.CharField(max_length=50, null=True, blank=True)
    for_total_made = models.CharField(max_length=200, null=True, blank=True)
    for_total_made_fr = models.CharField(max_length=200, null=True, blank=True)
    organization = models.ForeignKey(Organization)

    translated_fields = ['name', 'description', 'unit_verbose', 'for_total_made']
    language_code = 'en'

    def __unicode__(self):
        return self.name

    def icon_image_url(self):
        return self.icon_image.url

    def thumbnail_url(self):
        try:
            return self.thumbnail.url
        except ValueError:
            return ''

    def organization_name(self):
        return self.organization.name

    def serialize_fields(self):
        return [
            'name',
            'slug',
            'active',
            'description',
            'thumbnail_url',
            'unit_quantity',
            'unit',
            'unit_verbose',
            'for_total_made',
            'organization',
            'images',
            'footprints']

    @property
    def footprints(self):
        footprints = self.footprint_set.all()

        for footprint in footprints:
            footprint.set_language(self.language_code)
        return footprints

    @property
    def images(self):
        images = self.image_set.all()
        for image in images:
            image.set_language(self.language_code)
        return images

    @models.permalink
    def get_absolute_url(self):
        url = ('artifact', (), {'slug': self.slug})
        return url


class Image(models.Model, TranslatedModelMixin):
    artifact = models.ForeignKey(Artifact)
    caption = models.CharField(max_length=500, null=True, blank=True)
    caption_fr = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='artifacts/images')

    language_code = 'en'
    translated_fields = ['caption']

    def serialize_fields(self):
        return ['caption', 'image_url']

    @property
    def image_url(self):
        try:
            return self.image.url
        except ValueError:
            return ''

    def __unicode__(self):
        return u'Image for %s' % self.artifact.name


class Footprint(models.Model, TranslatedModelMixin):
    artifact = models.ForeignKey(Artifact)
    year = models.IntegerField(null=True)
    co2_per_unit = models.FloatField(null=True, blank=True, help_text="Enter quantities as tonnes")
    total_tons_produced = models.FloatField(null=True, blank=True)
    total_offset_tons = models.FloatField(null=True, blank=True)
    annual_report = models.FileField(upload_to='annual_reports', null=True, blank=True)
    annual_report_fr = models.FileField(upload_to='annual_reports', null=True, blank=True)
    carbon_sources = models.ManyToManyField('CarbonSource', through='FootprintCarbonSource')

    translated_fields = ['annual_report']
    language_code = 'en'

    _offset_variables = None

    @property
    def carbon_sources_list(self):
        carbon_sources = FootprintCarbonSource.objects.filter(footprint=self)

        for carbon_source in carbon_sources:
            carbon_source.source.set_language(self.language_code)
            carbon_source.percent = carbon_source.co2_amount_tons / self.total_tons_produced

        return carbon_sources

    @property
    def offset_variables(self):
        if self.year == None:
            return None

        if self._offset_variables != None:
            return self._offset_variables

        try:
            offset_variables = OffsetVariables.objects.get(year=self.year)
        except OffsetVariables.DoesNotExist:
            self._offset_variables = ''

        self._offset_variables = offset_variables

        return self._offset_variables

    @property
    def trees_planted(self):
        variables = self.offset_variables
        
        if variables == '':
            return 'No Offset Variables Set for Year %i' % self.year

        trees_planted = math.floor(self.total_offset_tons * variables.offsets_per_co2_ton * variables.trees_per_offset)

        return trees_planted


    @property
    def annual_report_url(self):
        try:
            return self.annual_report.url
        except ValueError:
            return ''

    def serialize_fields(self):
        return ['year', 'co2_per_unit', 'total_tons_produced', 'total_offset_tons',
            'trees_planted', 'annual_report_url', 'carbon_sources_list',
            'other_actions']

    @property
    def other_actions(self):
        other_actions = self.otheraction_set.all()
        for other_action in other_actions:
            other_action.set_language(self.language_code)

        return other_actions

    def __unicode__(self):
        return "%i Footprint for %s" % (self.year, self.artifact.name)

    @models.permalink
    def get_absolute_url(self):
        return ('footprint', (), {'slug': self.artifact.slug,
            'year': self.year})


class OtherAction(models.Model, TranslatedModelMixin):
    footprint = models.ForeignKey(Footprint)
    type = models.ForeignKey('OtherActionType', null=True)
    description = models.TextField(help_text="Each new line creates a new list item")
    description_fr = models.TextField(help_text="Each new line creates a new list item")
    
    language_code = 'en'
    translated_fields = ['name', 'description']

    def description_formatted(self):
        return linebreaksbr(self.description)

    def description_list(self):
        return self.description.split('\n')

    def name(self):
        self.type.set_language(self.language_code)
        return self.type

    def serialize_fields(self):
        return ['name', 'description_formatted', 'description_list']

    def __unicode__(self):
        return "Other Action for %s" % (self.footprint)


class OtherActionType(models.Model, TranslatedModelMixin):
    name = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)
    icon_code = models.CharField(max_length=20)

    language_code = 'en'
    translated_fields = ['name']

    def serialize_fields(self):
        return ['name', 'icon_code']

    def __unicode__(self):
        return self.name


class FootprintCarbonSource(models.Model):
    footprint = models.ForeignKey(Footprint)
    source = models.ForeignKey('CarbonSource')
    co2_amount_tons = models.FloatField()

    @property
    def name(self):
        return self.source.name

    def serialize_fields(self):
        return ['name', 'co2_amount_tons', 'percent']

    def __unicode__(self):
        return u'%s - %s' % (self.footprint.artifact.name, self.source.name)


class CarbonSource(models.Model, TranslatedModelMixin):
    name = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)

    translated_fields = ['name']
    language_code = 'en'

    def serialize_fields(self):
        return ['name']

    def __unicode__(self):
        return self.name


class OffsetVariables(models.Model):
    year = models.IntegerField(unique=True)
    offsets_per_co2_ton = models.FloatField(null=True, blank=True)
    trees_per_offset = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Offset Variables'

    def __unicode__(self):
        return "Variables for %i" % self.year

