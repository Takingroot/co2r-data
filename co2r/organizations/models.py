from django.db import models


class Organization(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='organizations')
    name = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)

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
    name = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization)

    def __unicode__(self):
        return u'%s - %s' % (self.organization.name, self.name)
