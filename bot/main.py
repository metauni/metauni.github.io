# Discord.py API reference
# https://discordpy.readthedocs.io/en/latest/api.html
# bot tips https://github.com/AnIdiotsGuide/discordjs-bot-guide/blob/master/frequently-asked-questions.md
# Learned something from Moveer

import os
import pickle
import discord
import pymongo

from pymongo import MongoClient

from keep_alive import keep_alive
from discord.ext import commands
from discord import ChannelType

# The .env file contains database login credentials and bot id

# Set up database
# following https://towardsdatascience.com/creating-a-discord-bot-from-scratch-and-connecting-to-mongodb-828ad1c7c22e

cluster = MongoClient(
    "mongodb+srv://admin:" + os.environ.get("DATABASE_PASSWORD") +
    "@cluster0.frasl.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["discordroblox"]

discord_from_roblox = {}  # cache (avoiding database bug)

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = # YOUR DISCORD ID HERE


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


@bot.command()
async def register(ctx, arg):
    # Update the registration database
    # First see if this user has already registered
    registered = False
    myquery = {"_id": ctx.author.id}
    collection = db["discordroblox"]
    mydoc = collection.find(myquery)

    for x in mydoc:
        registered = True

    if registered:
        collection = db["discordroblox"]
        collection.update_one(myquery, {"$set": {"roblox_name": arg}})
        await ctx.send('Thanks for updating your Roblox Username!')
    else:
        # create a new entry
        post = {"_id": ctx.author.id, "roblox_name": arg}
        collection = db["discordroblox"]
        collection.insert_one(post)
        await ctx.send('Thanks for registering your Roblox Username!')

    discord_from_roblox[arg] = ctx.author.id


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    # https://stackoverflow.com/questions/56928396/how-to-make-a-bot-react-to-messages-under-a-certain-channel-with-a-certain-webh
    if (message.author.bot and message.content.find("MoverBot:") != -1):
        # I think that message.guild.members is broken
        # so we use a workaround looking for voice channel members

        # print("---- new message ----")
        channel_list = message.guild.voice_channels

        msg_split = message.content.split(" ")
        user_to_move = msg_split[1]
        channel_to_move = msg_split[2]

        discord_id = -1
        # print("discord from roblox")
        # print(discord_from_roblox)
        # print("")

        if user_to_move in discord_from_roblox:
            # use cached value
            discord_id = discord_from_roblox[user_to_move]
        else:
            # Run the query against the database
            myquery = {"roblox_name": user_to_move}
            collection = db["discordroblox"]
            mydoc = collection.find(myquery)

            for x in mydoc:
                # print(x)
                if '_id' in x:
                    discord_id = x['_id']

        # print("got discord ID")
        # print(discord_id)

        if discord_id != -1:
            # Move the user to the designated channel
            founduser = False
            foundchannel = False

            for c in channel_list:
                # print("c = " + c.name)
                if (c.name == channel_to_move):
                    foundchannel = True
                    channel = c

                # print(c.name)
                # print(c.members)
                # print("")

                for u in c.members:
                    if (u.id == discord_id):
                        founduser = True
                        user = u

            if (founduser and foundchannel):
                # print("moving user " + str(u.id) + " to " + c.name)
                await user.move_to(channel)


keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)  # Starts the bot
