'''
 An abstract base class model that provides self-updating ``created`` and ``modified`` fields.
'''
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
