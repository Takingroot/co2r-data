from django.contrib import admin

from co2r.artifacts.models import CarbonSource, Footprint, Artifact

admin.site.register(CarbonSource, admin.ModelAdmin)
admin.site.register(Footprint, admin.ModelAdmin)
admin.site.register(Artifact, admin.ModelAdmin)
