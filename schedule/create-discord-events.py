#!/usr/bin/env python
import os
import sys
import re
import yaml
import json
import requests
from datetime import datetime

schedule = None
with open(os.environ["SCHEDULE_PATH"], "r", encoding="utf-8") as f:
    schedule = yaml.safe_load(f)

BASE_URL = f"https://discord.com/api/guilds/{os.environ['GUILD_ID']}/scheduled-events"
HEADERS = {
    "Authorization": f"Bot {os.environ['EVENTBOT_CLIENT_SECRET']}",
    "Content-Type": "application/json"
}
DATE = schedule["date"]
TIMEZONE = schedule["timezone"]

def get_discord_events():
    response = requests.get(BASE_URL, headers=HEADERS)
    # TODO: Error handling
    return response.json()

def delete_discord_event(id):
    url = BASE_URL + f"/{id}"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code != 204:
        raise Exception(response.text)

def update_discord_event(id, data):
    print("UPDATING", data["name"])
    url = BASE_URL + f"/{id}"
    response = requests.patch(url, headers=HEADERS, data=json.dumps(data))
    # TODO: Error handling

def create_discord_event(data):
    print("CREATING", data["name"])
    response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(data))
    print(response.text)
    # TODO: Error handling

def parse_event_times(time):
    start_time = time[0:5]
    end_time = time[6:11]
    return (
        datetime.strptime(f"{DATE} {start_time} {TIMEZONE}", "%d/%m/%Y %H:%M %z"),
        datetime.strptime(f"{DATE} {end_time} {TIMEZONE}", "%d/%m/%Y %H:%M %z")
    )
    
# Converts the yaml to an easier format to work with
def parse_schedule(schedule):
    new_schedule = {}
    for seminar in schedule:
        name = next(iter(seminar))
        data = seminar[name]
        new_schedule[name] = data
    return new_schedule

def build_event_request_data(name, event):
    # TODO: Make this more concise
    location = event["location"]
    scheduled_start_time, scheduled_end_time = parse_event_times(event["time"])

    if re.fullmatch("\d+", location):
        # Location is a Discord channel
        # TODO: Instead look for the "#" and grab the channel ID from that
        return {
            "channel_id": location,
            "name": name,
            "privacy_level": "2", # 2 is the only option as of v10
            "scheduled_start_time": scheduled_start_time.isoformat(),
            "scheduled_end_time": scheduled_end_time.isoformat(),
            "description": event.get("desc", ""),
            "entity_type": "2"
        }
    else:
        return {
            "entity_metadata": {
                "location": location
            },
            "name": name,
            "privacy_level": "2", # 2 is the only option as of v10
            "scheduled_start_time": scheduled_start_time.isoformat(),
            "scheduled_end_time": scheduled_end_time.isoformat(),
            "description": event.get("desc", ""),
            "entity_type": "3"
        }

new_events = parse_schedule(schedule["whats on"])
current_events = get_discord_events()

for event in current_events:
    #TODO: Make the modifying more concise
    name = event["name"]

    # Delete event if not in seminar.yml
    new_event = new_events.get(name)
    if new_event == None:
        print("DELETING " + name)
        delete_discord_event(event["id"])
        continue

    # Modify event if its details are different in seminar.yml
    new_event_start_time, new_event_end_time = parse_event_times(new_event["time"])
    if (
        event["description"] != new_event.get("desc")
        or datetime.fromisoformat(event["scheduled_start_time"]) != new_event_start_time
        or datetime.fromisoformat(event["scheduled_end_time"]) != new_event_end_time
    ):
        update_discord_event(event["id"], build_event_request_data(name, new_event))

    if event.get("channel_id"):
        if event["channel_id"] != new_event.get("location"):
            update_discord_event(event["id"], build_event_request_data(name, new_event))
    elif event.get("entity_metadata"):
        if event["entity_metadata"]["location"] != new_event.get("location"):
            update_discord_event(event["id"], build_event_request_data(name, new_event))

    # Remove event to avoid recreating it
    del new_events[name]

for name, event in new_events.items():
    if event.get("location"):
        create_discord_event(build_event_request_data(name, event))