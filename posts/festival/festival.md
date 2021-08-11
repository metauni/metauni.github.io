# Rules of Roblox

When creating the content for your node it is important to remember that while higher education and corporate usage is on Roblox's roadmap (see p.31 and p.131 of their [SEC S-1 filing](https://www.sec.gov/Archives/edgar/data/1315098/000119312520298230/d87104ds1.htm)) at the moment they make their money from kids playing games and so they have a stringent process for examining uploaded images and audio (and [they need it](https://techcrunch.com/2018/07/18/roblox-responds-to-the-hack-that-allowed-a-childs-avatar-to-be-raped-in-its-game/)). To avoid getting your account locked, you should familiarise yourself with:

* Roblox [Terms of Use](https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use).

* Roblox [Community Rules](https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Rules).

* The [Moderation Messages](https://en.help.roblox.com/hc/en-us/articles/360020870412-Understanding-Moderation-Messages).

It is likely that from time to time you *will* inadvertently have your account locked for violating their Terms of Use or Community Rules while uploading content in Roblox Studio (we have). When this happens you may be locked out of Roblox Studio. Just go to the Roblox homepage and log into your account, and will see a "Moderation Message" explaining your violation. If you agree to follow the rules in future they unlock your account (which happens instantly in our experience). The messages are listed  along with further explanation of what causes each message. While this is disconcerting there is no reason to panic: Roblox claims only to delete accounts for the most serious violations or people who are acting maliciously. 

This uncertainty does mean that you should **avoid uploading images or audio to your world immediately prior to an event**.

Here are some of the rule violations you are likely to encounter in preparing academic content for Roblox:

* Make sure your in-game text and images do not contain **URLs or email addresses** (e.g. the first or last page of preprints). Their AI will catch anything that even remotely looks like either, so "a@b" or "a.b" is risky. However links to YouTube, Twitter, Twitch are explicitly allowed.
* Do not put information about Discord in-world or instructions for using it
* Photos of people (they are afraid of users identifying other users)
* We have observed that even the word "Talk" on a `SurfaceGui > TextLabel` is enough to cause problems (not Moderation Messages but weird behaviour in Roblox Studio). In general if you observe strange behaviour, think about whether or not you could have introduced something their AIs dislike.
* Make sure the text in your images is not too small for the filtration system to read (this may easily happen if you compress high resolution images, rendering small fonts close to unreadable).

## Is the metauni Discord system consistent with the rules?

Yes, we believe so. The usage of Discord servers for voice chat associated with Roblox games is widespread, and there is an [official method](https://en.help.roblox.com/hc/en-us/articles/360000910966-Social-Media-Links-for-Games) for listing your Discord server on your Roblox page (see e.g. [this popular game](https://www.roblox.com/games/331811267/Innovation-Inc-Spaceship) with over 37 million visits, which has an active Discord server featuring voice chat). Note that Discord requires users to be at least 13 years old, and you **should avoid encouraging anyone to break these rules** in order to visit your metauni node.

It is certainly against the Roblox rules to advertise or encourage people to use Discord (or provide links) within the world itself (see [this](https://devforum.roblox.com/t/reminder-regarding-permissible-links/61736) Developer Forum post):

> Linking of Discord servers and references to Discord on the Roblox website are not allowed. Since Discord’s Terms of Service only allows people aged 13 or older to use their platform and Roblox is a platform for all ages, we cannot risk unfairly exposing underage users to platforms such as Discord. In light of this, we will continue to ban the advertisement of discord servers, any references to Discord will not be permitted through our chat systems. We understand the argument can be made that YouTube, Twitter, and Twitch all have similar policies regarding users under 13, but these platforms also allow users to browse without logging in, while Discord requires you to have an account so people aged 12 and under cannot see the information you are linking. This is the primary reason we are not able to allow it.

The current metauni setup involves Roblox communicating via `HTTPService` with a Discord bot to move users between voice channels as they navigate the world, and this communication could be blocked if the Roblox administrators decide it is against their rules. But all we are doing is sending location information from Roblox to Discord, and there are certainly no rules against that (perhaps the *intent* of that information matters, and they can interpret their rules however they wish).

The relevant passage from the Community Rules is

> **Building your game.** When building your game, it’s important to do the following: Filter all chat and text. Developers must pass all chat and/or game text through Roblox’s filtering system. Roblox scans all chat communication and player inputted text for the safety of our users and legal compliance reasons, including the Children's Online Privacy Protection Act (COPPA). All chat and content must also be reportable through the Report Abuse system.

Our reading is that this rule is meant to prevent developers from putting in internal circumventions to the chat system (i.e. in-world keyboards that display on in-world screens).

## Are metauni whiteboards consistent with the rules?

Yes, we believe so, if they are used for sketching, drawing, diagrams, mathematics etc. However, using a whiteboard to bypass the in-game chat violates the Community Rules (see above), so we believe it is appropriate for administrators to observe carefully how the whiteboards are used and put in place mechanisms to flag inappropriate images and restrict access for users who abuse them. The [guidance on Roblox Developer forums](https://devforum.roblox.com/t/are-you-allowed-to-let-players-draw-in-your-game/231264) is that whiteboards are not against the rules, but it is recommended to give users a way of flagging a drawn image as inappropriate.

Further, there are many active and popular games on Roblox using in-world drawing, some created more than five years ago:

* [Paint 'N Guess](https://www.roblox.com/games/256497097/Paint-N-Guess) (48M+ visits, created 6/2015).
* [Guess the drawing](https://www.roblox.com/games/3281073759/Guess-the-drawing) (37M+ visits, created 6/2019).
* [Free Draw 2](https://www.roblox.com/games/1547610457/Free-Draw-2) (47M+ visits, created 3/2018).

On these grounds we believe the metauni whiteboards are consistent with the Roblox rules.

## Are voice audio files consistent with the rules?

Yes, we believe so, although again if you read the Roblox rules strictly this is in a gray area. The Roblox Community rules state

> **Do not ask for or collect (or allow the transfer between players in your game) any personally identifiable information (PII)**. For example, you should not ask for a player’s first and last name, age, home or physical address, something that contains a person’s image or voice (such as a photograph, video or audio file), social security number, passport number (or national identity number), phone number or email address (or other forms of online contact information).

and on the Moderation Messages page you will find the following audio content message

> **"We're sorry, but audio featuring your voice or other personal information is not permitted on Roblox."** This is done for the safety of the user. Preventing personally identifiable information from being released is a top priority of Roblox.

These rules seem to be in place to prevent people from encouraging players (particular those under the age of 13) from uploading audio of their voice to Roblox and then sharing it. It doesn't seem to be targeted at developers, who might choose to put audio of voice actors into their games. Indeed many games on Roblox have audio content in their worlds produced by voice actors (and the Developer forums have many [ads for voice acting work](https://devforum.roblox.com/t/hiring-voice-actor-and-audio-editor-found/595917)). Some examples:

* [Q-clash](https://www.roblox.com/games/2029250188/Q-CLASH) (22M+ visits, created 1/2018).
* [Alone](https://www.roblox.com/games/2856821731/ALONE-Battle-Royale) (32M+ visits, created 2/2019).
* [ROSES](https://www.roblox.com/games/1064846716/ROSES) (1.6M+ visits, created 9/2017).

DM has uploaded around ten minutes of his own voiceovers to the Rising Sea node, without encountering any moderation messages.

## Quotes from the rules

An important passage from the Terms of Use:

> **Ownership of UGC and License Grant to Roblox.** For any UGC that you have ever Provided or that you will Provide (whether created solely by you or together with others) (a) between you and us or you and users, you retain all copyrights that you may hold in the UGC, and (b) in consideration of using the Service and the potential to earn Robux as discussed in the Robux section, you grant us a perpetual, irrevocable, worldwide, non-exclusive, royalty-free right and license (with the right to sublicense to any person or entity, whether a user of the Service or not) to host, store, transfer, publicly display, publicly perform (including by means of digital audio transmissions and on a through-to-the-audience basis), reproduce (including in timed synchronization to visual images), modify, create derivative works of, distribute, and use in any way the UGC that you Provide, in whole or in part, including modifications and derivative works, in any media or formats (tangible or intangible) and through any media, items or channels (online, offline, or others, now known or hereafter developed), including for publicity and marketing purposes (except that you are not granting us any license to make new or derivative video games using your UGC). 

Some important passages from the Community Rules:

> **Personal information.** We strongly encourage you to protect your personal information. In some cases (such as when you are under 13), we employ automated tools and other techniques so as to help comply with legal requirements concerning your personal information. In all cases, you are not allowed to share personal information of others, including through any comment or message posted on Group walls, private or public chats, forums or personal posts. Personal information includes: Full name; Email; Password; Home or other address; Telephone number; Social security, passport, or national identity number; Real life, personal, or family photos (these are not permitted to be uploaded for community safety); and other personally identifiable information.

> Certain trades are allowed through Roblox. (Found by clicking on "Trade" on the toolbar). No other method of trading is permitted on or off Roblox.

> Offsite website links, services, and additional 3rd party content are not permitted on Roblox with the following exceptions: YouTube, Twitter, Twitch. Users under the age of 13 are not permitted to share YouTube, Twitter, Twitch links for their privacy and safety. Permitted offsite links, content, or references must contain Roblox appropriate content or your account will be moderated up to immediate termination. Using partial links, filter-breaking, using permitted website links to indirectly link to non-permitted sites, content, or services, describing or otherwise encouraging users to go to unpermitted offsite links, content, or services is also not allowed.

> **Building your game.** When building your game, it’s important to do the following: Filter all chat and text. Developers must pass all chat and/or game text through Roblox’s filtering system. Roblox scans all chat communication and player inputted text for the safety of our users and legal compliance reasons, including the Children's Online Privacy Protection Act (COPPA). All chat and content must also be reportable through the Report Abuse system.

> Don’t build a game that encourages (or redirects) users to go off Roblox.

> **Do not ask for or collect (or allow the transfer between players in your game) any personally identifiable information (PII)**. For example, you should not ask for a player’s first and last name, age, home or physical address, something that contains a person’s image or voice (such as a photograph, video or audio file), social security number, passport number (or national identity number), phone number or email address (or other forms of online contact information).

> **Do not create promotions offering prizes of any sort (including contests, raffles, lotteries, chain letters or any kind of giveaway)**. It is okay to offer players promo codes for in-game items only so long as they are not in exchange for something (e.g., in exchange for a thumb up on your game).

> All text in uploaded images must be clearly visible to Roblox moderators. Images with tiny, unclear, or unreadable text will be blocked from upload.

