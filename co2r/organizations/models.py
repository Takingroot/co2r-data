from django.db import models

CONTACT_INFO_CHOICES = (('twitter', 'Twitter'),
    ('facebook', 'Facebook'),
    ('email', 'Email'),
    ('other', 'Other'))


class Organization(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='organizations')
    name = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    description_fr = models.TextField(null=True, blank=True)

    translated_fields = ['name', 'description']

    def image_url(self):
        try:
            return self.image.url
        except ValueError:
            return ''

    def serialize_fields(self):
        return ['name', 'slug', 'image_url']

    def __unicode__(self):
        return self.slug


class ContactInfo(models.Model):
    contact_type = models.CharField(max_length=100, choices=CONTACT_INFO_CHOICES)
    name = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization)

    translated_fields = ['name']

    def __unicode__(self):
        return u'%s - %s' % (self.organization.name, self.name)
