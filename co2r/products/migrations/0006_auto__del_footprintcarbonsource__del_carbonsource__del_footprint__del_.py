# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'FootprintCarbonSource'
        db.delete_table('products_footprintcarbonsource')

        # Deleting model 'CarbonSource'
        db.delete_table('products_carbonsource')

        # Deleting model 'Footprint'
        db.delete_table('products_footprint')

        # Deleting model 'Product'
        db.delete_table('products_product')


    def backwards(self, orm):
        # Adding model 'FootprintCarbonSource'
        db.create_table('products_footprintcarbonsource', (
            ('footprint', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Footprint'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.CarbonSource'])),
            ('percent', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('products', ['FootprintCarbonSource'])

        # Adding model 'CarbonSource'
        db.create_table('products_carbonsource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('products', ['CarbonSource'])

        # Adding model 'Footprint'
        db.create_table('products_footprint', (
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('total_offset_tons', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2, blank=True)),
            ('annual_report', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('co2_per_unit', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('total_trees_planted', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total_tons_produced', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2, blank=True)),
            ('ton_offset_per_tree', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2, blank=True)),
        ))
        db.send_create_signal('products', ['Footprint'])

        # Adding model 'Product'
        db.create_table('products_product', (
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unit_quantity', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('unit_verbose', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('icon_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('internal_name', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organizations.Organization'])),
        ))
        db.send_create_signal('products', ['Product'])


    models = {
        
    }

    complete_apps = ['products']