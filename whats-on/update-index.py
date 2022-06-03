#!/usr/bin/env python
import os
import yaml

SEMINAR_PROPS = {"time", "organizer", "desc", "note", "website", "location"}
BEGIN_WHATS_ON = "<!-- BEGIN WHATS ON -->"
END_WHATS_OFF = "<!-- END WHATS OFF -->"
BEGIN_WHATS_OFF = "<!-- BEGIN WHATS OFF -->"
END_WHATS_ON = "<!-- END WHATS ON -->"

def seminar_to_markdown(seminar):
    name = next(iter(seminar))
    data = seminar[name]

    for key in data.keys():
        if not key in SEMINAR_PROPS:
            raise Exception(f"Unknown property \"{key}\" for seminar \"{name}\"")

    time = data.get("time")
    organizer = data.get("organizer")
    desc = data.get("desc")
    note = data.get("note")
    website = data.get("website")
    location = data.get("location")

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

whats_on = ""
whats_off = ""

with open("whats-on/whats-on.yml", "r", encoding="utf-8") as f:
    loaded = yaml.safe_load(f)
    for seminar in loaded["whats on"]:
        whats_on += seminar_to_markdown(seminar) + "\n"
    for seminar in loaded["whats off"]:
        whats_off += seminar_to_markdown(seminar) + "\n"

with open("index.md", "r+", encoding="utf-8") as f:
    lines = []
    inside_tags = False # Used to skip over existing what's on text

    for line in f.readlines():
        if line.startswith(BEGIN_WHATS_ON):
            inside_tags = True
            lines.append(BEGIN_WHATS_ON + "\n")
            lines.append(whats_on)
        elif line.startswith(BEGIN_WHATS_OFF):
            inside_tags = True
            lines.append(BEGIN_WHATS_OFF + "\n")
            lines.append(whats_off)
        elif line.startswith(END_WHATS_ON):
            inside_tags = False
            lines.append(END_WHATS_ON + "\n")
        elif line.startswith(END_WHATS_OFF):
            inside_tags = False
            lines.append(END_WHATS_OFF + "\n")
        elif not inside_tags: # Skips over lines between BEGIN and END tags
            lines.append(line)

    f.seek(0) # Move cursor to start of file
    f.truncate(0) # Clear file
    f.writelines(lines)