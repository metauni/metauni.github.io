---
title:
    Privacy
description:
    How your data is used at metauni
---

This document is a work-in-progress covering how your information is used. 

## Recordings

Some of our seminars are recorded and posted publicly to YouTube. The policy is that this is announced at the beginning of seminars and we are working on explicit UI that says **Recording in Progress** to make clear when recording has started and stopped. Whether or not recordings take place at all is up to the discretion of individual seminar organisers.

## AI

The privacy policy around AI interactions is under active discussion. It is likely that we will adopt a policy that whenever seminars are recorded, the records will be available to the AI infrastructure.

### NPCs

When an NPC is online at metauni you will see an "AI" menu item which you can click to view your privacy settings. The first column *Hear* shows whether or not the NPC can hear you (via transcription of voice chat). This feature is currently only active during specific seminars. The second column *Read* shows whether the NPC can see chat messages that you send. This is enabled by default, but can be disabled. The third column *Remember* shows whether the NPC will incorporate your chat messages into the summaries that it makes of its experiences (roughly every minute). These summaries are stored and queried over (see the section on embeddings on the [GitHub page](https://github.com/metauni/metauniOS/blob/main/README-AI.md)) in order to create the impression that the NPC maintains continuing conversations with you. This is disabled by default.

![privacy-screen](https://user-images.githubusercontent.com/320329/216851728-bb933673-28c3-49e3-9018-7a7e7dee6152.png)

You can find more technical information on the metauni AI infrastructure on the [GitHub page](https://github.com/metauni/metauniOS/blob/main/README-AI.md). 

Some general principles informing our thinking on this:

* **No surprises**: Speech or chat messages will not be stored unless it is clearly communicated and you are in a situation where there is a reasonable expectation that this is taking place: for example, you're in a seminar with a **Recording in Progress** sigil, or you are interacting with a chatbot that you have personally authorised to make memories of your interactions.

* **Warnings**: At the end of the day, your interactions with a GPT-based chatbot are going off to OpenAI's servers for processing and we have no control over what happens there, so one should probably be sensible and view these interactions as fundamentally public. However, the chatbots will soon be so good that people may be tempted to overshare. There should be reminders not to do this.

### Autosummaries

We make use of automatic transcription and summarisation services (the latter based on GPT3) to make seminar contents accessible to the AI infrastructure. You can see an example [here](https://metauniservice.com/transcript?videoID=HXCpQWZfWIw). Each paragraph under the *Long Summary* section is embedded and queried by NPCs

```
Density of states is an important concept in singular learning theory, which is related to solid state physics. It is a real valued function of a real parameter t, and its asymptotic behaviour is determined by the singularities of the set of true parameters. In a system with n discrete configurations, the density of states is the number of possible states with a given energy e per unit volume. For a continuous system, the density of states must be calculated differently. It is an important concept in understanding the effect of the rlct.
```

*Current thoughts*: These summaries may misrepresent the views of the speaker or participants in the seminar, and so should be incorporated into the AI infrastructure (and/or shown publicly) only with the consent of the speaker.
