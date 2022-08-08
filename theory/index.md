# Theory

We started running events in Roblox in 2020 due to COVID lockdowns in Melbourne, Australia. To our surprise we found that we actually enjoyed it, especially as compared to events in Zoom. It still isn't clear to us exactly *why* it is better, but here are some ideas:

1. **Creative Expression**. The ability to manifest your own will, creatively, in a shared space makes it feel real. This feeling of reality buttresses the rest of the experience. Creative acts range from the individual and simple (demonstrating your attention by following the speaker between boards, or saying "thanks" to the speaker by writing it in fancy colours on your personal board) to the social and complex (see the [Pillars Incident](https://youtu.be/jryDAxI3XSo)).

2. **No Video.** In Zoom the feeling of co-presence is based on being able to see other people's faces. This is better than lecturing to a blank screen, but it is also [exhausting](https://psycnet.apa.org/fulltext/2021-77825-003.pdf). In a 3D environment you get a sense of other people paying attention to what is going on, without having to constantly see their faces and your own.

3. **Play is Serious**. When unexpected things happen (red bouncy chairs, people abducting you in a floating boat, personal board climbing, etc) and they are fun, it reinforces a sense of shared experience and refills our "I want to be here" tank for a while. It seems that for virtual events to work, this mix of "serious" content and play needs to be carefully managed to keep these tanks nonempty.

> I really keenly feel that the 3d world adds a new dimension to the social interaction (since you are fixed in space in Zoom, I guess it actually adds three new dimensions). Just the fact that I can stand next to someone, even without saying a word, is a kind of connection that is really lacking in Zoom. Roblox events feel much more socially natural to me than video calls do (even without video). Imagine an in-person meeting, but instead of being free to move physically, you are strapped into a chair with your head facing forward. All of the other attendees have the same constraints. You proceed to inject your discussion into one another. That's what Zoom feels like in comparison to Roblox. -- a student

Roblox is a utility platform for large-scale 3D social environments (see [Baszucki keynote](https://www.youtube.com/watch?v=G00GlCJc0mU) and their [SEC S-1 filing](https://www.sec.gov/Archives/edgar/data/1315098/000119312520298230/d87104ds1.htm)). We chose Roblox because of its massive user base and accessibility on a wide array of platforms (43 million daily active users as of early 2021) and user-friendly tooling supported by many tutorials (Roblox Studio). It's remarkable that you can deploy an attractive 3D world with 100 simultaneous multiplayer users for free, in minutes, from your laptop. While you can make ugly things with Roblox, you can make [beautiful](https://www.roblox.com/games/3158922185/Toyokawa-Inari-Shrine-Showcase) [things](https://www.roblox.com/games/7056870928/Ancient-Machine-SHOWCASE) [too](https://www.roblox.com/games/6524322789/Garden-Of-Hestia-SHOWCASE).

Metauni is inspired by the [Free University of Berlin](https://en.wikipedia.org/wiki/Free_University_of_Berlin), [Lianda](https://en.wikipedia.org/wiki/National_Southwestern_Associated_University) and [Sabishii University](https://www.kimstanleyrobinson.info/content/shabishii).

# Mechanics

Architecture is sometimes defined as the art and science of designing physical spaces. Frank Lloyd Wright said more poetically that

> The mission of an architect is to help people understand how to make life more beautiful, the world a better one for living in, and to give reason, rhyme, and meaning to life.

While buildings are static, people are dynamic; guiding the flows of matter and attention in physical spaces are very much the concern of an architect, both of physical and virtual spaces. This webpage is a place for collecting notes about the *mechanics of metauni* as they evolve. It is intended to be a practical document: as a designer of virtual spaces, what are best practices for making them beautiful and useful?

Some background knowledge about how lectures in metauni work: players walk their character from the spawn point in the world to a set of boards and

* Attach as Listener to an orb, perhaps briefly chat before the beginning of the lecture.
* Engage Orbcam to listen
* At some interval (perhaps every few boards, perhaps per set) disengage Orbcam and navigate their character to the next set of boards
* Re-engage Orbcam

## Antics

<img width="700" alt="Screen Shot 2022-07-21 at 7 31 50 am copy" src="https://user-images.githubusercontent.com/320329/180327328-cadeab5b-e67e-4434-a0d0-07fe9a596875.png">

> The problem is that passively watching a lecture does not quite light up enough different parts of the brain for focus to flow naturally

Antics give a way of distracting some part of your mind that is itching to do something, in a way that isn't disruptive (and actually is in some strange way constructive) and is sufficiently in-context that the other part of your mind can continue to focus.

## Rhythm

The illusion of being physically present in a virtual space is a powerful tool. It is desirable to have regular prompts to "re-enter" the illusion of being physically present. E.g. the boards come in sets, and we have developed a habit of exiting orbcam to move our character to the next set of boards and then re-entering orbcam. It's not a coincidence I think that the board climbing in the screenshot started shortly after one of those transitions - it's almost an invitation to engage your brain for a bit in the illusion of moving around.
