#!/usr/bin/env python
import os
import yaml
from ics import Calendar, Event
from datetime import datetime

schedule = None
with open(os.environ["SCHEDULE_PATH"], "r", encoding="utf-8") as f:
    schedule = yaml.safe_load(f)

DATE = schedule["date"]
TIMEZONE = schedule["timezone"]

cal = Calendar()

def parse_event_times(time):
    start_time = time[0:5]
    end_time = time[6:11]
    return (
        datetime.strptime(f"{DATE} {start_time} {TIMEZONE}", "%d/%m/%Y %H:%M %z"),
        datetime.strptime(f"{DATE} {end_time} {TIMEZONE}", "%d/%m/%Y %H:%M %z")
    )

def add_seminar_to_calendar(seminar):
    name = next(iter(seminar))
    data = seminar[name]

    time = data.get("time")
    desc = data.get("desc")
    note = data.get("note")
    website = data.get("website")
    location = data.get("location")

    scheduled_start_time, scheduled_end_time = parse_event_times(time)

    event = Event()
    event.name = name
    event.begin = scheduled_start_time.isoformat()
    event.end = scheduled_end_time.isoformat()

    if desc or note:
        event.description = ""
        if desc:
            event.description += desc
        if note:
            event.description += "\n\n" + note

    event.location = location
    event.url = website

    cal.events.add(event)

for seminar in schedule["whats on"]:
    add_seminar_to_calendar(seminar)

with open('schedule.ics', 'w') as f:
    f.writelines(cal)