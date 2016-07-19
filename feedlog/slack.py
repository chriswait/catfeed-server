import requests
import json
from django.utils import timezone

url = "https://hooks.slack.com/services/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"
def post_to_slack_with_datetime(now):
    imgRequest = requests.post("http://thecatapi.com/api/images/get?format=src&type=gif&size=med")
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
