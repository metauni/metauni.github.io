#!/usr/bin/env python
import os
import re
import json
import requests
from datetime import datetime
from schedule_utils import *

BASE_URL = f"https://discord.com/api/guilds/{os.environ['GUILD_ID']}"
HEADERS = {
    "Authorization": f"Bot {os.environ['EVENTBOT_TOKEN']}",
    "Content-Type": "application/json"
}

schedule = load_schedule()
timezone = schedule.get("timezone")

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
        print("FAILED TO GET DISCORD CHANNELS: ", e)
        raise Exception(e)

channels_by_name = {}
channels_by_id = {}
for channel in get_discord_channels():
    channels_by_name[channel["name"]] = channel["id"]
    channels_by_id[channel["id"]] = channel["name"]

def build_event_request_data(name, event):
    location = event.get("location")
    start_time, end_time = parse_event_times(event.get("date"), timezone, event.get("time"))

    data = {
        "name": name,
        "privacy_level": "2", # 2 is the only option as of v10
        "scheduled_start_time": start_time.isoformat(),
        "scheduled_end_time": end_time.isoformat(),
        "description": event.get("desc", ""),
    }
    if re.fullmatch("\d+", location) and channels_by_id.get(location):
        # Location is the ID of a Discord channel
        data["channel_id"] = location
        data["entity_type"] = 2
    else:
        data["entity_metadata"] = {
            "location": location
        }
        data["entity_type"] = 3

    return data

current_events = get_discord_events()
new_events = {}
for seminar in schedule["whats on"]:
    name = seminar.get("name")
    new_events[name] = seminar

    # Convert locations which are Discord channel names to their IDs
    location = seminar.get("location")
    if location and location[0] == "#" and channels_by_name.get(location[1:]):
        seminar["location"] = channels_by_name.get(location[1:])

    # Append note to description
    note = seminar.get("note")
    if note:
        if seminar.get("desc"):
            seminar["desc"] += " " + note
        else:
            seminar["desc"] = note

for name, event in current_events.items():
    print("GOT EXISTING EVENT ", name)

    # Delete event if not in seminar.yml
    new_event = new_events.get(name)
    if new_event == None:
        delete_discord_event(event["id"], name)
        continue

    # Modify event if its details are different in seminar.yml
    new_event_start_time, new_event_end_time = parse_event_times(new_event.get("date"), timezone, new_event.get("time"))

    # Delete existing event if the new one is in the past
    if new_event_start_time < datetime.now(new_event_start_time.tzinfo):
        delete_discord_event(event["id"], name)
        continue

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
        start_time, end_time = parse_event_times(event.get("date"), timezone, event.get("time"))

        # Create the event as long as it's in the future
        if start_time >= datetime.now(start_time.tzinfo):
            create_discord_event(build_event_request_data(name, event))
