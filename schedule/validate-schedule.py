#!/usr/bin/env python
import os
import yaml
import re
from datetime import datetime

SEMINAR_PROPS = {"time", "organizer", "desc", "note", "website", "location"}
SEMINAR_MISSING_PROP_EXCEPTION = "Seminar \"{}\" is missing the property \"{}\""

def validate_seminars(schedule):
    for seminar in schedule:
        name = next(iter(seminar))
        data = seminar[name]
        for key, value in data.items():
            if not key in SEMINAR_PROPS:
                raise Exception(f"Unknown property \"{key}\" for seminar \"{name}\"")
            if type(value) != str: # Currently all properties are string. This could change. /shrug
                raise Exception(f"\"key\" property for seminar \"{name}\" must be a string, got {type(value).__name__}")

def validate_whats_on(schedule):
    validate_seminars(schedule)
    for seminar in schedule:
        name = next(iter(seminar))
        data = seminar[name]
        
        time = data.get("time")
        if time:
            time_match = re.match("\d{2}:\d{2}-\d{2}:\d{2}", time)
            if not time_match:
                raise Exception(f"\"time\" value for seminar \"{name}\" does not match hh:mm-hh:mm format")
            # TODO: Validate that the times are valid and the start comes before the end
        else:
            raise Exception(SEMINAR_MISSING_PROP_EXCEPTION.format(name, "time"))

        location = data.get("location")
        if location:
            # TODO: Validate location is a link or Discord channel
            pass

def validate_date(date):
    try:
        datetime.strptime(date, "%d/%m/%Y")
    except ValueError as e:
        raise Exception("\"date\" value does not match dd/mm/yyyy format")

def validate_timezone(timezone):
    try:
        datetime.strptime(timezone, "%z")
    except ValueError as e:
        raise Exception("\"timezone\" value does not match (+|-)hhmm format")

SCHEDULE_PROPS = {
    "whats on": validate_whats_on,
    "whats off": validate_seminars,
    "date": validate_date,
    "timezone": validate_timezone
}

with open(os.environ("SCHEDULE_PATH"), "r", encoding="utf-8") as f:
    loaded = yaml.safe_load(f)

    for prop, validator in SCHEDULE_PROPS.items():
        value = loaded.get(prop)
        if value:
            validator(value)
        else:
            raise Exception(f"Schedule is missing \"{prop}\" property")

    for prop in loaded.keys():
        if not SCHEDULE_PROPS.get(prop):
            raise Exception(f"Schedule has unknown property \"{prop}\"")