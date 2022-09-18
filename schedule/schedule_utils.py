import os
import yaml
import time
from datetime import datetime

# Parses a string of the form "HH:MM-HH:MM" into two datetime objects
def parse_event_times(date, timezone, time):
    times = time.split("-")
    start_time = times[0]
    end_time = times[1]
    return (
        datetime.strptime(f"{date} {start_time} {timezone}", "%d/%m/%Y %H:%M %z"),
        datetime.strptime(f"{date} {end_time} {timezone}", "%d/%m/%Y %H:%M %z")
    )

# Parses a string of the form "dd/mm/yyyy" into a datetime object
def parse_date(date):
    return datetime.strptime(date, "%d/%m/%Y")

def run_with_retry(method, *args, **kwargs):
    while True:
        response = method(*args, **kwargs)
        try:
            response_json = response.json()
            if type(response_json) is dict and response_json.get("retry_after"):
                print(f"Rate limited for {response_json['retry_after']}s")
                time.sleep(response_json["retry_after"]/1000 + 1)
            else:
                return response
        except Exception as e:
            # Likely means the response wasn't json
            return response

def load_schedule():
    with open(os.environ["SCHEDULE_PATH"], "r", encoding="utf-8") as f:
        schedule = yaml.safe_load(f)

        # Reformat "whats on" and "whats off"
        whats_on = []
        for seminar in schedule["whats on"]:
            name = next(iter(seminar))
            data = seminar[name]
            data["name"] = name
            whats_on.append(data)
        schedule["whats on"] = whats_on

        whats_off = []
        for seminar in schedule["whats off"]:
            name = next(iter(seminar))
            data = seminar[name]
            data["name"] = name
            whats_off.append(data)
        schedule["whats off"] = whats_off

        return schedule
