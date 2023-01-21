# Video

On this page you can find information about how the videos in the metauni [YouTube channel](https://www.youtube.com/channel/UCJTk6uSbSsclXN8v3b27_QQ) are created. One advantage of virtual lectures over in-person lectures is that they are (generally) more convenient to record at high quality, especially if speakers make use of cheaply available, [highly quality microphones](https://metauni.org/posts/instructions/hardware). As of this writing (September 2022) we have recorded over 200 hours of seminars and lectures.

## Workflow

The workflow for recording a seminar (not as speaker) are as follows:

0. **Prep**. Make sure you have enough disk space to record (somewhere between 20-30Gb per hour, depending on your settings, to record both your local audio and system audio and screen), microphones and devices are plugged into power, etc.
1. **Start Recording**. Make sure to record both the microphone on the local machine (for your voice), system audio (which is what will capture the voice of the speaker coming through Roblox voice chat or Discord) and the screen. It's a good idea to test your settings before recording a live seminar. You may want to run a keepalive script that moves your character every `X` minutes, in order to avoid having to manually interact with Roblox during the recording (the game will kick you for inactivity after 20 minutes).
2. **Join Roblox** and (a) Attach as Listener to the relevant Orb (b) use `Shift-C` to get into Orbcam without the Roblox UI.
3. **Editing**: most of the time in preparing videos lies in the editing process, and most of this lies in editing out background audio of your own voice track (which is not audible to others during the event, if you're muted). Generally it takes me somewhere from 3-6min per 1hr of video to process.
4. **Uploading**. Depending on your Internet connection, uploading a 1hr seminar to YouTube may take an hour or more.
5. **Processing**: adding titles and descriptions, choosing a thumbnail and playlists. While YouTube autograbs potential thumbnails (and does a surprisingly good job) you will probably want to upload higher quality screenshots. Tag the videos in the description with the recording date (which is generally going to be different to the upload date) to maintain sanity later.

## Tools

The tools used to make our recordings as of September 2022:

* [Camtasia](https://www.techsmith.com/video-editor.html) for video and audio recording and editing. While [OBS](https://obsproject.com) is free and capable, note that (at least on Mac OS X) there are some steps required to reliably record System Audio.
* [Dropbox](https://www.dropbox.com/home). Note that 20-30Gb per hour adds up to a lot of storage, if you have 4-5 seminars to record once a week.
* [YouTube](https://www.youtube.com). You may prefer options like [Vimeo](https://vimeo.com) but note that if you are planning to upload at the rate that metauni does, you will be paying a substantial amount per year to be on their business plans. YouTube has its downsides, but its advantages are also profound: it is free, and has enormous reach. I just upload through the web interface and use no additional tools beyond the built-in YouTube Studio.

For one hour seminars the final MP4 file is somewhere around 5-10Gb.

## Notes

In the early days quite a few seminar recordings were lost (a crime!), principally due to

* Running out of disk space (solution: *be rigorous about uploading old seminars to Dropbox or external storage well before new recording dates*).
* Failing to capture system audio (solution: *double check after system upgrades or Camtasia upgrades, as the system audio plugins may stop working*).

Some other remarks:

* YouTube is likely to be one of the principal ways that people discover your seminar. Therefore, you should make sure to put links to relevant webpages in the description of every one of your videos. Note that *Google search loves to recommend YouTube videos* so you might be surprised at the upside to putting a bit more effort into descriptions in your videos (Google also generates transcripts with ML and Google search seems to hook into those transcripts).

* It's better to process videos as soon as possible after recording, because you will want to fill in detailed descriptions while your memory of the seminar is fresh. **Use good thumbnails**. You probably want to be taking screenshots during the seminar itself in order to generate those thumbnails.

* It's a good idea to take a few screenshots during every seminar, to post to social media or into your community Discord.

## Places for improvement

Here are what I think of as the current margins to improve on the quality of metauni videos:

* **Microphones**: getting more speakers to use better microphones.
* **Background noise removal**: better tools for removing background noise and artifacts (I have tried a few but they stink).
* **Removing unnecessary Roblox UI**: generally I'm recording on an account I'm also using to interact with the world, communicate in the chat with audience members, switching to Discord to take care of admin tasks, etc., and all of this makes it into the recording.
* **Better intros and outros**: "so let's get started" -> "In today's seminar"
* **Obnoxious visual effects**: when it's done right, the "living" environment of metauni experiences adds to the recording, but when the lighting is bad or exaggerated (I'm looking at you *SunRays*) it can be quite bad.
* **Speaker uncertainty about orbs**: sometimes speakers will be obstructing the view of the board in orbcam but be unaware, or the orbcam may be looking at the wrong set of boards (it tries to follow you, but maybe you aren't standing in the right spot, or forgot to move).

## Recording seminars in OBS

- Record to mkv, not mp4. Then remux to mp4. From the OBS forum: 

> MKV if you need multi-track audio, FLV if you only need a single audio track. On a crash with either of these you may lose a second or two at the end. It's why they're the default format, and why an orange warning message pops up when you switch to mp4 warning you not to record to mp4. MP4 should NEVER be recorded to directly. As you've discovered, it is not a recording-safe format, and many editors have problems with the mp4 files that OBS creates when recorded direct anyway. Just record to MKV, then go you OBS' File menu, Remux Recordings to convert them to mp4s. You can also automatically remux at the completion of a recording by ticking a checkbox in Settings->Advanced.

- Under Settings > Video, set both Base and Output canvas resolution to 1920x1080, and fps to 30
- The rest of the recording config is under Output > Recording
- Recording Format: mkv
- Audio Track: Select 1 and 2
- Encoder: x264 or Apple VT H264 Software/Hardware. I'd assume the hardware one is the best of the 3 options but may depend on your machine.
- Encoder Settings: Bitrate is the per-second data budget. 2,500 is low, 60,000 is super-high. Lower bitrate becomes noticeable when there's a lot of movement on the screen. 6,000 is my currently chosen sweet spot for seminars and I'd estimate an hour is ~3GB.
- Rate Control: CBR is constant bitrate. That's probably fine. ABR and VBR adaptively adjust the bitrate in different ways. Maybe ABR would be beneficial - it varies bitrate across different regions of the screen. Maybe good for long songspires recordings.
- Keyframe Interval: 2 seconds. Helpful for preview scrubbing and editing.
- Add a new source and choose "macOS Screen Capture". You can configure this to capture the display or a specific window/application. This will also add an audio track to the scene.
- Right click the preview > Transform > Fit to Screen (or cmd + F). Then resize it as desired if you have a black margin in the preview.
- You should have two audio tracks, macOS Screen Capture and Mic/Aux. You can mute or unmute these and adjust audio levels to balance in game voice chat with your own voice. Click the three dots > Advanced Audio Properties, then make sure macOS Screen Capture is ticked on 1 and unticked on 2, and Mic/Aux is unticked on 1 and ticked on 2. This means we record Roblox audio to track 1 and microphone to track 2 - convenient for editing.
- If you can, wear headphones while recording (but still take microphone input from your desired source). Easier in editing to find sections where you're actually speaking and cut out the rest for improved audio experience. When both tracks are playing and the desktop audio is also audible in the mic, other peoples voices aren't as crisp and we hear background noise and super-bassy-keyboard-typing.

## Adding summaries and titles with ChatGPT

The summaries for YouTube descriptions and titles can be automaticaly inferred by ChatGPT and then edited by a human. Here are the steps

- Install the Chrome extension "YouTube Summary with ChatGPT" [here](https://chrome.google.com/webstore/detail/youtube-summary-with-chat/nmmicjeknamkfloonkhhcjmomieiodli/related).
- Go to the video in YouTube Studio and click the preview on the left to "View on YouTube".
- In the top right you should see a new box "Transcript and Summary" (if not, restart Chrome).
- Open it and click the "OpenAI" logo to pass the transcript to ChatGPT and get a summary.
- If a title is required, ask ChatGPT to "Give a short title for the talk". If it's too long, give it a word limit.
