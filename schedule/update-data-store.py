#!/usr/bin/env python
import os
import sys
import requests
import json
import yaml
from datetime import datetime
# Used to generate Content-MD5 which is used by Roblox to check data integrity
import base64, hashlib

ROBLOX_API_KEY = os.environ["ROBLOX_API_KEY"]
UNIVERSE_ID = 3138032475
BASE_URL = f"https://apis.roblox.com/datastores/v1/universes/{UNIVERSE_ID}"
DATASTORE_NAME = "Schedule"
DATASTORE_KEY = "Schedule"

schedule = None
with open(os.environ["SCHEDULE_PATH"], "r", encoding="utf-8") as f:
    schedule = yaml.safe_load(f)

date = schedule.get("date")
timezone = schedule.get("timezone")

schedule["whats off"] = None
newWhatsOn = []
for seminar in schedule["whats on"]:
    seminarName = next(iter(seminar))
    seminarData = seminar[seminarName]

    times = seminarData.get("time").split("-")
    start_time = times[0]
    end_time = times[1]

    # make datetime objects for start and end times factoring in date and timezone
    start_time = datetime.strptime(f"{date} {start_time} {timezone}", "%d/%m/%Y %H:%M %z")
    end_time = datetime.strptime(f"{date} {end_time} {timezone}", "%d/%m/%Y %H:%M %z")

    newSeminar = {
        "name": seminarName,
        "time": seminarData.get("time"),
        "start_datetime": start_time.isoformat(),
        "end_datetime": end_time.isoformat(),
        "organizer": seminarData.get("organizer"),
        "desc": seminarData.get("desc"),
        "note": seminarData.get("note"),
        "location": seminarData.get("location"), # Used on Roblox to get place id or identify if it's something else (Discord)
        "alias": seminarData.get("alias")
    }

    newWhatsOn.append(newSeminar)
schedule["whats on"] = newWhatsOn

scheduleJson = json.dumps(schedule)
contentMd5 = str(base64.b64encode(hashlib.md5(bytes(scheduleJson, encoding="utf8")).digest()), encoding="utf8")

headers = {
    'x-api-key': ROBLOX_API_KEY,
    'content-md5': contentMd5,
}

response = requests.post(
    f"{BASE_URL}/standard-datastores/datastore/entries/entry?datastoreName={DATASTORE_NAME}&entryKey={DATASTORE_KEY}",
    headers=headers,
    data=scheduleJson,
)

if response.status_code != 200:
    sys.exit(response.text) # Prints the content of the response and returns exit code 1