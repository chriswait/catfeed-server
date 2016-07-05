import requests
import json

url = "https://hooks.slack.com/services/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"
data = {
    'username': "Lady",
    'channel': '#lady',
    "text": "I just got fed!",
    "attachments": [
        {
            "text": "",
            "image_url": "http://thecatapi.com/api/images/get?format=src&type=gif"
        }
    ]
}
def post_to_slack():
    request = requests.post(url, data=json.dumps(data))
    return request.text
