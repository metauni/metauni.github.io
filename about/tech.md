---
title:
    metauni tech
description:
    How it works
---

This page is a bare-bones guide to the technology that enables metauni. Most of what you see here has been scripted by us in Luau on top of Roblox, although we rely on many third-party libraries (such as Roact and the Nexus VR character model).

# Chatbots

There are several GPT-powered chatbots present at all times at metauni. They are part of our seminars and other activities:

<p align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/T98E8kO0Iic" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

The chatbots 

- Can hear voice chat in seminars (through live transcription)
- Can see and reply to messages in the text chat
- Can read boards (via OCR)
- Can remember their past interactions with community members (who explicitly consent through the privacy controls)
- Have access to a library of relevant books and transcripts of past seminars (via vector embeddings and querying)
- Can interact with the world by walking around, and "seeing" a subset of objects
- Can build using the Builder Tools

The underlying LLM is either ChatGPT or GPT4 depending on the setting.

# Boards

Metaboards are multiplayer boards for sharing knowledge within Roblox. They are persistent (their contents stay there when you leave), accurate (all users see the same thing, even with redo/undo) and fast. For the code see the [Metaboard GitHub repo](https://github.com/metauni/metaboard). The easiest way to view boards is the Look button:

<p align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Oo3aM0Ga5-w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

## Boards and the web

Each board at metauni has a URL. Think of it like a Zoom meeting URL: when you visit the board URL in a web-browser, you can click on the "Visit Board" link to launch Roblox with the information required to take you directly to the board inside metauni. You can also view a board as a PNG. To find the URL of a board use the knot menu as shown in the video, and paste the Key into [metauniService](http://service.metauni.org).

<p align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/wrNxdVPv2Ms" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

# Orbs

Orbs make it easy to attend a seminar at metauni, by making it *optional* to control your avatar in 3D while listening to a talk. When you join an event, walk up to the orb, "Attach as Listener" and you'll hear from the position of the Orb (which is near the speaker) and have the option to engage "Orbcam" which gives you a fullscreen view of the boards. Disable Orbcam to move your avatar around and "Detach" at the end of the talk so you can listen from the position of your avatar again.

A white ring above your head means you are currently attached as a Listener (*note*: if you are far from an Orb, and can't hear someone speaking next to you, this might be why, as your "Metaverse ears" are somewhere else) and a black ring means someone is viewing through Orbcam.

<p align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/u9kDwbWJGgw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

For the code see the [Orb GitHub repo](https://github.com/metauni/orb).

# Pockets

Currently metauni is organised as one top-level world ([The Rising Sea](https://www.roblox.com/games/8165217582/The-Rising-Sea)) and numerous Pockets, which are worlds built from a template. For example, [Symbolic Wilds 5](https://www.roblox.com/games/start?placeId=8165217582&launchData=pocket%3ASymbolic%20Wilds%205) and [Symbolic Wilds 6](https://www.roblox.com/games/start?placeId=8165217582&launchData=pocket%3ASymbolic%20Wilds%206) are based off the same "world template" but the boards within have an independent existence (write on boards in Symbolic Wilds 5 and it doesn't affect what you see in Symbolic Wilds 6). Just as links connect webpages, portals connect Pockets. 

<p align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/jI0FCELBr30" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

You will need the appropriate permissions to create new pockets.

For the code see the [Metaportal GitHub repo](https://github.com/metauni/metaportal).

# VR and Replays

You can attend metauni events in VR with devices such as the Meta Quest (linked to a PC running Roblox). For more information see the [VR page](/vr). Replays are multi-channel recordings of speaker audio, writing on metaboards, motion capture of a VR character and additional scripted elements such as interactive 3D graphs or mathematical objects. We believe these are a compelling new format for communicating complex ideas.

<p align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/s4dfwxzXEFM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

To experience it for yourself, jump into the [Rising Sea](https://www.roblox.com/games/8165217582/The-Rising-Sea).
