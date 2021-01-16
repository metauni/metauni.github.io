*The physical universe is a legacy platform.*

The Free University of the Metaverse (metauni) is a public network (like the World Wide Web) built out of [Roblox](https://www.roblox.com/) nodes (webpages) connected by teleports (links). It is free in the sense of [freedom](https://en.wikipedia.org/wiki/Free_University_of_Berlin). Roblox is a utility platform for persistent large-scale 3D social environments (see [Baszucki keynote](https://www.youtube.com/watch?v=G00GlCJc0mU)). It can be a [beautiful place](https://www.roblox.com/games/5326950832/Roblox-Realistic-Forest-Demo)! 

The purpose of this page: help others set up metauni nodes, coordinate the development of open source tools (e.g. for uploading preprints and talk slides) and host announcements of virtual events (sign up [here](http://tinyletter.com/adminmetauni) for the mailing list).

## Instructions

In its current iteration localised voice chat in metauni is based on [Discord](https://www.discord.com), a popular real-time communication platform. Currently the only active server on metauni is the Rising Sea. Here are instructions for visiting:

1. Create Roblox and Discord accounts.
2. Enter the Rising Sea [Discord channel](https://discord.gg/zg3K3NMK).
3. Register your Roblox username with `!register <username>`.
4. Manually enter any Discord voice channel (e.g. General).
5. Enter the [Rising Sea Roblox](https://www.roblox.com/games/6224932973/The-Rising-Sea).

You should notice almost transparent zones near floating white billboards or other points of interest. Those zones, when entered, will transition your Discord into an appropriate location-specific voice channel. Leaving the zone will not remove you from the channel, so feel free to take a walk and pick some apples...

## Setup

Here's how this is currently setup, so you can replicate it and make your own node.

The details: a Discord bot [running on Repl.it](https://repl.it/@dmurfet/MetaUni) `robloxvoicebot` translates information coming from a Discord webhook into the Discord API to move users between voice channels. Within the Roblox game a script detects `Touched` events when a player enters a zone, and triggers the webhook. The zones should be groups within a folder `Workspace > Zones`. Zones can contain multiple base parts, make each part `CanCollide = False` and you should probably make it large (i.e. so the Player's whole body enters the zone). You need to enable Http requests in Roblox Studio `Game Settings > Security`. You will need to make Discord voice channels with the same name as the regions, and make whatever channel the webhook is operating in private. Put `ZonesScript` into `ServerScriptService` where

```
local PlayerZones = {}
local Players = game:GetService("Players")

-- Attach Touched events to baseparts in each zone
-- based on https://developer.roblox.com/en-us/articles/detecting-collisions
-- and https://developer.roblox.com/en-us/api-reference/function/Players/GetPlayerFromCharacter
zones = game.Workspace.Zones:GetChildren()

for _,zone in pairs(zones) do
	for _,obj in pairs(zone:GetDescendants()) do
		if obj:IsA("BasePart") then
			obj.Touched:Connect(function(hit)
				local humanoid = hit.Parent:FindFirstChildWhichIsA("Humanoid")
				if humanoid then
					-- A player touched a zone
					
					local plr = Players:GetPlayerFromCharacter(hit.Parent)
					if plr then
						if PlayerZones[plr.Name] ~= zone.Name then
							PlayerZones[plr.Name] = zone.Name

							local HS = game:GetService("HttpService")
							local WebhookURL = "<your webhook URL here>"
							local MessageData = {
								["content"] = "MoverBot: "..plr.Name.." "..zone.Name
							}
							MessageData = HS:JSONEncode(MessageData)
							HS:PostAsync(WebhookURL,MessageData)
						end
					end
				end
			end)
		end
	end
end
```
