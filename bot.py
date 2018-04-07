import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
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
            chance = random.randint(0, 100)
            ad_1 = random.choice(links)
            ad_2 = random.choice(special_links)
            channel = discord.utils.get(server.channels, name='servers')
            if chance <= 60:
                await client.send_message(channel, "{}".format(ad_2))
                print("Advertised: {}".format(ad_2))
            else:
                await client.send_message(channel, "{}".format(ad_1))
                print("Advertised: {}".format(ad_1))
        await asyncio.sleep(900)
    
client.loop.create_task(advertisement())

# ad!help
client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    await client.say("`List of commands:`\n \n`ad!help - Shows this message.`\n`ad!setup - Adds your server to the advertising list if it isn't added yet.`\n`ad!ping - Use this to check if the bot is online.`\n`ad!support - Gives you the link for the support server.`")
    await client.say("`Use ad!setup to add your server to the advertising list!`")
    await client.say("`If join the support server ( ad!support ) you can get your server in the special links. Special servers have a higher chance of being advertised.`")

# ad!setup
@client.command(pass_context=True)
async def setup(ctx):
    author = ctx.message.author
    server = ctx.message.server
    await client.say("`Please make a channel called 'servers' before using this command! If you do not get another message after this one then something went wrong.`")
    channel = discord.utils.get(server.channels, name='servers')
    invite = await client.create_invite(destination = channel, xkcd = True, max_uses = 0)
    if server in ad_servers:
        await client.say("`This server is already being advertised!`")
    else:
        links.append(invite)
        ad_servers.append(server)
        await client.say("`Added this server to the advertising list!`")
        print(links)

# ad!ping
@client.command(pass_context=True)
async def ping(ctx):
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    await client.say("`Pong! {}ms`".format(round((t2-t1)*1000)))

# ad!support
@client.command(pass_context=True)
async def support(ctx):
    author = ctx.message.author
    await client.send_message(author, "`This is the support server for the bot:` https://discord.gg/7BU8Uty `Once you join, you can DM the owner ( `<@412201413335056386>` ) for any help.`")

# ad!special <link>
@client.command(pass_context=True)
async def special(ctx, args = None):
    author = ctx.message.author
    if args == None:
        await client.say("`Error!`")
    else:
        if author.id == "412201413335056386":
            if args in special_links:
                await client.say("`That link is already in the list!`")
            else:
                special_links.append(args)
                await client.say("`Added to special servers!`")
                print(special)
        else:
            await client.say("`This can only be used by the bot creator!`")

# ad!info
@client.command(pass_context=True)
async def info(ctx):
    await client.say("```fix\nI'm currently in {} servers!\nAdvertising on {} servers!\nAdvertising {} links!\nAdvertising {} special links!\n```".format(len(client.servers), len(ad_servers), len(links), len(special_links)))

# TURNS THE BOT ON
client.run(os.environ['BOT_TOKEN'])
