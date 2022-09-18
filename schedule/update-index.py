#!/usr/bin/env python
import os
import yaml
from datetime import datetime
from schedule_utils import parse_date, parse_event_times, load_schedule

BEGIN_WHATS_ON = "<!-- BEGIN WHATS ON -->"
END_WHATS_OFF = "<!-- END WHATS OFF -->"
BEGIN_WHATS_OFF = "<!-- BEGIN WHATS OFF -->"
END_WHATS_ON = "<!-- END WHATS ON -->"
DATE_FORMAT = "%B %d, %Y" # ex. September 17, 2022

def seminar_to_markdown(seminar):
    name = seminar.get("name")
    date = seminar.get("date")
    time = seminar.get("time")
    organizer = seminar.get("organizer")
    desc = seminar.get("desc")
    note = seminar.get("note")
    website = seminar.get("website")
    location = seminar.get("location")

    text = "* "
    if website:
        text += f"**[{name}]({website})**"
    else:
        text += f"**{name}**"
    if time:
        text += f" **{time}**"
    if organizer:
        text += f" (*{organizer}*)"
    if desc or note:
        text += ":"
        if desc:
            text += f" {desc}"
        if note:
            text += f" {note}"

    return text

# Formats a list of strings as a row of a markdown table
def list_to_table_row(array):
    row = "|"
    for value in array:
        row += f" {value or ''} |"
    return row

# def seminar_to_markdown(seminar):
    # name = next(iter(seminar))
    # data = seminar[name]
    # return list_to_table_row([
    #     name,
    #     # data.get("date"),
    #     data.get("time"),
    #     data.get("organizer"),
    #     data.get("desc"),
    #     data.get("note"),
    #     # data.get("website"),
    #     f"[Roblox]({data.get('location')})",
    #     # data.get("location")
    # ])

# Load schedule.yml into dictionary
# schedule = None
# with open(os.environ["SCHEDULE_PATH"], "r", encoding="utf-8") as f:
#     schedule = yaml.safe_load(f)
schedule = load_schedule()
metauni_day = schedule["metauni day"]
timezone = schedule["timezone"]

# Categorize seminars by date
seminars_by_date = {}
for seminar in schedule["whats on"]:
    date = seminar.get("date") or metauni_day
    if date:
        timestamp = parse_date(date).timestamp() # Time since Unix epoch as a float
        seminars_list = seminars_by_date.get(timestamp)
        if seminars_list:
            seminars_list.append(seminar)
        else:
            seminars_by_date[timestamp] = [seminar]
seminars_by_date = list(seminars_by_date.items()) # Convert dictionary to list of the form [(timestamp, seminar)]
seminars_by_date.sort(key=lambda x: x[0]) # Sorts the list by timestamp

# Generate markdown for seminars
def sort_seminars(seminar):
    start_time, end_time = parse_event_times(seminar.get("date") or metauni_day, timezone, seminar.get("time"))
    return start_time.timestamp()

whats_on_md = ""
whats_off_md = ""
for item in seminars_by_date:
    timestamp = item[0]
    seminars = item[1]
    seminars.sort(key=sort_seminars)
    whats_on_md += f"### {datetime.fromtimestamp(timestamp).strftime(DATE_FORMAT)}\n"
    # whats_on_md += list_to_table_row(["Name", "Time", "Organizer", "&nbsp; "*5 + "Description" + "&nbsp; "*5, "Note", "Location"]) + "\n"
    # whats_on_md += "|---"*6 + "|\n"
    for seminar in seminars:
        whats_on_md += seminar_to_markdown(seminar) + "\n"
for seminar in schedule["whats off"]:
    whats_off_md += seminar_to_markdown(seminar) + "\n"

# Insert generated markdown into index.md
with open("index.md", "r+", encoding="utf-8") as f:
    lines = []
    inside_tags = False # Used to skip over existing what's on text

    # TODO: Throw if the tags don't exist

    for line in f.readlines():
        if line.startswith(BEGIN_WHATS_ON):
            inside_tags = True
            lines.append(f"{BEGIN_WHATS_ON}\n{whats_on_md}{END_WHATS_ON}\n")
        elif line.startswith(BEGIN_WHATS_OFF):
            inside_tags = True
            lines.append(f"{BEGIN_WHATS_OFF}\n{whats_off_md}{END_WHATS_OFF}\n")
        elif line.startswith(END_WHATS_ON):
            inside_tags = False
        elif line.startswith(END_WHATS_OFF):
            inside_tags = False
        elif not inside_tags: # Skips over lines between BEGIN and END tags
            lines.append(line)

    f.seek(0) # Move cursor to start of file
    f.truncate(0) # Clear file
    f.writelines(lines)