from django.contrib import admin
from co2r.artifacts.models import CarbonSource, Footprint, Artifact

admin.site.register(CarbonSource)
admin.site.register(Footprint)
admin.site.register(Artifact)
