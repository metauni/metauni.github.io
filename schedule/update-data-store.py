#!/usr/bin/env python
import os
import sys
import requests
import json
import yaml
# Used to generate Content-MD5 which is used by Roblox to check data integrity
import base64, hashlib
from schedule_utils import parse_event_times, load_schedule

ROBLOX_API_KEY = os.environ["ROBLOX_API_KEY"]
UNIVERSE_ID = 3138032475
BASE_URL = f"https://apis.roblox.com/datastores/v1/universes/{UNIVERSE_ID}"
DATASTORE_NAME = "Schedule"
DATASTORE_KEY = "Schedule"

# Load schedule from yaml
schedule = load_schedule()
metauni_day = schedule.get("date")
timezone = schedule.get("timezone")

# Create JSON data from schedule
new_whats_on = []
schedule["whats off"] = None
schedule["whats on"] = new_whats_on
for seminar in schedule["whats on"]:
    name = seminar.get("name")
    date = seminar.get("date")
    start_time, end_time = parse_event_times(date or metauni_day, timezone, seminar.get("time"))

    new_whats_on.append({
        "name": name,
        "time": seminar.get("time"),
        "start_datetime": start_time.isoformat(),
        "end_datetime": end_time.isoformat(),
        "organizer": seminar.get("organizer"),
        "desc": seminar.get("desc"),
        "note": seminar.get("note"),
        "location": seminar.get("location"), # Used on Roblox to get place id or identify if it's something else (Discord)
        "alias": seminar.get("alias"),
        "pocket": seminar.get("pocket")
    })
schedule_json = json.dumps(schedule)

# Send post request to datastore
content_md5 = str(base64.b64encode(hashlib.md5(bytes(schedule_json, encoding="utf8")).digest()), encoding="utf8")
headers = {
    "x-api-key": ROBLOX_API_KEY,
    "content-md5": content_md5,
}
response = requests.post(
    f"{BASE_URL}/standard-datastores/datastore/entries/entry?datastoreName={DATASTORE_NAME}&entryKey={DATASTORE_KEY}",
    headers=headers,
    data=schedule_json,
)
if response.status_code != 200:
    sys.exit(response.text) # Prints the content of the response and returns exit code 1