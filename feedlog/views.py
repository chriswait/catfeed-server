from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse, JsonResponse
from StringIO import StringIO

from .models import Feed
from .timestamp import drawTimestamp
from .slack import post_to_slack_with_datetime

recent = timedelta(seconds=10)

def index(request):
    recent_feed = Feed.objects.last()
    # If no prior feed, should feed 
    if (recent_feed is None):
        return HttpResponse(1)

    recent_feed_date = timezone.localtime(recent_feed.feed_date)
    current_date = timezone.localtime(timezone.now())
    fed_today = current_date.day == recent_feed_date.day
    diff = current_date - recent_feed_date

    should_feed = False
    # If have fed today already, wait at least 8 hours
    if fed_today:
        should_feed = diff > timedelta(hours=8)
        # print "fed today, %f hours ago, should feed: %s" % ((diff.seconds / 3600.0), should_feed)
    # otherwise, wait at least 10 hours
    else:
        should_feed = diff > timedelta(hours=10)
        # print "fed yesterday, %f hours ago, should feed: %s" % ((diff.seconds / 3600.0), should_feed)

    return HttpResponse(int(should_feed))

def add_feed(request):
    now = timezone.now()
    feed = Feed()
    feed.feed_date = now
    feed.save()

    # post message to slack
    slack_response = post_to_slack_with_datetime(now)
    if (slack_response is not None):
        return HttpResponse(slack_response)
    else:
        return HttpResponse("Success")

def feeds(request):
    feeds = Feed.objects.all().order_by("feed_date")
    feed_times = {
        "feed_times": [timezone.localtime(feed.feed_date) for feed in feeds]
    }
    response = JsonResponse(feed_times)
    return response

def timestamp(request, timestamp):
    response = HttpResponse(content_type="image/png")
    img = drawTimestamp(timestamp)
    img.save(response, "PNG")
    return response

