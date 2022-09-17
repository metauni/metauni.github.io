#!/usr/bin/env python
import os
import yaml
import re
from datetime import datetime

SEMINAR_PROPS = {"time", "organizer", "desc", "note", "website", "location", "alias", "pocket"}
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

# Validates that the seminar times do not overlap
# def validate_seminar_times(seminars):
#     times = []
#     for seminar in seminars:
#         name = next(iter(seminar))
#         data = seminar[name]

#         time = data["time"]
#         times.append({
#             "name": name,
#             "start": int(time[0:2])*60 + int(time[3:5]),
#             "end": int(time[6:8])*60 + int(time[9:11])
#         })
#     times.sort(key=lambda e: e["start"])
    
#     overlaps = []
#     for i in range(len(times) - 1):
#         this_overlaps = []
#         for j in range(i + 1, len(times) - 1):
#             if times[i]["end"] > times[j]["start"]:
#                 this_overlaps.append(times[j]["name"])
#         if len(this_overlaps) > 0:
#             overlaps.append(f"\"{times[i]['name']}\" extends into \"" + "\", \"".join(this_overlaps) + "\"")

#     if len(overlaps) > 0:
#         raise Exception("The following seminars overlap:\n" + "\n".join(overlaps))


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
            if int(time[0:2]) > 24 or int(time[3:5]) > 59:
                raise Exception("Start time is not on a regular 24 hour clock")
            if int(time[6:8]) > 24 or int(time[9:11]) > 59:
                raise Exception("End time is not on a regular 24 hour clock")
            if int(time[0:2])*60 + int(time[3:5]) > int(time[6:8])*60 + int(time[9:11]):
                raise Exception("Start time must come before end time")
        else:
            raise Exception(SEMINAR_MISSING_PROP_EXCEPTION.format(name, "time"))

        location = data.get("location")
        if location:
            # TODO: Validate location is a link or Discord channel
            pass

        alias = data.get("alias")
        if alias and len(alias) >= len(name):
            raise Exception(f"The alias \"{alias}\" should be shorter than its seminar name \"{name}\"")
    # validate_seminar_times(schedule)

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

with open(os.environ["SCHEDULE_PATH"], "r", encoding="utf-8") as f:
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