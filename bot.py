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
dmd_star = "https://i.imgur.com/1SuakAM.png"
gold_star = "https://i.imgur.com/Lv2cocr.png"

ad_servers = []
special_ad_servers = []
links = []
special_links = []

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
            if server.id in ad_servers or server.id in special_ad_servers:
                lvl = rndom.randint(0, 100)
                ad_1 = rndom.choice(links)
                ad_2 = rndom.choice(special_links)
                try:
                    channel = discord.utils.get(server.channels, name='servers')
                    if lvl >= 50:
                        await client.send_message(channel, "```diff\n+ <O> ADVERTISEMENT <O> +\n```\n \n{}".format(ad_1))
                        print("Advertised: {}".format(ad_1))
                    else:
                        msg = discord.Embed(colour=0xFF0000, description= "")
                        msg.title = ""
                        msg.set_footer(text=footer_text)
                        msg.set_image(url="{}".format(gold_star))
                        msg.add_field(name=":star2: ", value="```diff\n- >>>>>>>>>> SPECIAL SERVER <<<<<<<<<< -\n=================================\n--- ----------{o}---------- ---\n+ {}\n--- ----------{o}---------- ---\n=================================\n```\n \n{}".format(ad_2, ad_2))
                        await client.send_message(channel, embed=msg)
                        print("Advertised: {}".format(ad_2))
                except:
                    print("ERROR IN AUTO ADVERTISEMENT")
            else:
                print(".")
        print(".")
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
    msg += "\nad!force"
    msg += "\n   # Forces the bot to advertise. CREATOR ONLY."
    msg += "\nad!special <link>"
    msg += "\n   # Turns the given link to a special link. CREATOR ONLY."
    msg += "\nad!servers"
    msg += "\n   # Gives you a list of servers that are being advertised."
    msg += "\nad!random"
    msg += "\n   # Gives you a random server from the advertising list."
    msg += "\nad!test"
    msg += "\n   # Checks if everything is working like it should be."
    msg += "\nad!serverinfo"
    msg += "\n   # Gives you information about the server."
    msg += "\nad!invite"
    msg += "\n   # Gives you the invite link for the bot."
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
        if server.id in ad_servers or server.id in special_ad_servers:
            await client.say("This server is already being advertised!")
        else:
            await client.say("Starting...")
            try:
                channel = discord.utils.get(server.channels, name='servers')
                invite = await client.create_invite(destination = channel, xkcd = True, max_uses = 0)
                links.append(invite)
                ad_servers.append(server.id)
                await client.send_message(channel, "```fix\nTEST MESSAGE:\n \nLink used: {}\nServer: {}\nID: {}```".format(invite, server, server.id))
                await client.say("Added this server to the advertising list!")
                print(links)
                for srv in client.servers:
                    try:
                        chnl = discord.utils.get(srv.channels, name='servers')
                        await client.send_message(chnl, "```fix\nNEW SERVER:\n```\n{}".format(invite))
                    except:
                        print(".")
            except:
                await client.say("Error! Make sure you followed the steps in `ad!setup`. If you think this is a bug, please join the support server and DM <@412201413335056386>.")
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
    await client.say("Sliding in your DMs...")
    try:
        await client.send_message(author, "This is the support server for the bot: https://discord.gg/7BU8Uty Once you join, you can DM the owner ( <@412201413335056386> ) for any help.")
    except:
        await client.say("Error! Please check if the bot is allowed to DM you.")

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
                invite = await client.get_invite(args)
                server_id = invite.server.id
                server_name = invite.server.name
                special_links.append(args)
                special_ad_servers.append(server_id)
                await client.say("Added to special servers!\n```fix\nLink: {}\nServer: {}\nID: {}```".format(args, server_name, server_id))
                print("done")
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
                try:
                    channel = discord.utils.get(server.channels, name='servers')
                    msg = discord.Embed(colour=0xFF0000, description= "")
                    msg.title = ""
                    msg.set_footer(text=footer_text)
                    msg.set_image(url="{}".format(dmd_star))
                    msg.add_field(name=":loudspeaker: ", value="```md\n# >>>>>>>>>>{x}{X}{x}<<<<<<<<<< # \n[+](+)[+](+)[+](+)[+](+)[+](+)[+](+)[+]\n \n {} \n \nMessage by: {}\n \n[+](+)[+](+)[+](+)[+](+)[+](+)[+](+)[+]\n# >>>>>>>>>>{x}{X}{x}<<<<<<<<<< # \n```".format(args, author))
                    await client.send_message(channel, embed=msg)
                except:
                    print("ERROR IN AUTO ADVERTISEMENT")
            print(".")
                
    else:
        await client.say("This can only be used by the bot creator!")

# ad!force
@client.command(pass_context=True)
async def force(ctx):
    author = ctx.message.author
    if author.id == "412201413335056386":
        for server in client.servers:
            if server.id in ad_servers or server.id in special_ad_servers:
                lvl = rndom.randint(0, 100)
                ad_1 = rndom.choice(links)
                ad_2 = rndom.choice(special_links)
                try:
                    channel = discord.utils.get(server.channels, name='servers')
                    if lvl >= 50:
                        await client.send_message(channel, "```diff\n+ <O> ADVERTISEMENT <O> +\n```\n \n{}".format(ad_1))
                        print("Advertised: {}".format(ad_1))
                    else:
                        msg = discord.Embed(colour=0xFF0000, description= "")
                        msg.title = ""
                        msg.set_footer(text=footer_text)
                        msg.set_image(url="{}".format(gold_star))
                        msg.add_field(name=":star2: ", value="```diff\n- >>>>>>>>>> SPECIAL SERVER <<<<<<<<<< -\n=================================\n--- ----------{o}---------- ---\n+ {}\n--- ----------{o}---------- ---\n=================================\n```\n \n{}".format(ad_2, ad_2))
                        await client.send_message(channel, embed=msg)
                        print("Advertised: {}".format(ad_2))
                except:
                    print("ERROR IN AUTO ADVERTISEMENT")
            else:
                print(".")
    else:
        await client.say("This can only be used by the bot creator!")

# ad!servers
@client.command(pass_context=True)
async def servers(ctx):
    author = ctx.message.author
    srvlist = ""
    sp_srvlist = ""
    for server in client.servers:
        if server.id in special_ad_servers:
            sp_srvlist += "\n{} `-` {}".format(server, server.id)
        else:
            srvlist += "\n{} `-` {}".format(server, server.id)
    await client.say("Sliding in your DMs...")
    try:
        await client.send_message(author, "`SERVERS:`\n{}".format(srvlist))
        await client.send_message(author, "`SPECIAL SERVERS:`\n{}".format(sp_srvlist))
    except:
        await client.say("Error! Please check if the bot is allowed to DM you.")

# ad!random
@client.command(pass_context=True)
async def random(ctx):
    author = ctx.message.author
    await client.say("Sliding in your DMs...")
    try:
        await client.send_message(author, "`Random server:`\n{}".format(rndom.choice(links)))
    except:
        await client.say("Error! Either the bot cannot DM you or there are no links to select from.")

# ad!test
@client.command(pass_context=True)
async def test(ctx):
    author = ctx.message.author
    server = ctx.message.server
    await client.say("Testing...")
    try:
        channel = discord.utils.get(server.channels, name='servers')
        invite = await client.create_invite(destination = channel, xkcd = True, max_uses = 1)
        await client.send_message(channel, "```fix\nTEST MESSAGE:\n \nLink used: {}\nServer: {}\nID: {}```".format(invite, server, server.id))
        await client.say("All good! If there are any problems, please join the support server and DM <@412201413335056386>.")
    except:
        await client.say("Error! Make sure you followed all steps in `ad!setup`. If you think that this is a bug, pleace join the support server and DM <@412201413335056386>.")

# ad!invite
@client.command(pass_context=True)
async def invite(ctx):
    author = ctx.message.author
    server = ctx.message.server
    await client.say("Sliding to your DMs...")
    try:
        await client.send_message(author, "This is the link to invite the bot:\nhttps://discordapp.com/oauth2/authorize?client_id=432099205914427394&scope=bot&permissions=379921")
    except:
        await client.say("Error! Please check if the bot is allowed to DM you.")

# ad!serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    author = ctx.message.author
    server = ctx.message.server
    msg = discord.Embed(colour=0xFF0000, description= "")
    msg.title = ":page_with_curl: SERVER INFORMATION"
    msg.set_footer(text=footer_text)
    msg.add_field(name="MEMBERS", value=(len(ctx.message.server.members)), inline=True)
    msg.add_field(name="CHANNELS", value=(len(ctx.message.server.channels)), inline=True)
    msg.add_field(name="EMOJIS", value=(len(ctx.message.server.emojis)), inline=True)
    msg.add_field(name="ID", value=(ctx.message.server.id), inline=True)
    msg.add_field(name="REGION", value=(ctx.message.server.region), inline=True)
    msg.add_field(name="ROLES", value=(len(ctx.message.server.roles)), inline=True)
    msg.add_field(name="OWNER", value=(ctx.message.server.owner), inline=True)
    msg.add_field(name="CREATED AT", value=(ctx.message.server.created_at), inline=True)
    if server.id in special_ad_servers:
        msg.add_field(name="SPECIAL ADS:", value="True", inline=True)
    else:
        msg.add_field(name="SPECIAL ADS:", value="False", inline=True)
    await client.say(embed=msg)

# TURNS THE BOT ON
client.run(os.environ['BOT_TOKEN'])
