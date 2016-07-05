from __future__ import unicode_literals

from django.db import models

class Feed(models.Model):
    feed_date = models.DateTimeField('date/time fed')
    def __str__(self):
        return str(self.feed_date)
