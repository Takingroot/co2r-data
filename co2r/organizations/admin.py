from django.contrib import admin

from co2r.organizations.models import Organization, ContactInfo


class ContactInfoInline(admin.TabularInline):
    model = ContactInfo
    extra = 0


class OrganizationAdmin(admin.ModelAdmin):
    inlines = [ContactInfoInline]


admin.site.register(Organization, OrganizationAdmin)
