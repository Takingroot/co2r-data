from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='organizations')

    def image_url(self):
        try:
            return self.image.url
        except ValueError:
            return ''

    def serialize_fields(self):
        return ['name', 'slug', 'image_url']

    def __unicode__(self):
        return self.name
