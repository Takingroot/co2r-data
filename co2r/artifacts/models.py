from django.db import models

from co2r.organizations.models import Organization


class CarbonSource(models.Model):
    name = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Artifact(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    description_fr = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='artifacts', null=True, blank=True)
    icon_image = models.ImageField(upload_to='artifacts/icon', null=True, blank=True)
    unit_quantity = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    unit_verbose = models.CharField(max_length=50, null=True, blank=True)
    unit_verbose_fr = models.CharField(max_length=50, null=True, blank=True)
    organization = models.ForeignKey(Organization)

    def __unicode__(self):
        return self.name

    def icon_image_url(self):
        return self.icon_image.url

    def image_url(self):
        try:
            return self.image.url
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
            'image_url',
            'icon_image_url',
            'unit_quantity',
            'unit',
            'unit_verbose',
            'organization'
        ]

    @models.permalink
    def get_absolute_url(self):
        return ('artifact', (), {'slug': self.slug})


class Footprint(models.Model):
    artifact = models.ForeignKey(Artifact)
    year = models.IntegerField(null=True)
    co2_per_unit = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    total_tons_produced = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    total_offset_tons = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    total_trees_planted = models.IntegerField(null=True, blank=True)
    ton_offset_per_tree = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    annual_report = models.FileField(upload_to='annual_reports', null=True, blank=True)
    annual_report_fr = models.FileField(upload_to='annual_reports', null=True, blank=True)
    carbon_sources = models.ManyToManyField(CarbonSource, through='FootprintCarbonSource')

    def __unicode__(self):
        return "%i Footprint for %s" % (self.year, self.artifact.name)

    @models.permalink
    def get_absolute_url(self):
        return ('footprint', (), {'slug': self.artifact.slug,
            'year': self.year})


class FootprintCarbonSource(models.Model):
    footprint = models.ForeignKey(Footprint)
    source = models.ForeignKey(CarbonSource)
    percent = models.IntegerField()
