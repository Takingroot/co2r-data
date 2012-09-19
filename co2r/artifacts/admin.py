from django.contrib import admin
from hvad.admin import TranslatableAdmin

from co2r.artifacts.models import CarbonSource, Footprint, Artifact

admin.site.register(CarbonSource, TranslatableAdmin)
admin.site.register(Footprint)
admin.site.register(Artifact)
