# Loci

A _locus_ is a metauni node dedicated to a particular mathematical topic. It hosts expository content such as talkboards and is a place for shared mathematical activity. A locus may have associated **office hours** (see below) at which time the host will join the node and be available for discussion. Since the main form of interaction in a locus is the whiteboards, it is recommended that you use a tablet and stylus (e.g. an Apple iPad and Pencil).

Talkboards and other content in a locus have the following indexing convention similar to paragraphs in a text: **LCXYZ.xyz:abc** stands for locus **XYZ**, boardgroup **xyz** and individual board number **abc**.

## LC001 - Matrix factorisations

* **Link**: [Roblox](https://www.roblox.com/games/6461013759/metauni-Replays), [Discord](https://discord.gg/9yBaAxPSK8).
* **Office hours**: Fridays 9-10am AEDT.
* **Video**: TODO.

References:

* For exterior algebras: my notes on [Tensor, Exterior, Symmetric algebras](http://therisingsea.org/notes/TensorExteriorSymmetric.pdf).

## HOWTO

Here is how the talkboards are created.

* In Roblox Studio, insert a whiteboard with the replay functionality. Make sure that under `Settings > Security` you enable Studio Access to API Services, because the recording is stored to a DataStore (the Studio and live versions will connect to the same DataStore). Publish the Roblox game, make it public and join the live version on your iPad.
* Open up the whiteboard on your iPad and enter the "Record" menu. When you're ready to start recording tap "Start Record" on your iPad, and also start recording audio on your computer (I use Camtasia, but your favourite audio recording software will do). Generally I  When you're finished open the Record menu again and click "Stop Record" and stop recording the audio. Keep in mind that Roblox will only allow you to upload audio segments of seven minutes or less (I try to keep it under 5 minutes to be safe, large files are also rejected).
* Choose a name for the recording and enter it in the "Replay Name" field and click "Save Replay". This name is used as a key into the DataStore. I generally follow the above naming convention **LCXYZ.xyz:abc** for each board.
* Make sure your recording is in MP3 format (I use MP3 encoder, available on the Mac Appstore). Then upload it to Roblox (this costs Robux) and grab the ID.
* Stop Roblox Studio and edit the whiteboard, under `Config > Sound` and set `SoundId` to the ID of the uploaded audio. Set `Config > SpielName` to whatever you named the recording.
