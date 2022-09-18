# Helper file to delete all Discord events

import os
import requests
import time

BASE_URL = f"https://discord.com/api/guilds/{os.environ['GUILD_ID']}/scheduled-events"
HEADERS = {
    "Authorization": f"Bot {os.environ['EVENTBOT_TOKEN']}",
    "Content-Type": "application/json"
}

def delete_discord_event(id):
    url = BASE_URL + f"/{id}"
    run_with_retry(requests.delete, url, headers=HEADERS)

def run_with_retry(method, *args, **kwargs):
    while True:
        response = method(*args, **kwargs)
        try:
            response_json = response.json()
            if type(response_json) is dict and response_json.get("retry_after"):
                print(f"Rate limited for {response_json['retry_after']}s")
                time.sleep(response_json["retry_after"]/1000 + 1)
            else:
                return response
        except Exception as e:
            # Likely means the response wasn't json
            return response

events = run_with_retry(requests.get, BASE_URL, headers=HEADERS).json()
for event in events:
    delete_discord_event(event["id"])
    print("DELETED " + event["name"])