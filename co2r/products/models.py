from django.db import models
from co2r.organizations.models import Organization


class CarbonSource(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    internal_name = models.SlugField(max_length=100)
    active = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    icon_image = models.ImageField(upload_to='products/icon', null=True, blank=True)
    unit_quantity = models.IntegerField(null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    unit_verbose = models.CharField(max_length=50, null=True, blank=True)
    organization = models.ForeignKey(Organization)

    def __unicode__(self):
        return self.name


class Footprint(models.Model):
    product = models.ForeignKey(Product)
    year = models.IntegerField(null=True)
    co2_per_unit = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    total_tons_produced = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    total_offset_tons = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    total_trees_planted = models.IntegerField(null=True, blank=True)
    ton_offset_per_tree = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    annual_report = models.FileField(upload_to='annual_reports', null=True, blank=True)
    carbon_sources = models.ManyToManyField(CarbonSource, through='FootprintCarbonSource')

    def __unicode__(self):
        return "%i Footprint for %s" % (self.year, self.product.name)


class FootprintCarbonSource(models.Model):
    footprint = models.ForeignKey(Footprint)
    source = models.ForeignKey(CarbonSource)
    percent = models.IntegerField()