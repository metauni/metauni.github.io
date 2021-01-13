# Free University of the Metaverse

The Free University is [on Roblox](https://www.roblox.com/games/6233302798/Metauni), a utility platform for persistent large-scale 3D social environments (see [Baszucki keynote](https://www.youtube.com/watch?v=G00GlCJc0mU)). It is free in the sense of [freedom](https://en.wikipedia.org/wiki/Free_University_of_Berlin). In its current iteration localised voice chat is based on Discord, a popular real-time communication platform.

## Instructions

1. When you enter an enabled Discord server register your Roblox username with `!register <username>`.
2. Manually enter any Discord voice channel
3. Move around the Roblox world

## Setup

Currently a Discord bot (running on Repl.it) `robloxvoicebot` translates information coming from a Discord webhook into the Discord API to move users between voice channels. Within the Roblox game scripts detect Touched events when a player enters a zone, and triggers the webhook.
