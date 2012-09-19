from django.contrib import admin
from hvad.admin import TranslatableAdmin

from co2r.organizations.models import Organization

admin.site.register(Organization, TranslatableAdmin)
