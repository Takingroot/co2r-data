from django.contrib import admin
from co2r.artifacts.models import CarbonSource, Footprint, Artifact, Image, OffsetVariables


class FootprintInline(admin.StackedInline):
    model = Footprint
    extra = 0


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class ArtifactAdmin(admin.ModelAdmin):
    inlines = [FootprintInline, ImageInline]


class FootprintCarbonSourceInline(admin.TabularInline):
    model = Footprint.carbon_sources.through


class FootprintAdmin(admin.ModelAdmin):
    inlines = [FootprintCarbonSourceInline]


admin.site.register(CarbonSource, admin.ModelAdmin)
admin.site.register(Footprint, FootprintAdmin)
admin.site.register(Artifact, ArtifactAdmin)
admin.site.register(OffsetVariables, admin.ModelAdmin)

