from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=100)
    internal_name = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='organizations')

    def __unicode__(self):
        return self.name
