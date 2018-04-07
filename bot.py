import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random as rndom
import pickle
import os
import os.path
import requests
import json
import time
from gtts import gTTS

''''''

Client = discord.Client()
bot_prefix= "ad!"
client = commands.Bot(command_prefix=bot_prefix)
footer_text = "[+]Advertisement Bot[+]"

ad_servers = []
links = ["https://discord.gg/7BU8Uty"]
special_links = ["https://discord.gg/7BU8Uty"]
chance = ["1", "2", "3", "4", "5"]

# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    t1 = time.perf_counter()
    print("============================================================")
    print("ADVERTISEMENT BOT - LOGGED IN!")
    print("============================================================")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("============================================================")
    await client.change_presence(game=discord.Game(name='ad!help'))
    await client.wait_until_ready()
    t2 = time.perf_counter()
    print("Ping: {}".format(round((t2-t1)*1000)))
    print("============================================================")

# ADVERTISEMENT SYSTEM
async def advertisement():
    await client.wait_until_ready()
    while not client.is_closed:
        for server in client.servers:
            lvl = rndom.choice(chance)
            ad_1 = rndom.choice(links)
            ad_2 = rndom.choice(special_links)
            channel = discord.utils.get(server.channels, name='servers')
            if lvl == "1" or lvl == "2":
                await client.send_message(channel, "{}".format(ad_1))
                print("Advertised: {}".format(ad_1))
            else:
                await client.send_message(channel, "{}".format(ad_2))
                print("Advertised: {}".format(ad_2))
        await asyncio.sleep(900)

client.loop.create_task(advertisement())

# ad!help
client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    msg = "```cs"
    msg += "\nad!help"
    msg += "\n   # Gives you this list."
    msg += "\nad!setup [start]"
    msg += "\n   # Sets up the bot."
    msg += "\nad!ping"
    msg += "\n   # Pings the bot. Use this to check if the bot is lagging."
    msg += "\nad!support"
    msg += "\n   # Gives you the link to the support server."
    msg += "\nad!info"
    msg += "\n   # Gives you information about the bot."
    msg += "\nad!say <text>"
    msg += "\n   # Sends a message to all servers. CREATOR ONLY."
    msg += "\nad!force [-]"
    msg += "\n   # Forces the bot to advertise. CREATOR ONLY."
    msg += "\nad!special <link>"
    msg += "\n   # Turns the given link to a special link. CREATOR ONLY."
    msg += "\nad!servers"
    msg += "\n   # Gives you a list of servers that are being advertised."
    msg += "\nad!random"
    msg += "\n   # Gives you a random server from the advertising list."
    msg += "\nad!test"
    msg += "\n   # Checks if everything is working like it should be."
    msg += "\n```"
    await client.say(msg)

# ad!setup [start]
@client.command(pass_context=True)
async def setup(ctx, args = None):
    author = ctx.message.author
    server = ctx.message.server
    if args == None:
        msg = "```fix"
        msg += "\n- Create a channel called 'servers'."
        msg += "\n- Make sure the bot can read and send messages in that channel."
        msg += "\n- If you have an AD-Block, make sure to make an exception for the bot."
        msg += "\n- Do `ad!setup start`."
        msg += "\n- The bot should send a test message to the 'servers' channel."
        msg += "\n- If it doesn't then something went wrong."
        msg += "\n- You can use `ad!test` to check if everything is working like it should."
        msg += "\n- For any problems or help, please join the support server."
        msg += "\n```"
        await client.say(msg)
    elif args == "start":
        if server in ad_servers:
            await client.say("This server is already being advertised!")
        else:
            await client.say("Starting...\nIf I don't send a message after this, then something went wrong.")
            channel = discord.utils.get(server.channels, name='servers')
            invite = await client.create_invite(destination = channel, xkcd = True, max_uses = 0)
            links.append(invite)
            ad_servers.append(server)
            await client.send_message(channel, "```fix\nTEST MESSAGE:\n \nLink used: {}\nServer: {}\n```".format(invite, server))
            await client.say("Added this server to the advertising list!")
            print(links)
            for srv in client.servers:
                if srv.id == "414089074870321153":
                    chnl = discord.utils.get(srv.channels, name='servers')
                    await client.send_message(chnl, "```fix\nNEW SERVER:\n \n{}\n```".format(invite))
                else:
                    print(".")
            print(".")
    else:
        await client.say("Error: `ad!setup [start]`\n \nUse `ad!setup` for help and `ad!setup start` when you are ready to start the setup!")

# ad!ping
@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    await client.say("Pong! {}ms".format(round((t2-t1)*1000)))

# ad!support
@client.command(pass_context=True)
async def support(ctx):
    author = ctx.message.author
    await client.say("The support server link should be sent in your DMs. If it isn't, please check your profile settings.")
    await client.send_message(author, "This is the support server for the bot: https://discord.gg/7BU8Uty Once you join, you can DM the owner ( <@412201413335056386> ) for any help.")

# ad!info
@client.command(pass_context=True)
async def info(ctx):
    msg = "```fix"
    msg += "\nI'm in {} servers!".format(len(client.servers))
    msg += "\nAdvertising {} servers in total!".format(len(ad_servers))
    msg += "\nAdvertising {} normal links!".format(len(links))
    msg += "\nAdvertising {} special links!".format(len(links))
    msg += "\n```"
    await client.say(msg)

# ad!special <link>
@client.command(pass_context=True)
async def special(ctx, args = None):
    author = ctx.message.author
    if author.id == "412201413335056386":
        if args == None:
            await client.say("Error: `ad!special <link`")
        else:
            if args in special_links:
                await client.say("That link is already in the list!")
            else:
                special_links.append(args)
                await client.say("Added to special servers!")
                print(special)
    else:
        await client.say("This can only be used by the bot creator!")

# ad!say <text>
@client.command(pass_context=True)
async def say(ctx, *, args = None):
    author = ctx.message.author
    if author.id == "412201413335056386":
        if args == None:
            await client.say("Error: `ad!say <text>`")
        else:
            for server in client.servers:
                channel = discord.utils.get(server.channels, name='servers')
                await client.send_message(channel, "```fix\n----------[+][+][+]----------\n \n{}\n \n----------[+][+][+]----------\n```".format(args))
            print(".")
                
    else:
        await client.say("This can only be used by the bot creator!")

# ad!force [-]
@client.command(pass_context=True)
async def force(ctx, args = None):
    author = ctx.message.author
    if author.id == "412201413335056386":
        if args == None:
            for server in client.servers:
                lvl = rndom.choice(chance)
                ad_1 = rndom.choice(links)
                ad_2 = rndom.choice(special_links)
                channel = discord.utils.get(server.channels, name='servers')
                if lvl == "1" or lvl == "2":
                    await client.send_message(channel, "{}".format(ad_1))
                    print("Advertised: {}".format(ad_1))
                else:
                    await client.send_message(channel, "{}".format(ad_2))
                    print("Advertised: {}".format(ad_2))
        elif args == "-":
            for server in client.servers:
                ad_1 = rndom.choice(links)
                channel = discord.utils.get(server.channels, name='servers')
                await client.send_message(channel, "{}".format(ad_1))
        else:
            await client.say("Error: `ad!force [-]`")
    else:
        await client.say("This can only be used by the bot creator!")

# ad!servers
@client.command(pass_context=True)
async def servers(ctx):
    author = ctx.message.author
    await client.say("A list of servers should be sent to your DMs. If it isn't, please check your profile settings.")
    await client.send_message(author, "Normal links: {}".format(links))
    await client.send_message(author, "Special links: {}".format(special_links))

# ad!random
@client.command(pass_context=True)
async def random(ctx):
    author = ctx.message.author
    await client.say("A random server link should be sent to your DMs. If it isn't, please check your profile settings.")
    await client.send_message(author, "Random server: {}".format(rndom.choice(links)))

# ad!test
@client.command(pass_context=True)
async def test(ctx):
    author = ctx.message.author
    server = ctx.message.server
    await client.say("Testing... If I don't send another message after this one then something went wrong.")
    channel = discord.utils.get(server.channels, name='servers')
    invite = await client.create_invite(destination = channel, xkcd = True, max_uses = 1)
    await client.send_message(channel, "```fix\nTEST MESSAGE\n \n{}\n```".format(invite))
    await client.say("All good! If there are any problems, please join the support server and DM <@412201413335056386>.")

# TURNS THE BOT ON
client.run(os.environ['BOT_TOKEN'])
