import requests
import json
from django.utils import timezone

url = "https://hooks.slack.com/services/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"
def post_to_slack_with_datetime(now):
    imgRequest = requests.post("http://thecatapi.com/api/images/get?format=src&type=gif")
    imgRedirect = imgRequest.url

    time_string = timezone.localtime(now).strftime("%H:%M")
    timestamp_url = "http://timestamp.chriswait.net/"+time_string

    data = {
        'username': "Lady",
        'channel': '#lady',
        "text": "I just got fed!",
        "attachments": [
            {
                "text": "",
                "image_url": imgRedirect,
            },
            {
                "text": "",
                "image_url": timestamp_url,
            }
        ]
    }
    request = requests.post(url, data=json.dumps(data))
    return request.text
