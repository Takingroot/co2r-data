from django.db import models
from co2r.main.models import TranslatedModelMixin

CONTACT_INFO_CHOICES = (('twitter', 'Twitter'),
    ('website', 'Website'),
    ('facebook', 'Facebook'),
    ('email', 'Email'),
    ('other', 'Other'))


class Organization(models.Model, TranslatedModelMixin):
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='organizations')
    name = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    description_fr = models.TextField(null=True, blank=True)
    website_url = models.CharField(max_length=400, blank=True)

    translated_fields = ['name', 'description']
    language_code = 'en'

    def image_url(self):
        try:
            return self.image.url
        except ValueError:
            return ''

    @property
    def contact_infos(self):
        contact_infos = self.contactinfo_set.all()

        for contact_info in contact_infos:
            contact_info.set_language(self.language_code)
        return contact_infos

    def serialize_fields(self):
        return ['name', 'slug', 'image_url', 'description', 'contact_infos', 'website_url']

    def __unicode__(self):
        return self.slug


class ContactInfo(models.Model, TranslatedModelMixin):
    contact_type = models.CharField(max_length=100, choices=CONTACT_INFO_CHOICES)
    name = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization)

    translated_fields = ['name']
    language_code = 'en'

    def serialize_fields(self):
        return ['name', 'contact_type', 'link']

    def __unicode__(self):
        return u'%s - %s' % (self.organization.name, self.name)
