The Free University of the Metaverse (metauni) is a public network (like the World Wide Web) built out of [Roblox](https://www.roblox.com/) nodes (webpages) connected by teleports (links). It is free in the sense of [freedom](https://en.wikipedia.org/wiki/Free_University_of_Berlin). Roblox is a utility platform for persistent large-scale 3D social environments (see [Baszucki keynote](https://www.youtube.com/watch?v=G00GlCJc0mU) and their [SEC S-1 filing](https://www.sec.gov/Archives/edgar/data/1315098/000119312520298230/d87104ds1.htm)). It can be a [beautiful place](https://www.roblox.com/games/5326950832/Roblox-Realistic-Forest-Demo)! 

The purpose of this page is to help others set up metauni nodes and demonstrate best practices through our own nodes, coordinate the development of open source tools (e.g. for uploading preprints and talk slides) and host announcements of virtual events (sign up [here](http://tinyletter.com/adminmetauni) for the mailing list). Code and demonstration levels are hosted [on Github](https://github.com/metauni/metauni-dev) and contributors are welcome. 

You can contact us at <admin@metauni.org>.

## Events

Upcoming events:

* **Friday 22/1/2021 10-11am AEDT**: Talk by [Daniel Murfet](http://www.therisingsea.org) on deep learning theory ([lecture notes](https://www.dropbox.com/s/tc3mmw69lkqprta/DLT%20Lecture%201.pdf?dl=0)).
* **Friday 29/1/2021 10am-12pm AEDT**: Drop in session for getting help with [setting up your own node](http://metauni.org/posts/make-your-own/make-your-own).
* Talk by [Adam Dorr](http://www.adamdorr.com/about/) on energy policy.
* Talk by [Lucas Cantor](https://www.lucascantormusic.com/), subject TBA.
* Talk by Ziling Ye on Chinese history.

There is a brief [video guide](https://youtu.be/mA1X-aP-jBU) to attending talks. If you have a question during a talk, please send `?` using the in-game chat and a question mark bubble will appear over your head for the speaker to see. Typically events consist of a talk, question and discussion time, followed by challenges with unique in-game items as prizes. For the history of challenge winners and instructions for collecting a prize, see the [challenges](http://metauni.org/posts/challenges/challenges) page.

## Instructions

### How do I get in?

In its current iteration localised voice chat in metauni is based on [Discord](https://www.discord.com), a popular real-time communication platform. Currently the only active server on metauni is the Rising Sea. Here are instructions for visiting:

1. Create Roblox and Discord accounts.
2. Enter the Rising Sea [Discord channel](https://discord.gg/9yBaAxPSK8).
3. Register your Roblox username with `!register <username>`.
4. Manually enter any Discord voice channel (e.g. General).
5. Enter the [Rising Sea Roblox](https://www.roblox.com/games/6224932973/The-Rising-Sea).

Some notes on in-game controls and features:

* You should notice translucent boxes on the ground near the white floating displays or other points of interest. Those zones, when entered, will transition your Discord into an appropriate location-specific voice channel. Leaving the zone will not remove you from the channel. If you want to return to the General voice channel, click the "General" button that has appeared on your GUI in the top right corner.

* By default you move your player with the arrow keys (or WASD) and you can look around by holding down the right mouse button, or doing a two-finger drag on a trackpad. The control scheme can be changed in Settings (press Escape in-game to access) and you may prefer `Click to Move` for your `Movement Mode`.

* To interact with in-world GUI elements, such as buttons, you simply (left) click on them. Most of the white floating displays can be clicked on for a more readable popup view, including the presenter display in the talk zone.

* To use the in-game chat press `/`. 

You should comply with the [Roblox community rules](https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Rules) while on their platform, and that includes the developer rules if you are creating your own nodes. These rules are in place to protect the children who spend a lot of time in Roblox, and seem to me well-intentioned and reasonable. However this does mean that you should **refrain from using the in-game chat or images to share URLs** or post Discord information inside your node. This coordination should happen on Discord or through some other channel. Finally, *do not under any circumstances climb the knot*.

### Troubleshooting

If you have trouble connecting to Roblox (and you have clicked Retry a few times) you might have to turn off your VPN. Some people have a better experience with the separate Discord application as compared to running Discord in the browser. The Discord-Roblox integration can be a bit weird when you sign in for the first time, please try switching zones a few times (by walking in between two of them) or manually changing voice channels once in Discord (then the bot may notice that you exist). If all else fails, you can manually join the `zTalk` channel on Discord to hear talks.

### How do I host my own node?

Currently a Metauni node consists of code inside a Roblox game, talking to a Discord webhook, talking to a Discord bot hosted on Repl.it and talking to a database backend on MongoDB. We have compiled [detailed instructions](http://metauni.org/posts/make-your-own/make-your-own) for setting up your own node and run regular drop-in sessions where you can get help (subscribe to the mailing list for notifications).

## History

* 14/1/2021 - History start, got Discord integration working, [intro video](https://youtu.be/0K3sCNvFpWE).
* 16/1/2021 - Update with clickable documents, audio plinths and working teleports, [another video](https://youtu.be/CJeuAvoRE9U).
* 16/1/2021 - Quick [video](https://youtu.be/vkaBQw9-OBY) on understanding "Publish to Roblox".
* 17/1/2021 - Rewrote Discord bot to use MongoDB, fixed some bugs, implemented slide presentations ([video](https://youtu.be/9-fyJvrTRzA)).
* 17/1/2021 - Implemented popover "fullscreen" GUI for looking at slides, synced to the presenter's current slide. There is a [video](https://youtu.be/rNtZGYnRHdA) demoing this feature as well as recapping the other features.
* 18/1/2021 - First release of [Metauni demonstration node](http://www.metauni.org/Backup18-1-2021.rbxl) (the Rising Sea world Roblox file).
* 18/1/2021 - How to attend an in-world talk ([video](https://youtu.be/mA1X-aP-jBU))
* 18/1/2021 - Instructions for [building your own node](https://youtu.be/SEwmyMInqTM) to be read in conjunction with [this blog post](https://towardsdatascience.com/creating-a-discord-bot-from-scratch-and-connecting-to-mongodb-828ad1c7c22e) for the database and [this one](https://repl.it/talk/learn/Hosting-discordpy-bots-with-replit/11008) for keep alive.
* 20/1/2021 - Development update: implemented "gather all" for voice channels ([video](https://youtu.be/GJunGvBGo6Y)) and implemented the challenge system, with the first two challenges for Friday's talk `#1A, #1B` see [challenges](http://metauni.org/posts/challenges/challenges).

Current contributors are [Daniel Murfet](http://www.therisingsea.org) and [Billy Price](https://billyprice.me/).
