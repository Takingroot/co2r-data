from django.contrib import admin
from co2r.products.models import CarbonSource, Footprint, Product

admin.site.register(CarbonSource)
admin.site.register(Footprint)
admin.site.register(Product)
