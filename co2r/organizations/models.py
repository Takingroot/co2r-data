from django.db import models
from co2r.main.models import TranslatedModelMixin

CONTACT_INFO_CHOICES = (('twitter', 'Twitter'),
    ('website', 'Website'),
    ('facebook', 'Facebook'),
    ('email', 'Email'),
    ('other', 'Other'))


class Organization(models.Model, TranslatedModelMixin):
    slug = models.SlugField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='organizations', null=True, blank=True)
    logo_mark = models.ImageField(upload_to='organizations', null=True, blank=True)
    name = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    description_fr = models.TextField(null=True, blank=True)
    is_partner = models.BooleanField(default=False)
    partner_description = models.TextField(null=True, blank=True)
    partner_description_fr = models.TextField(null=True, blank=True)
    website_url = models.CharField(max_length=400, blank=True)
    twitter_handle = models.CharField(max_length=40, blank=True)
    twitter_handle_fr = models.CharField(max_length=40, blank=True)

    translated_fields = ['name', 'description', 'partner_description']
    language_code = 'en'

    def logo_url(self):
        try:
            return self.logo.url
        except ValueError:
            return ''

    def logo_mark_url(self):
        try:
            return self.logo_mark.url
        except ValueError:
            return ''

    @property
    def available_twitter_handle(self):
        if self.language_code == 'en' or self.twitter_handle_fr == None:
            return self.twitter_handle
        else:
            return self.twitter_handle_fr

    @property
    def contact_infos(self):
        contact_infos = self.contactinfo_set.all()

        for contact_info in contact_infos:
            contact_info.set_language(self.language_code)
        return contact_infos

    def serialize_fields(self):
        return ['name', 'slug', 'logo_url', 'logo_mark_url', 'description', 'contact_infos', 'website_url',\
            'available_twitter_handle', 'is_partner', 'partner_description']

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

    def full_link(self):
        prepend = {'facebook': 'http://facebook.com/',
            'twitter': 'http://twitter.com/',
            'email': 'mailto:'}

        if self.contact_type in prepend:
            return prepend[self.contact_type] + self.link
        else:
            return self.link

    def serialize_fields(self):
        return ['name', 'contact_type', 'link', 'full_link']

    def __unicode__(self):
        return u'%s - %s' % (self.organization.name, self.name)
