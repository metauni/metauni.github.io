# Loci

A [locus](https://en.wikipedia.org/wiki/Method_of_loci) is a place for mathematical activity, organised around talking boards and scheduled office hours where the host is available for discussion. It is recommended that you use a tablet and stylus (e.g. an Apple iPad and Pencil). To join a locus you'll need Roblox and Discord, see the Instructions on the [metauni main page](https://metauni.org). 

Talking boards follow an indexing convention similar to paragraphs in a text: **LCXYZ.xyz:abc** stands for locus **XYZ**, boardgroup **xyz** and individual board number **abc**. To view a talking board, the best idea is to either click on it or go into "first person" mode by either using the scrollwheel on your mouse, the I/O keys on your keyboard, or pinching to zoom in.

## LC001 - Matrix factorisations

* **Links**: [Roblox](https://www.roblox.com/games/6461013759/metauni-Replays), [Discord](https://discord.gg/9yBaAxPSK8) voice channel `LC001`.
* **Office hours**: Friday 16-7-2021 10-10:30am Melbourne time.

### LC001.01 - General introduction

* **Video**: [YouTube](https://youtu.be/39d4g1ERDpw).
* D. Eisenbud, "[Homological algebra on a complete intersection, with an application to group representations](https://www.ams.org/journals/tran/1980-260-01/S0002-9947-1980-0570778-7/home.html)", Trans. Amer. Math. Soc. **260** (1980), 35--64.
* P. Dirac "[The quantum theory of the electron](https://royalsocietypublishing.org/doi/10.1098/rspa.1928.0023)", Proc. R. Soc. Lond. A117 (1928) 610--624.
* M. Khovanov and L. Rozansky, "[Matrix factorizations and link homology](https://arxiv.org/abs/math/0401268)", Fund. Math. 199 (2008), 1--91.

### LC001.02 - Exterior algebras

* **Video**: [YouTube](https://youtu.be/D_LoTZ8OYsc).
* The main reference is my notes on [Tensor, Exterior, Symmetric algebras](http://therisingsea.org/notes/TensorExteriorSymmetric.pdf).
* If you want to know more about universal properties, functors and categories you could see [my old course](http://therisingsea.org/post/mast90068/) but there are many fine references for category theory (my usual reference is Borceux's "Handbook of categorical algebra").

## HOWTO

Here is how the talking boards are created.

* In Roblox Studio, insert a whiteboard with the replay functionality. Make sure that under `Settings > Security` you enable Studio Access to API Services, because the recording is stored to a DataStore (the Studio and live versions will connect to the same DataStore). Publish the Roblox game, make it public and join the live version on your iPad.
* Open up the whiteboard on your iPad and enter the "Record" menu. When you're ready to start recording tap "Start Record" on your iPad, and also start recording audio on your computer (I use Camtasia, but your favourite audio recording software will do). Generally I  When you're finished open the Record menu again and click "Stop Record" and stop recording the audio. Keep in mind that Roblox will only allow you to upload audio segments of seven minutes or less (I try to keep it under 5 minutes to be safe, large files are also rejected).
* Choose a name for the recording and enter it in the "Replay Name" field and click "Save Replay". This name is used as a key into the DataStore. I generally follow the above naming convention **LCXYZ.xyz:abc** for each board.
* Make sure your recording is in MP3 format (I use MP3 encoder, available on the Mac Appstore). Then upload it to Roblox (this costs Robux) and grab the ID.
* Stop Roblox Studio and edit the whiteboard, under `Config > Sound` and set `SoundId` to the ID of the uploaded audio. Set `Config > SpielName` to whatever you named the recording.

Note that as currently implemented, if there is a "next board" it will start playing as soon as the recorded strokes end, so make sure you write something on the board just before you stop recording and stop the audio (I usually remember this by writing the board number). Also note that each time you click "Start Record" the replay history is wiped, so "Stop Recording" is **not** a pause in the recording.
