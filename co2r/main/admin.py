from django.contrib import admin
from co2r.main.models import Co2Equivalents, DefinedTerms, Faq

admin.site.register(Co2Equivalents, admin.ModelAdmin)
admin.site.register(DefinedTerms, admin.ModelAdmin)
admin.site.register(Faq, admin.ModelAdmin)
