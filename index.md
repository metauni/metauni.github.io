# Free University of the Metaverse

The Free University is on Roblox, a utility platform for persistent large-scale 3D social environments (see [Baszucki keynote](https://www.youtube.com/watch?v=G00GlCJc0mU)). It is free in the sense of [freedom](https://en.wikipedia.org/wiki/Free_University_of_Berlin). In its current iteration localised voice chat is based on [Discord](https://www.discord.com), a popular real-time communication platform.

## Instructions

1. Create Roblox and Discord accounts.
2. Enter the Rising Sea [Discord channel](https://discord.gg/zg3K3NMK).
3. Register your Roblox username with `!register <username>`.
4. Manually enter any Discord voice channel (e.g. General).
5. Enter the [Rising Sea Roblox](https://www.roblox.com/games/6224932973/The-Rising-Sea).

You should notice transparent volumes around floating white billboards (currently abstracts of papers, or lecture notes). Those volumes, when touched, will transition your Discord into an appropriate location-specific voice channel. Leaving the volume will not leave the channel (you can manually reset to General, or use the reset volume near your spawn point) so you can take a walk together and enjoy the view...

## Setup

Here's how this is currently setup, if you want to replicate it.

A Discord bot (running on Repl.it) `robloxvoicebot` translates information coming from a Discord webhook into the Discord API to move users between voice channels. Within the Roblox game scripts detect Touched events when a player enters a zone, and triggers the webhook. The zones should be groups within a folder `Workspace > Zones`. Zones can contain multiple base parts, make each part `CanCollide = False` and you should probably make it large (i.e. so the Player's whole body enters the zone). You need ot enable Http requests in Roblox Studio `Game Settings > Security`. You will need to make Discord voice channels with the same name as the regions, and make whatever channel the webhook is operating in private. Put `ZonesScript` into `ServerScriptService` where

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
