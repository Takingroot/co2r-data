from django.contrib import admin
from co2r.artifacts.models import CarbonSource, Footprint, Artifact, Image,\
	 OffsetVariables, OtherAction, OtherActionType


class OtherActionInline(admin.StackedInline):
    model = OtherAction
    extra = 0

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

class ArtifactAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

class FootprintCarbonSourceInline(admin.TabularInline):
    model = Footprint.carbon_sources.through

class FootprintAdmin(admin.ModelAdmin):
    inlines = [FootprintCarbonSourceInline, OtherActionInline]

admin.site.register(CarbonSource, admin.ModelAdmin)
admin.site.register(Footprint, FootprintAdmin)
admin.site.register(Artifact, ArtifactAdmin)
admin.site.register(OffsetVariables, admin.ModelAdmin)
admin.site.register(OtherActionType, admin.ModelAdmin)