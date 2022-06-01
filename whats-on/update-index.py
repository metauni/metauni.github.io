import os
import yaml
print("asdf")
def seminar_to_markdown(seminar):
    name = next(iter(seminar))
    data = seminar[name]

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
        stripped = line.rstrip()
        if stripped == "<!-- BEGIN WHATS ON -->":
            inside_tags = True
            lines.append(stripped + "\n")
            lines.append(whats_on)
        elif stripped == "<!-- BEGIN WHATS OFF -->":
            inside_tags = True
            lines.append(stripped + "\n")
            lines.append(whats_off)
        elif stripped == "<!-- END WHATS ON -->" or stripped == "<!-- END WHATS OFF -->":
            inside_tags = False
            lines.append(stripped + "\n")
        elif not inside_tags:
            lines.append(line)

    f.seek(0) # Move cursor to start of file
    f.truncate(0) # Clear file
    f.writelines(lines)