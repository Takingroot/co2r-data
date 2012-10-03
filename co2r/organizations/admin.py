from django.contrib import admin

from co2r.organizations.models import Organization, ContactInfo

admin.site.register(Organization, admin.ModelAdmin)
admin.site.register(ContactInfo, admin.ModelAdmin)
