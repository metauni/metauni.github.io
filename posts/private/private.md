# Private servers

In the course of running seminars and [events](https://metauni.org/posts/events/events) we have learned a lot about how to support intellectual activities in virtual spaces, and we have built some technical tools. We have open sourced most of these tools, so others can reproduce what we are doing:

* Admin commands, Discord bot, viewer (https://metauni.org/posts/make-your-own/tools)
* Whiteboards (https://github.com/metauni/metaboard)

We will continue to talk publicly about what we have learned and release our tools as open source. However, some users will find it convenient to have a a simpler way to create environments similar to the ones in which we host metauni events, which will **just work**. To this end we are starting to explore the use of Roblox [Private Servers](https://en.help.roblox.com/hc/en-us/articles/205345050-How-do-I-Purchase-and-Configure-Private-VIP-Servers-).



One of the main directions I would like to explore with metauni in 2022 is to find ways to **encourage such collaborations** (while continuing to develop and release open source tools like metaboard). An important part of that is to lead by example, and Lucas and I have some plans along these lines.

Beyond that, I want to share an idea with you all and get some feedback. That idea is **metauni private servers**. Since I've already been using the term for something similar, I'll just call these **loci** for now.
 
Roblox has a feature called Private Servers (). If this is enabled for an experience you can (as a player) make your own private server, which you control insofar as you can decide who can join it. You also get an individual URL to share with people.

This seems like a natural way to package up all the metauni tools in a way that is "one click". The private server could contain boards, voice chat (which is built into Roblox), the admin system, and additionally be visually interesting with art and music and interesting architecture to explore before/after/in-between talks. Plus minigames. You could just advertise a time, give the URL to your private server, and host events more or less as we have been doing with metauni for the past year.

The other aspect of metauni that requires some technical skill is recording and editing the videos. In some sense this isn't difficult, but I manage to screw it up from time to time (hard drive space issues, my recording tool is misconfigured, etc.) so I can't pretend it's trivial either, and I think it will be a real barrier for many. On the other hand YouTube is an amazing tool for sharing knowledge and attracting attention, and I think it's important there is a good story for recording talks (if people wish to). 

To that end I've started work on a GCP bot that will start up Roblox, join your event, record video from a specified CFrame (that can be controlled through the admin system), and then email you a URL to download the video.

Great art, architecture, music and code isn't free, and maybe you shouldn't expect all of these private servers to be free either, if you want talented people to spend their valuable time making them. Personally I want other people to make these things and I'm happy to pay for them. I want a world where every month I can try out a new working environment with something beautiful and inspiring.

Since it's better to show than tell, here's a demo:

- "Proof of Concept" a crappy world constructed by freezing Songspires and putting boards in it and private servers and voice chat enabled. The owner of the private server is an admin (https://www.roblox.com/games/8276085305/Proof-of-Concept).
- A video showing how I made this https://youtu.be/pB44fI0lKso
