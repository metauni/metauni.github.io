#!/usr/bin/env python
import os
import yaml
from ics import Calendar, Event
from schedule_utils import parse_event_times, load_schedule

# Load schedule from yaml
schedule = load_schedule()
timezone = schedule.get("timezone")

# Create calendar
cal = Calendar()

def add_seminar_to_calendar(seminar):
    name = seminar.get("name")
    date = seminar.get("date")
    time = seminar.get("time")
    desc = seminar.get("desc")
    note = seminar.get("note")
    website = seminar.get("website")
    location = seminar.get("location")
    start_time, end_time = parse_event_times(date, timezone, time)

    event = Event()
    event.name = name
    event.begin = start_time.isoformat()
    event.end = end_time.isoformat()

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

with open("schedule.ics", "w") as f:
    f.writelines(cal)