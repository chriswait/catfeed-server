from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse
from .models import Feed

from slack import post_to_slack

recent = timedelta(seconds=10)

def index(request):
    recent_feed = Feed.objects.last()
    if (recent_feed is not None):
        recent_feed_date = recent_feed.feed_date
        current_date = timezone.now()
        diff = current_date - recent_feed_date
        return HttpResponse(int(diff > recent))
    return HttpResponse(1)

def add_feed(request):
    now = timezone.now()
    feed = Feed()
    feed.feed_date = now
    feed.save()
    slack_response = post_to_slack()
    if (slack_response is not None):
        return HttpResponse(slack_response)
    else:
        return HttpResponse("Success")
