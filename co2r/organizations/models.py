from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=100)
    internal_name = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='organizations')

    def image_url(self):
        try:
            return self.image.url
        except ValueError:
            return ''

    def serialize_fields(self):
        return ['name', 'internal_name', 'image_url']

    def __unicode__(self):
        return self.name
