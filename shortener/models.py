from shortener import utils
from django.db import models

# Create your models here.

class KirrURLManager(models.Manager):
    def all(*arg, **kwargs):
        qs = super(KirrURLManager, self).all(*arg, **kwargs)
        return qs

class KirrURL(models.Model):
    """
    Creats shortcode for urls
    """
    url = models.CharField(max_length=255)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        """
        Returns string representation of a KirrURL object
        """
        return str(self.url)

    def save(self, *arg, **kwargs):
        """
        Overrides save method of KirrURL model
        :param: *args
        :param: *kwargs
        """
        if not self.shortcode:
            self.shortcode = utils.create_shortcode(instance=self)
        super(KirrURL, self).save(*arg, **kwargs)
