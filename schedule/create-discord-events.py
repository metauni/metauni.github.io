#!/usr/bin/env python
import os
import sys
import re
import yaml
import json
import requests
import time
from datetime import datetime

schedule = None
with open(os.environ["SCHEDULE_PATH"], "r", encoding="utf-8") as f:
    schedule = yaml.safe_load(f)

BASE_URL = f"https://discord.com/api/guilds/{os.environ['GUILD_ID']}"
HEADERS = {
    "Authorization": f"Bot {os.environ['EVENTBOT_TOKEN']}",
    "Content-Type": "application/json"
}
DATE = schedule["date"]
TIMEZONE = schedule["timezone"]

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

def get_discord_events():
    url = BASE_URL + "/scheduled-events"
    response = run_with_retry(requests.get, url, headers=HEADERS)
    try:
        response_json = response.json()
        events = {}
        for event in response_json:
            events[event["name"]] = event
        return events
    except Exception as e:
        return []

def delete_discord_event(id, name):
    url = BASE_URL + f"/scheduled-events/{id}"
    response = run_with_retry(requests.delete, url, headers=HEADERS)
    if response.status_code == 204:
        print("DELETED " + name)
    else:
        print("FAILED TO DELETE " + name)
        raise Exception(response.text)

def update_discord_event(id, data):
    url = BASE_URL + f"/scheduled-events/{id}"
    response = run_with_retry(requests.patch, url, headers=HEADERS, data=json.dumps(data))
    if response.status_code == 200:
        print("UPDATED " + data["name"])
    else:
        print("FAILED TO UPDATE " + data["name"])
        raise Exception(response.text)

def create_discord_event(data):
    url = BASE_URL + "/scheduled-events"
    response = run_with_retry(requests.post, url, headers=HEADERS, data=json.dumps(data))
    if response.status_code == 200:
        print("CREATED " + data["name"])
    else:
        print("FAILED TO CREATE " + data["name"])
        raise Exception(response.text)

def get_discord_channels():
    url = BASE_URL + "/channels"
    response = run_with_retry(requests.get, url, headers=HEADERS)
    try:
        return response.json()
    except Exception as e:
        print("FAILED TO GET DISCORD CHANNELS:", e)
        raise Exception(e)

def parse_event_times(time):
    start_time = time[0:5]
    end_time = time[6:11]
    return (
        datetime.strptime(f"{DATE} {start_time} {TIMEZONE}", "%d/%m/%Y %H:%M %z"),
        datetime.strptime(f"{DATE} {end_time} {TIMEZONE}", "%d/%m/%Y %H:%M %z")
    )

channels_by_name = {}
channels_by_id = {}
for channel in get_discord_channels():
    channels_by_name[channel["name"]] = channel["id"]
    channels_by_id[channel["id"]] = channel["name"]

def build_event_request_data(name, event):
    location = event["location"]
    scheduled_start_time, scheduled_end_time = parse_event_times(event["time"])
    desc = event.get("desc", "")
    if event.get("note"):
        desc += event["note"] if len(desc) == 0 else " " + event["note"]

    data = {
        "name": name,
        "privacy_level": "2", # 2 is the only option as of v10
        "scheduled_start_time": scheduled_start_time.isoformat(),
        "scheduled_end_time": scheduled_end_time.isoformat(),
        "description": desc,
    }
    if re.fullmatch("\d+", location) and channels_by_id.get(location):
        # Location is the ID of a Discord channel
        data["channel_id"] = location
        data["entity_type"] = "2"
    else:
        data["entity_metadata"] = {
            "location": location
        }
        data["entity_type"] = "3"

    return data

current_events = get_discord_events()
new_events = {}
for seminar in schedule["whats on"]:
    name = next(iter(seminar))
    data = seminar[name]
    new_events[name] = data

    # Convert locations which are Discord channel names to their IDs
    location = data.get("location")
    if location and location[0] == "#" and channels_by_name.get(location[1:]):
        data["location"] = channels_by_name.get(location[1:])

for name, event in current_events.items():
    print("GOT EXISTING EVENT ", name)

    # Delete event if not in seminar.yml
    new_event = new_events.get(name)
    if new_event == None:
        delete_discord_event(event["id"], name)
        continue

    # Modify event if its details are different in seminar.yml
    new_event_start_time, new_event_end_time = parse_event_times(new_event["time"])
    if (
        # These apply to all events
        event["description"] != new_event.get("desc")
        or datetime.fromisoformat(event["scheduled_start_time"]) != new_event_start_time
        or datetime.fromisoformat(event["scheduled_end_time"]) != new_event_end_time
    ) or (
        # These apply to Discord voice channel events
        event.get("channel_id")
        and event["channel_id"] != new_event.get("location")
    ) or (
        # These apply to off-Discord events
        event.get("entity_metadata")
        and event["entity_metadata"]["location"] != new_event.get("location")
    ):
        update_discord_event(event["id"], build_event_request_data(name, new_event))

    # Remove event to avoid recreating it later
    del new_events[name]

for name, event in new_events.items():
    if event.get("location"):
        create_discord_event(build_event_request_data(name, event))