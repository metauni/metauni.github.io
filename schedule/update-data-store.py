#!/usr/bin/env python
import os
import sys
import requests
import json
# Used to generate Content-MD5 which is used by Roblox to check data integrity
import base64, hashlib
from schedule_utils import *

ROBLOX_API_KEY = os.environ["ROBLOX_API_KEY"]
UNIVERSE_ID = 3138032475
BASE_URL = f"https://apis.roblox.com/datastores/v1/universes/{UNIVERSE_ID}"
DATASTORE_NAME = "Schedule"
DATASTORE_KEY = "Schedule"

schedule = load_schedule()
timezone = schedule.get("timezone")

# Create JSON data from schedule
new_whats_on = []
for seminar in schedule["whats on"]:
    name = seminar.get("name")
    date = seminar.get("date")
    start_time, end_time = parse_event_times(date, timezone, seminar.get("time"))

    new_whats_on.append({
        "name": name,
        "date": seminar.get("date"),
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
schedule["whats off"] = None
schedule["whats on"] = new_whats_on
schedule_json = json.dumps(schedule)

# Sort whats on
def sort_seminars(seminar):
    start_time, end_time = parse_event_times(seminar.get("date"), timezone, seminar.get("time"))
    return start_time.timestamp()
schedule["whats on"].sort(key=sort_seminars)

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