# Automated Schedule Deployment

`schedule/schedule.yml` is the source of truth for metauni's weekly seminar schedule. Modifying this file kicks off the following processes:
1. Validate that the yaml is properly formatted.
1. Update `index.md` with generated markdown.
1. Create/update/delete Discord events.
1. Put schedule data in a Roblox data store, which is read from in-game by the What's On board.
1. Update `schedule.ics` with events.

## `schedule.yml` format

Besides dictionaries, all values should be strings. YAML strings can usually be written without quotes unless they contain a pound sign (#), end with a colon (:), or span multiple lines.

| Property | Description | Format |
| --- | --- | --- |
| metauni day | Date of the next metauni day | dd/mm/yyyy |
| timezone | Timezone for the seminar times | [+-]hh:mm |
| whats on | Seminars on for the next metauni day | dictionary |
| whats off | Seminars off for the next metauni day | dictionary |

The `whats on` and `whats off` properties are a list of seminars. Each seminar is a dictionary with its name as the key. The dictionary can contain the following properties:
| Property | Description | Format |
| --- | --- | --- |
| date | Date of the seminar. Defaults to the metauni day date if empty. | dd/mm/yyyy |
| time* | Time of the seminar | hh:mm-hh:mm |
| organizer | Names of the organizers | |
| desc | Description of the seminar | |
| note | Note specific to the upcoming metauni day | |
| website | Website for the seminar | URL |
| location | Location of the seminar | Roblox URL or Discord channel name|
| pocket | The name of a pocket, used by the What's On Board. `location` must link to The Rising Sea. | Must have exact capitalization and spelling, such as `Alpha Cove 1` |
| alias | Shorter name for the seminar to be used by the What's On board | |

\* `time` is the only required property.

## Project structure

Updating `schedule.yml` triggers the `metauni-day-schedule-workflow.yml` workflow located in `.github/workflows`. This workflow first calls `validate-schedule.py` to validate the schedule YAML. If successful, it then calls the following scripts in parallel:
* `update-index.py`
* `create-discord-events.py`
* `update-data-store.py`
* `update-icalendar.py`

Some of these scripts need secrets like a Roblox API key and Discord bot token; these can be seen at https://github.com/metauni/metauni.github.io/settings/secrets/actions.
