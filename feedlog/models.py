from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Feed(models.Model):
    feed_date = models.DateTimeField('date/time fed')
    def __str__(self):
        local_datetime = timezone.localtime(self.feed_date)
        time_string = local_datetime.strftime("%H:%M - %d/%m/%y")
        return time_string
