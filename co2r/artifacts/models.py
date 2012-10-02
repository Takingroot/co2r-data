from django.db import models
from co2r.organizations.models import Organization
from co2r.main.models import TranslatedModelMixin


class Artifact(models.Model, TranslatedModelMixin):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    description_fr = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='artifacts/thumbnail', null=True, blank=True)
    unit_quantity = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    unit_verbose = models.CharField(max_length=50, null=True, blank=True)
    unit_verbose_fr = models.CharField(max_length=50, null=True, blank=True)
    organization = models.ForeignKey(Organization)

    translated_fields = ['name', 'description', 'unit_verbose']
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


class Image(models.Model):
    artifact = models.ForeignKey(Artifact)
    caption = models.CharField(max_length=500)
    caption_fr = models.CharField(max_length=500)
    image = models.ImageField(upload_to='artifacts/images')

    translated_fields = ['caption']

    def __unicode__(self):
        return u'Image for %s' % self.artifact.name


class Footprint(models.Model, TranslatedModelMixin):
    artifact = models.ForeignKey(Artifact)
    year = models.IntegerField(null=True)
    co2_per_unit = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    total_tons_produced = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    total_offset_tons = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    total_trees_planted = models.IntegerField(null=True, blank=True)
    ton_offset_per_tree = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    annual_report = models.FileField(upload_to='annual_reports', null=True, blank=True)
    annual_report_fr = models.FileField(upload_to='annual_reports', null=True, blank=True)
    carbon_sources = models.ManyToManyField('CarbonSource', through='FootprintCarbonSource')

    translated_fields = ['annual_report']
    language_code = 'en'

    @property
    def carbon_sources_list(self):
        carbon_sources = FootprintCarbonSource.objects.filter(footprint=self)

        for carbon_source in carbon_sources:
            carbon_source.source.set_language(self.language_code)
        return carbon_sources

    def serialize_fields(self):
        return ['year', 'co2_per_unit', 'total_tons_produced', 'total_offset_tons',
            'total_trees_planted', 'ton_offset_per_tree', 'annual_report', 'carbon_sources_list']

    def __unicode__(self):
        return "%i Footprint for %s" % (self.year, self.artifact.name)

    @models.permalink
    def get_absolute_url(self):
        return ('footprint', (), {'slug': self.artifact.slug,
            'year': self.year})


class FootprintCarbonSource(models.Model):
    footprint = models.ForeignKey(Footprint)
    source = models.ForeignKey('CarbonSource')
    percent = models.IntegerField()

    @property
    def name(self):
        return self.source.name

    def serialize_fields(self):
        return ['name', 'percent']

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
