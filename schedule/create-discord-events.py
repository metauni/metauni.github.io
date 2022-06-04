#!/usr/bin/env python
import os
import yaml
from datetime import datetime

EVENTS_URL = f"https://discord.com/api/guilds/{os.environ("GUILD_ID")}/scheduled-events"

schedule = None
with open(os.environ("SCHEDULE_PATH"), "r", encoding="utf-8") as f:
    schedule = yaml.safe_load(f)

date = datetime.strptime(schedule.date, "%d/%m/%Y")
timezone = datetime.strptime(schedule.timezone, "%z")

for seminar in schedule["whats on"]:
    name = next(iter(seminar))
    data = seminar[name]

    location = data.get("location")
    if not location:
        # Skip seminars without a location (ex. tea break)
        continue

    # Create request body
    time = data.time
    start_time = time.sub[0:5]
    end_time = time.sub[6:11]

    entity_type = None # "2" for Discord voice channel, "3" for elsewhere

    desc = data.get("desc", "")
    privacy_level = "2" # "2" is the only option as of v10 of the API

    request_body = {
        "entity_metadata": {
            "location": location
        },
        "name": name,
        "privacy_level": "2", # 2 is the only option as of v10
        "scheduled_start_time": f"{date}T{start_time}{timezone}",
        "scheduled_end_time": f"{date}T{end_time}{timezone}",
        "description": desc,
        "entity_type": entity_type
    }

    header = {
        "Authorization": f"Bot {os.environ("EVENTBOT_CLIENT_SECRET")}",
        "Content-Tye": "application/json"
    }

    url = BASE_URL

# env = {
#     "general_channel_id": "798370333492772927",
#     "dev_channel_id": "921236687370223657",
#     "guild_id": "798370332758245407",
# }

# json_body = {
#     "entity_metadata": {
#         "location": "https://www.roblox.com/games/8164954581/"
#     },
#     "name": "Cell Learning Theory",
#     "privacy_level": "2",
#     "scheduled_start_time": f"2022-08-06T12:00:00+1000",
#     "scheduled_end_time": f"2022-08-06T12:30:00+1000",
#     "description": "Learning and computation in biology",
#     "entity_type": "3" # 3 for other location, 2 for discord voice chat
# }