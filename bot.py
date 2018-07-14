print("Starting...")
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
import time
import re

''''''

Client = discord.Client()
bot_prefix= "ad!"
client = commands.Bot(command_prefix=bot_prefix)
footer_text = "[+] Get Advertiser Bot: https://discord.gg/UBh9FpK [+]"

help_msg1 = "```diff"
help_msg1 += "\n- COMMANDS FOR EVERYONE -"
help_msg1 += "\nad!help\n+ Gives you a list of commands."
help_msg1 += "\nad!ping\n+ Pings the bot. Used to check if the bot is lagging."
help_msg1 += "\nad!support <message>\n+ Sends a message to the bot's staff. Use this if you need any help or have questions."
help_msg1 += "\nad!info\n+ Shows information about the bot."
help_msg1 += "\nad!rnd\n+ Gives you a random server."
help_msg1 += "\nad!serverinfo [server id]\n+ Shows information about a server."
help_msg1 += "\nad!invite\n+ Gives you the invite link for the bot."
help_msg1 += "\nad!tos\n+ Gives you bot's rules and TOS."
help_msg1 += "\nad!suggest <suggestion>\n+ Sends a suggestion to the bot moderators."
help_msg1 += "\nad!uptime\n+ Shows you how long the bot's been online for."
help_msg1 += "\nad!report <user/server> <id> <reason>\n+ Reports a server or user to the bot moderators."
help_msg1 += "\nad!bug <message>\n+ Reports a bug to the bot moderators."
help_msg1 += "\nad!bump\n+ Forces the bot to advertise the server which the command is run in. This can only be used once every day."
help_msg1 += "\n```"

help_msg2 = "```diff"
help_msg2 += "\n- COMMANDS FOR SERVER MANAGERS -"
help_msg2 += "\nad!setup [log channel] [channel] [message]\n+ Shows you help on how to setup your server or starts the setup if you add the arguments."
help_msg2 += "\nad!unsetup\n+ Removes your server from all lists and deletes all data required to advertise your server."
help_msg2 += "\nad!test\n+ Checks if your server is setup correctly."
help_msg2 += "\nad!scan\n+ Bans users who are on the black list. Those users are most likely banned for harming servers or breaking the discord TOS."
help_msg2 += "\nad!toggle\n+ Toggles advertise mode on or off for your server."
help_msg2 += "\n```"

help_msg3 = "```diff"
help_msg3 += "\n- COMMANDS FOR BOT MODERATORS -"
help_msg3 += "\nad!msg <user/server> <id> <message>\n+ DMs an user or the owner of the specified server."
help_msg3 += "\nad!ban <user/server> <id> <reason>\n+ Bans an user from all servers or prevents a server from using the bot."
help_msg3 += "\nad!unban <user/server> <id>\n+ Unbans an user from all servers or gives access to a server that was banned."
help_msg3 += "\nad!reset <server id>\n+ Removes a server from all lists."
help_msg3 += "\n```"

help_msg4 = "```diff"
help_msg4 += "\n- COMMANDS FOR BOT ADMINISTRATORS -"
help_msg4 += "\nad!mod <add/del> <user>\n+ Adds or removes a bot moderator."
help_msg4 += "\nad!fbump <server id>\n+ Forces the bot to advertise the server with the matching ID as the one specified."
help_msg4 += "\nad!announce <text>\n+ Sends an announcement to all servers."
help_msg4 += "\nad!force\n+ Forces the bot to advertise."
help_msg4 += "\nad!log <message>\n+ Logs a message."
help_msg4 += "\nad!special <add/del> <server id>\n+ Adds or removes a server from the special list."
help_msg4 += "\nad!say <text>\n+ Forces the bot to say something."
help_msg4 += "\n```"

tos_msg = "**__By using this bot you agree to the following:__**"
tos_msg += "\n**~~=~~** Letting the bot ban and unban users that are known for harming other discord servers and/or breaking the discord TOS!"
tos_msg += "\n**~~=~~** Letting the bot create invite linnks for your server!"
tos_msg += "\n**~~=~~** Letting the bot send advertisements for other discord servers on your server and sending your server links to other servers!"
tos_msg += "\n**~~=~~** Giving the required permissions to the bot!"
tos_msg += "\n**~~=~~** Letting the bot get your server information such as members, server id, channel count, owner id etc!"
tos_msg += "\n "
tos_msg += "\n**__Bot rules:__**"
tos_msg += "\n**~~=~~** Everyone must be able to see the channel that the bot creates!"
tos_msg += "\n**~~=~~** Spamming bot commands or trying to make the bot lag is not allowed!"
tos_msg += "\n**~~=~~** Asking to become a bot moderator is not allowed!"
tos_msg += "\n**~~=~~** Only DM the bot administrators or bot moderators if you have any questions or if you need help!"
tos_msg += "\n**~~=~~** Do not send stupid suggestions!"
tos_msg += "\n**~~=~~** Do not false report users, servers and/or bugs!"
tos_msg += "\n**~~=~~** Breaking any of these rules will get you and/or your server banned!"
tos_msg += "\n "
tos_msg += "\n**__You can use `ad!help` to see a list of commands!__**"

test_msg_img = "https://i.imgur.com/3zHcRpt.png"
announcement_img = "https://i.imgur.com/2m9gzUm.png"
new_server_img = "https://i.imgur.com/79FgWOd.png"
special_server_img = "https://i.imgur.com/G5SWYtL.png"
random_servers_chnl = '450625326943436800'
console_chnl = '450625267413680148'
logs_chnl = '450625284664983562'
reports_users_chnl = '450625233913774080'
reports_servers_chnl = '450625596943499264'
reports_bugs_chnl = '450625543495221248'
suggestions_chnl = '450625186245378058'
banned_users_chnl = '450625846047145986'
banned_servers_chnl = '450625869233258497'
bot_mods_chnl = '450626647021060097'
bot_admins_chnl = '450626670852833280'
toggled_servers_chnl = '450627295108136971'
special_servers_chnl = '450627929345622016'
normal_servers_chnl = '450648126471143424'
channels_chnl = '450648284264923146'
log_channels_chnl = '451405759020793856'
normal_servers_msgs_chnl = '450648203612913664'
special_servers_msgs_chnl = '450648244138278933'
servers_links_chnl = '450960502831710208'
support_server = '440108166789988353'
community_server = 'https://discord.gg/UBh9FpK'
error_img = '<:erroremoji:451339882669801482>'
x_img = '<:xmark:314349398824058880>'
check_img = '<:check:314349398811475968>'
owner_id = '412201413335056386'
start_status = '- ad!help | ad!support'
loading_status = '- Loading...'
updating_status = '- Updating...'
support_chnl = '453133652029865995'

servers_links = []

normal_servers = []
special_servers = []

normal_servers_msgs = []
special_servers_msgs = []

channels_ids = ['450625326943436800']
log_channels_ids = ['450625284664983562']

banned_users = []
banned_servers = []
toggled_servers = []
bumped_servers = []

bot_mods = ['412201413335056386']
bot_admins = ['412201413335056386']

ut_seconds = []
ut_minutes = []
ut_hours = []

# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=loading_status), status='dnd')
    limit = 100000
    ns = client.get_channel(normal_servers_chnl)
    ss = client.get_channel(special_servers_chnl)
    nsm = client.get_channel(normal_servers_msgs_chnl)
    ssm = client.get_channel(special_servers_msgs_chnl)
    ci = client.get_channel(channels_chnl)
    bu = client.get_channel(banned_users_chnl)
    bs = client.get_channel(banned_servers_chnl)
    ts = client.get_channel(toggled_servers_chnl)
    bm = client.get_channel(bot_mods_chnl)
    ba = client.get_channel(bot_admins_chnl)
    c = client.get_channel(console_chnl)
    sl = client.get_channel(servers_links_chnl)
    lc = client.get_channel(log_channels_chnl)
    msg = "```diff"
    msg += "\n- LOGGED IN -"
    msg += "\n+ Name: {}".format(client.user.name)
    msg += "\n+ ID: {}".format(client.user.id)
    msg += "\n+ Total server count: {}".format(len(client.servers))
    async for message in client.logs_from(ns, limit=limit):
        normal_servers.append(message.content)
        print("[START UP][NORMAL SERVERS] ADDED {}".format(message.content))
    msg += "\n+ Normal server count: {}".format(len(normal_servers))
    async for message in client.logs_from(ss, limit=limit):
        special_servers.append(message.content)
        print("[START UP][SPECIAL SERVERS] ADDED {}".format(message.content))
    msg += "\n+ Special server count: {}".format(len(special_servers))
    async for message in client.logs_from(nsm, limit=limit):
        normal_servers_msgs.append(message.content)
        print("[START UP][NORMAL SERVERS MESSAGES] ADDED {}".format(len(normal_servers_msgs)))
    msg += "\n+ Normal message count: {}".format(len(normal_servers_msgs))
    async for message in client.logs_from(ssm, limit=limit):
        special_servers_msgs.append(message.content)
        print("[START UP][SPECIAL SERVERS MESSAGES] ADDED {}".format(len(special_servers_msgs)))
    msg += "\n+ Special message count: {}".format(len(special_servers_msgs))
    async for message in client.logs_from(ts, limit=limit):
        toggled_servers.append(message.content)
        print("[START UP][TOGGLED SERVERS] ADDED {}".format(message.content))
    msg += "\n+ Toggled server count: {}".format(len(toggled_servers))
    async for message in client.logs_from(sl, limit=limit):
        servers_links.append(message.content)
        print("[START UP][SERVERS LINKS] ADDED {}".format(message.content))
    msg += "\n+ Total link count: {}".format(len(servers_links))
    async for message in client.logs_from(ci, limit=limit):
        channels_ids.append(message.content)
        print("[START UP][CHANNELS IDS] ADDED {}".format(message.content))
    msg += "\n+ Total channel count: {}".format(len(channels_ids))
    async for message in client.logs_from(lc, limit=limit):
        log_channels_ids.append(message.content)
        print("[START UP][LOG CHANNELS IDS] ADDED {}".format(message.content))
    msg += "\n+ Total log channel count: {}".format(len(log_channels_ids))
    async for message in client.logs_from(bs, limit=limit):
        banned_servers.append(message.content)
        print("[START UP][BANNED SERVERS] ADDED {}".format(message.content))
    msg += "\n+ Banned server count: {}".format(len(banned_users))
    async for message in client.logs_from(bu, limit=limit):
        banned_users.append(message.content)
        print("[START UP][BANNED USERS] ADDED {}".format(message.content))
    msg += "\n+ Banned user count: {}".format(len(banned_servers))
    async for message in client.logs_from(bm, limit=limit):
        bot_mods.append(message.content)
        print("[START UP][BOT MODERATORS] ADDED {}".format(message.content))
    msg += "\n+ Bot moderator count: {}".format(len(bot_mods))
    async for message in client.logs_from(ba, limit=limit):
        bot_admins.append(message.content)
        print("[START UP][BOT ADMINISTRATORS] ADDED {}".format(message.content))
    msg += "\n+ Bot administrator count: {}".format(len(bot_admins))
    t1 = time.perf_counter()
    await client.send_typing(c)
    t2 = time.perf_counter()
    msg += "\n+ Ping: {} ms".format(round((t2-t1)*1000))
    msg += "\n```"
    await client.send_message(c, msg)
    await client.wait_until_ready()
    await client.change_presence(game=discord.Game(name=start_status))
    print("==========")
    print("==========")
    print("==========")
    print("BOT LOGGED IN")
    print("==========")
    print("==========")
    print("==========")

# SERVER COUNT
@client.event
async def on_server_join(server):
    c_chnl = client.get_channel(console_chnl)
    await client.send_message(c_chnl, "```diff\n- JOINED SERVER -\n+ Name: {}\n+ ID: {}\n```".format(server.name, server.id))
    try:
        await client.send_message(server.owner, "Thank you for adding this bot to your server. Below you can see the TOS and bot rules. For any help you can use: `ad!help` and `ad!support`. :grin: ")
        await client.send_message(server.owner, tos_msg)
    except:
        print("")

@client.event
async def on_server_remove(server):
    await client.wait_until_ready()
    c_chnl = client.get_channel(console_chnl)
    await client.send_message(c_chnl, "```diff\n- LEFT SERVER -\n+ Name: {}\n+ ID: {}\n```".format(server.name, server.id))
    if server.id in normal_servers or special_servers:
        nsm = client.get_channel(normal_servers_msgs_chnl)
        ssm = client.get_channel(special_servers_msgs_chnl)
        ns = client.get_channel(normal_servers_chnl)
        ss = client.get_channel(special_servers_chnl)
        sl = client.get_channel(servers_links_chnl)
        try:
            o = []
            for i in server_links:
                a = await client.get_invite(i)
                s = a.server.id
                if s == server.id:
                    servers_links.remove(i)
                    o.append(i)
                    print("REMOVED INVITE")
                    break
                else:
                    print("")
            async for m in client.logs_from(sl):
                if m.content == o[0]:
                    await client.delete_message(m)
                    print("REMOVED INVITE 2")
                    break
                else:
                    print("")
        except:
            print("")
        async for m in client.logs_from(nsm):
            a = str(m.content)
            if server.id in a:
                await client.delete_message(m)
                print("REMOVED MSG")
                break
            else:
                print("")
        for i in normal_servers_msgs:
            a = str(i)
            if server.id in a:
                normal_servers_msgs.remove(i)
                print("REMOVED MSG 2")
                break
            else:
                print("")
        async for m in client.logs_from(ssm):
            a = str(m.content)
            if server.id in a:
                await client.delete_message(m)
                print("REMOVED SPEC MSG")
                break
            else:
                print("")
        for i in special_servers_msgs:
            a = str(i)
            if server.id in a:
                special_servers_msgs.remove(i)
                print("REMOVED SPEC MSG 2")
                break
            else:
                print("")
        async for m in client.logs_from(ns):
            a = str(m.content)
            if server.id in a:
                await client.delete_message(m)
                print("REMOVED ID")
                break
            else:
                print("")
        try:
            normal_servers.remove(server.id)
            print("REMOVED ID 2")
        except:
            print("")
        async for m in client.logs_from(ss):
            a = str(m.content)
            if server.id in a:
                await client.delete_message(m)
                print("REMOVED SPEC ID")
                break
            else:
                print("")
        try:
            special_servers.remove(server.id)
            print("REMOVED SPEC ID 2")
        except:
            print("")
    else:
        print("")
    print("FINISHED")

# AUTO ADVERTISING SYSTEM
async def autoad():
    await client.wait_until_ready()
    while not client.is_closed:
        try:
            total = []
            normal = []
            special = []
            fail = []
            cnsl = client.get_channel(console_chnl)
            ss = []
            ns = []
            a_s = []
            cs = []
            for s in client.servers:
                if s.id in banned_servers:
                    print("[AUTO AD] SERVER IS BANNED")
                elif s.id in toggled_servers:
                    print("[AUTO AD] SERVER IS TOGGLED")
                elif s.id in special_servers:
                    ss.append(s.id)
                    a_s.append(s.id)
                    print("[AUTO AD] SERVER FOUND (S)")
                elif s.id in normal_servers:
                    ns.append(s.id)
                    a_s.append(s.id)
                    print("[AUTO AD] SERVER FOUND (N)")
                else:
                    print("[AUTO AD] SERVER NOT FOUND IN ANY LISTS")
            print("[AUTO AD INFO]\nnormal servers: {}\nspecial servers: {}\nall servers: {}".format(ns, ss, a_s))
            for c in channels_ids:
                try:
                    c1 = client.get_channel(c)
                    for srv in client.servers:
                        if srv in toggled_servers:
                            if c1 in srv.channels:
                                print("[AUTO AD] CHANNEL IS TOGGLED")
                            else:
                                cs.append(c)
                                print("[AUTO AD] CHANNEL FOUND")
                        else:
                            if c1 in srv.channels:
                                cs.append(c)
                                print("[AUTO AD] CHANNEL FOUND")
                            else:
                                print("[AUTO AD] CHANNEL NOT FOUND")
                except:
                    print("[AUTO AD] FAILED TO GET CHANNEL")
            print("[AUTO AD INFO]\nchannels: {}".format(cs))
            for c in cs:
                try:
                    chnl = client.get_channel(c)
                    co = random.choice(a_s)
                    if co in ss:
                        print("[AUTO AD] CHOICE: S")
                        m = random.choice(special_servers_msgs)
                        embed = discord.Embed(colour=0xFFAE00, description= "")
                        embed.title = ""
                        embed.set_image(url="{}".format(special_server_img))
                        embed.set_footer(text=footer_text)
                        embed.add_field(name="special advertisement", value="{}".format(m))
                        print("[AUTO AD] MESSAGE CREATED")
                    else:
                        print("[AUTO AD] CHOICE: N")
                        m = random.choice(normal_servers_msgs)
                        embed = discord.Embed(colour=0x00FFFF, description= "")
                        embed.title = ""
                        embed.set_footer(text=footer_text)
                        embed.add_field(name="advertisement", value="{}".format(m))
                        print("[AUTO AD] MESSAGE CREATED")
                    try:
                        await client.send_message(chnl, embed=embed)
                        print("[AUTO AD] SENT")
                        if co in ss:
                            special.append("+1")
                        else:
                            normal.append("+1")
                        total.append("+1")
                    except:
                        fail.append("+1")
                except:
                    print("[AUTO AD ERRORS] MAIN")
            log = "```diff"
            log += "\n- AUTO ADVERTISEMENT -"
            log += "\n+ Total sent: {}".format(len(total))
            log += "\n+ Failed: {}".format(len(fail))
            log += "\n+ Normal sent: {}".format(len(normal))
            log += "\n+ Special sent: {}".format(len(special))
            log += "\n```"
            await client.send_message(cnsl, log)
            print("[AUTO AD] FINISHED")
        except:
            print("[AUTO AD ERRORS] GLOBAL")
        await asyncio.sleep(1200)

client.loop.create_task(autoad())
        
# UPTIME SYSTEM
async def uptime_system():
    await client.wait_until_ready()
    while not client.is_closed:
        if len(ut_minutes) == 60:
            ut_minutes.clear()
            ut_hours.append("+1")
        elif len(ut_seconds) == 60:
            ut_seconds.clear()
            ut_minutes.append("+1")
        else:
            ut_seconds.append("+1")
        await asyncio.sleep(1)

client.loop.create_task(uptime_system())

''' COMMANDS FOR EVERYONE '''
# ad!help
client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    try:
        await client.send_message(author, help_msg1)
        await client.send_message(author, help_msg2)
        await client.send_message(author, help_msg3)
        await client.send_message(author, help_msg4)
        await client.say("Check your DMs. :slight_smile: ")
    except:
        await client.say("<:erroremoji:451339882669801482> Make sure the bot has permissions to send you DMs!")

# ad!ping
@client.command(pass_context=True)
async def ping(ctx):
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    else:
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        ping = round((t2-t1)*1000)
        msg = "My ping is: `{}ms`".format(ping)
        if ping > 300:
            msg += "\nThe bot is lagging! <:dnd:313956276893646850>"
        elif ping > 200:
            msg += "\nThe bot might be lagging! <:away:313956277220802560>"
        else:
            msg += "\nThe bot isn't lagging! <:online:313956277808005120>"
        await client.say(msg)

# ad!support <message>
@client.command(pass_context=True)
async def support(ctx, *, args = None):
    author = ctx.message.author
    server = ctx.message.server
    chnl = client.get_channel(support_chnl)
    if args == None:
        await client.say("{} No message given!\nExample: `ad!support I need help with setting up the bot.`.\nThe message cannot be longer than 1000 characters.".format(error_img))
    else:
        if len(str(args)) > 1000:
            await client.say("{} The message cannot be longer than 1000 characters.".format(error_img))
        else:
            await client.say("Sending... <a:typing:393848431413559296>")
            msg = "@everyone "
            msg += "```diff"
            msg += "\n- SUPPORT -"
            msg += "\n+ Author: {} ### {}".format(author, author.id)
            msg += "\n+ From: {} ### {}".format(server.name, server.id)
            msg += "\n+ Message:"
            msg += "\n```"
            msg += "\n{}".format(args)
            await client.send_message(chnl, msg)
            await client.say("{} Message sent!".format(check_img))
            try:
                await client.send_message(author, "{} The support ticket has been sent to the bot's staff. They will reply using this DM once they see the support ticket.".format(check_img))
            except:
                await client.say("{} Make sure the bot can send you DMs!".format(error_img))

# ad!info
@client.command(pass_context=True)
async def info(ctx):
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    else:
        big = []
        await client.say("Collecting information... <a:updating:403035325242540032>")
        msg = "```diff"
        msg += "\n- INFORMATION ABOUT THE BOT -"
        msg += "\n+ Total server count: {}".format(len(client.servers))
        for server in client.servers:
            if len(server.members) >= 750:
                big.append("+1")
            else:
                print("")
        msg += "\n+ Big server count: {}".format(len(big))
        msg += "\n+ Banned server count: {}".format(len(banned_servers))
        msg += "\n+ Banned user count: {}".format(len(banned_users))
        msg += "\n+ Advertising server count: {}".format(len(normal_servers) + len(special_servers))
        msg += "\n+ Advertising special server count: {}".format(len(special_servers))
        msg += "\n+ Total link count: {}".format(len(servers_links))
        msg += "\n+ Toggled server count: {}".format(len(toggled_servers))
        msg += "\n+ Bot's uptime: {}hours {}minutes {}seconds".format(len(ut_hours), len(ut_minutes), len(ut_seconds))
        msg += "\n+ Bot creator's ID: {}".format(owner_id)
        msg += "\n+ Community server link:\n```\n{}".format(community_server)
        await client.say(msg)

# ad!rnd
@client.command(pass_context=True)
async def rnd(ctx):
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    else:
        await client.say("**Random server:**\n{}".format(random.choice(servers_links)))

# ad!serverinfo [server id]
@client.command(pass_context=True)
async def serverinfo(ctx, target = None):
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    else:
        if target == None:
            await client.say("Collecting information... <a:updating:403035325242540032>")
            try:
                server = ctx.message.server
                msg = "```diff"
                msg += "\n- INFORMATION ABOUT {} -".format(server.name)
                msg += "\n+ Members: {}".format(len(server.members))
                msg += "\n+ Region: {}".format(server.region)
                msg += "\n+ ID: {}".format(server.id)
                msg += "\n+ Owner: {} ### {}".format(server.owner, server.owner.id)
                msg += "\n+ Created at: {}".format(server.created_at)
                if server.id in special_servers:
                    msg += "\n+ Special ADs: True"
                else:
                    msg += "\n+ Special ADs: False"
                if server.id in toggled_servers:
                    msg += "\n+ Toggled: True"
                else:
                    msg += "\n+ Toggled: False"
                if server.id in banned_servers:
                    msg += "\n+ Banned: True"
                else:
                    msg += "\n+ Banned: False"
                if server.id in normal_servers or server.id in special_servers:
                    msg += "\n+ Setup: True"
                else:
                    msg += "\n+ Setup: False"
                msg += "\n```"
                await client.say(msg)
            except:
                await client.say("<:erroremoji:451339882669801482> Error in collecting information!\nMake sure the bot has the required permissions.")
        else:
            found = []
            await client.say("Searching for server...")
            for server in client.servers:
                if server.id == target:
                    found.append("+1")
            if len(found) == 0:
                await client.say("<:erroremoji:451339882669801482> Server not found!\nEither the bot is not in that server or the server doesn't exist.")
            else:
                try:
                    server = client.get_server(target)
                    await client.say("Server found!\nCollecting information... <a:updating:403035325242540032>")
                    try:
                        msg = "```diff"
                        msg += "\n- INFORMATION ABOUT {} -".format(server.name)
                        msg += "\n+ Members: {}".format(len(server.members))
                        msg += "\n+ Region: {}".format(server.region)
                        msg += "\n+ ID: {}".format(server.id)
                        msg += "\n+ Owner: {} ### {}".format(server.owner, server.owner.id)
                        msg += "\n+ Created at: {}".format(server.created_at)
                        if server.id in special_servers:
                            msg += "\n+ Special ADs: True"
                        else:
                            msg += "\n+ Special ADs: False"
                        if server.id in toggled_servers:
                            msg += "\n+ Toggled: True"
                        else:
                            msg += "\n+ Toggled: False"
                        if server.id in banned_servers:
                            msg += "\n+ Banned: True"
                        else:
                            msg += "\n+ Banned: False"
                        if server.id in normal_servers or server.id in special_servers:
                            msg += "\n+ Setup: True"
                        else:
                            msg += "\n+ Setup: False"
                        msg += "\n```"
                        await client.say(msg)
                    except:
                        await client.say("<:erroremoji:451339882669801482> Error in collecting information!\nThe bot may not have the required permissions in that server.")
                except:
                    await client.say("<:erroremoji:451339882669801482> An unknown error occured while trying to collect the information for that server.")

# ad!invite
@client.command(pass_context=True)
async def invite(ctx):
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    else:
        await client.say("Here is the link to invite the bot:\n \nhttps://discordapp.com/oauth2/authorize?client_id=439051827384680449&scope=bot&permissions=537259127")

# ad!tos
@client.command(pass_context=True)
async def tos(ctx):
    await client.say(tos_msg)

# ad!suggest <suggestion>
@client.command(pass_context=True)
async def suggest(ctx, *, args = None):
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    else:
        author = ctx.message.author
        server = ctx.message.server
        if args == None:
            await client.say("{} No suggestion given.".format(error_img))
        else:
            if len(str(args)) > 1000:
                await client.say("{} The suggestion cannot be longer than 1000 characters.".format(error_img))
            else:
                await client.say("Sending suggestion... <a:typing:393848431413559296>")
                try:
                    chnl = client.get_channel(suggestions_chnl)
                    msg = "```diff"
                    msg += "\n- SUGGESTION -"
                    msg += "\n+ Author: {} ### {}".format(author, author.id)
                    msg += "\n+ From: {} ### {}".format(server.name, server.id)
                    msg += "\n+ Suggestion:"
                    msg += "\n```"
                    msg += "\n{}".format(args)
                    await client.send_message(chnl, msg)
                    await client.say("<:check:314349398811475968> Suggestion sent!")
                except:
                    await client.say("{} Error in sending suggestion.".format(error_img))

# ad!uptime
@client.command(pass_context=True)
async def uptime(ctx):
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    else:
        nr_hours = 23 - len(ut_hours)
        nr_minutes = 59 - len(ut_minutes)
        nr_seconds = 59 - len(ut_seconds)
        msg = "```diff"
        msg += "\n- UP TIME -"
        msg += "\n+ {} hour(s)".format(len(ut_hours))
        msg += "\n+ {} minute(s)".format(len(ut_minutes))
        msg += "\n+ {} second(s)".format(len(ut_seconds))
        msg += "\n```"
        msg += "\n```diff"
        msg += "\n- NEXT AUTO-RESTART IN -"
        msg += "\n+ {} hour(s)".format(nr_hours)
        msg += "\n+ {} minute(s)".format(nr_minutes)
        msg += "\n+ {} second(s)".format(nr_seconds)
        msg += "\n```"
        await client.say(msg)

# ad!report <user/server> <id> <reason>
@client.command(pass_context=True)
async def report(ctx, option = None, target = None, *, reason = None):
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    else:
        author = ctx.message.author
        server = ctx.message.server
        if option == None:
            await client.say("{} Command was used wrongly.\n`ad!report user <id> <reason>`.\n`ad!report server <id> <reason>`.".format(error_img))
        else:
            if option == "user" or option == "server":
                if target == None or reason == None:
                    await client.say("{} Command was used wrongly.\n`ad!report user <id> <reason>`.\n`ad!report server <id> <reason>`.".format(error_img))
                else:
                    if len(str(reason)) > 1000:
                            await client.say("{} The reason cannot be longer than 1000 characters.".format(error_img))
                    else:
                        if option == "user":
                            found = []
                            chnl = client.get_channel(reports_users_chnl)
                            await client.say("Reporting... <a:typing:393848431413559296>")
                            try:
                                msg = "```diff"
                                msg += "\n- USER REPORT -"
                                msg += "\n+ Author: {} ### {}".format(author, author.id)
                                msg += "\n+ From: {} ### {}".format(server.name, server.id)
                                msg += "\n+ Target: {}".format(target)
                                msg += "\n+ Reason:"
                                msg += "\n```"
                                msg += "\n{}".format(reason)
                                await client.send_message(chnl, msg)
                                await client.say("{} Reported!".format(check_img))
                            except:
                                await client.say("{} Error in sending report.".format(error_img))
                        elif option == "server":
                            found = []
                            chnl = client.get_channel(reports_servers_chnl)
                            await client.say("Reporting... <a:typing:393848431413559296>")
                            try:
                                msg = "```diff"
                                msg += "\n- SERVER REPORT -"
                                msg += "\n+ Author: {} ### {}".format(author, author.id)
                                msg += "\n+ From: {} ### {}".format(server.name, server.id)
                                try:
                                    srv = client.get_server(target)
                                    msg += "\n+ Target: {} ### {}".format(srv.name, srv.id)
                                except:
                                    msg += "\n+ Target:   ### {}".format(target)
                                msg += "\n+ Reason:"
                                msg += "\n```"
                                msg += "\n{}".format(reason)
                                await client.send_message(chnl, msg)
                                await client.say("{} Reported!".format(check_img))
                            except:
                                await client.say("{} Error in sending report.".format(error_img))
                        else:
                            await client.say("{} Command was used wrongly.\n`ad!report user <id> <reason>`.\n`ad!report server <id> <reason>`.".format(error_img))
            else:
                await client.say("{} Command was used wrongly.\n`ad!report user <id> <reason>`.\n`ad!report server <id> <reason>`.".format(error_img))

# ad!bug <message>
@client.command(pass_context=True)
async def bug(ctx, *, args = None):
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    else:
        if args == None:
            await client.say("{} No message given.\n`ad!bug <message>`.".format(error_img))
        else:
            if len(str(args)) > 1000:
                await client.say("{} The message cannot be longer than 1000 characters.".format(error_img))
            else:
                author = ctx.message.author
                server = ctx.message.server
                chnl = client.get_channel(reports_bugs_chnl)
                await client.say("Reporting the bug... <a:typing:393848431413559296>")
                try:
                    msg = "```diff"
                    msg += "\n- BUG REPORT -"
                    msg += "\n+ Author: {} ### {}".format(author, author.id)
                    msg += "\n+ From: {} ### {}".format(server.name, server.id)
                    msg += "\n+ Message:"
                    msg += "\n```"
                    msg += "\n{}".format(args)
                    await client.send_message(chnl, msg)
                    await client.say("{} Reported the bug!".format(check_img))
                except:
                    await client.say("{} Error in reporting the bug!".format(error_img))

# ad!bump
@client.command(pass_context=True)
async def bump(ctx):
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    elif ctx.message.server.id in bumped_servers:
        await client.say("{} This server is already bumped. Please try again after the bot restarts (`ad!uptime`).".format(error_img))
    else:
        server = ctx.message.server
        author = ctx.message.author
        if server.id in normal_servers:
            await client.say("Bumping... <a:typing:393848431413559296>")
            try:
                msgs = []
                found = []
                sent = []
                for m in normal_servers_msgs:
                    a = str(m)
                    if server.id in a:
                        msgs.append(m)
                        break
                    else:
                        print("")
                msg = msgs[0]
                embed = discord.Embed(colour=0x00FFFF, description= "")
                embed.title = ""
                embed.set_footer(text=footer_text)
                embed.add_field(name="bump", value="{}".format(msg))
                for c in channels_ids:
                    try:
                        chnl = client.get_channel(c)
                        found.append("+1")
                        await client.send_message(chnl, embed=embed)
                        sent.append("+1")
                    except:
                        print("")
                bumped_servers.append(server.id)
                await client.say("{} The server has been bumped on {}/{} servers!".format(check_img, len(sent), len(found)))
            except:
                await client.say("{} Error in bumping the server!\nFor any help use `ad!support`.".format(error_img))
        elif server.id in special_servers:
            await client.say("Bumping... <a:typing:393848431413559296>")
            try:
                msgs = []
                found = []
                sent = []
                for m in special_servers_msgs:
                    a = str(m)
                    if server.id in a:
                        msgs.append(m)
                        break
                    else:
                        print("")
                msg = msgs[0]
                embed = discord.Embed(colour=0xFFAE00, description= "")
                embed.title = ""
                embed.set_image(url="{}".format(special_server_img))
                embed.set_footer(text=footer_text)
                embed.add_field(name="bump", value="{}".format(msg))
                for c in channels_ids:
                    try:
                        chnl = client.get_channel(c)
                        found.append("+1")
                        await client.send_message(chnl, embed=embed)
                        sent.append("+1")
                    except:
                        print("")
                bumped_servers.append(server.id)
                await client.say("{} The server has been bumped on {}/{} servers!".format(check_img, len(sent), len(found)))
            except:
                await client.say("{} Error in bumping the server!\nFor any help use `ad!support`.".format(error_img))
        else:
            await client.say("{} This server is not being advertised. Use `ad!setup` to set it up.".format(error_img))

''' COMMANDS FOR SERVER MANAGERS '''
# ad!setup [log channel] [channel] [message]
@client.command(pass_context=True)
async def setup(ctx, log_channel: discord.Channel = None, channel: discord.Channel = None, *, message = None):
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    else:
        author = ctx.message.author
        server = ctx.message.server
        if author.server_permissions.manage_server or author.id in bot_mods or author.id in bot_admins:
            if channel == None or message == None or log_channel == None:
                a = "```diff"
                a += "\n- SETUP GUIDE -"
                a += "\n+ Command: ad!setup <log channel> <ad channel> <message>"
                a += "\n"
                a += "\n+ Make sure the bot has the following permissions: Manage Server, Manage Channels, Kick Members, Ban Members, Create Instant Invite, Manage Webhooks, Read Messages, Send Messages, Manage Messages, Embed Links, Attach Files, Read Message History, Add Reactions, Use External Emojis."
                a += "\n "
                a += "\n+ The bot should already have these permissions if you use the official invite link (ad!invite)."
                a += "\n "
                a += "\n+ Create 2 channels for the bot. One where the bot will send advertisements and another one where the bot logs stuff. You can also use already existing channels, but its recommended to create a separate channel for the bot to log stuff in."
                a += "\n "
                a += "\n+ If you are using a bot to log stuff, make an exception for this bot so it doesn't spam your logs."
                a += "\n "
                a += "\n+ Use ad!setup [log channel] [channel] [message]."
                a += "\n "
                a += "\n+ log channel - The channel where the bot will send logs, announcements etc."
                a += "\n "
                a += "\n+ channel - The channel where the bot will send advertisements."
                a += "\n "
                a += "\n+ message - The message you want the bot to use when advertising your server. The message cannot be longer than 500 characters."
                a += "\n "
                a += "\n+ Once the bot is done setting up, use ad!test to check if everything is working correctly."
                a += "\n "
                a += "\n+ Remember the read the bot's rules and TOS (ad!tos)."
                a += "\n "
                a += "\n+ If you have any issues with the bot just use the ad!support command."
                a += "\n```"
                await client.say(a)
            elif server.id in normal_servers or server.id in special_servers:
                await client.say("{} This server is already being advertised.\nYou can use `ad!unsetup` to un-set it up.".format(error_img))
            else:
                if len(str(message)) > 500:
                    await client.say("{} The message cannot be longer than 500 characters.".format(error_img))
                else:
                    await client.say("Starting setup... <a:typing:393848431413559296>")
                    log = "```diff"
                    log += "\n--- STARTING SETUP LOGGER ---"
                    try:
                        log += "\n= Trying to get the log channel's ID..."
                        log_chnl_id = log_channel.id
                        log += "\n+ Found the log channel's ID!"
                        log += "\n= Trying to find the log channel using its ID..."
                        log_chnl = client.get_channel(log_chnl_id)
                        log += "\n+ The log channel has been found!"
                        log += "\n= Trying to get the channel's ID..."
                        chnl_id = channel.id
                        log += "\n+ Found the channel's ID!"
                        log += "\n= Trying to find the channel using its ID..."
                        chnl = client.get_channel(chnl_id)
                        log += "\n+ The channel has been found!"
                        log += "\n= Trying to create an invite link for the channel..."
                        invite = await client.create_invite(destination = chnl, xkcd = True, max_uses = 0)
                        log += "\n+ Invite link created!"
                        log += "\n= Creating message..."
                        msg = "{}".format(message)
                        msg += "\n**__~~= = = = = = = = = = = = = = = = = = = =~~__**"
                        msg += "\n:label: Name: {}".format(server.name)
                        msg += "\n:credit_card: ID: {}".format(server.id)
                        msg += "\n:crown: Owner: {} ### {}".format(server.owner, server.owner.id)
                        msg += "\n:link: Link: {}".format(invite.url)
                        msg += "\n**__~~= = = = = = = = = = = = = = = = = = = =~~__**"
                        log += "\n+ Message created!"
                        log += "\n= Trying to convert the message into an embed..."
                        embed = discord.Embed(colour=0x00FF00, description= "")
                        embed.title = ""
                        embed.set_image(url="{}".format(test_msg_img))
                        embed.set_footer(text=footer_text)
                        embed.add_field(name="test message", value="{}".format(msg))
                        log += "\n+ Converting finished!"
                        log += "\n= Sending test message..."
                        await client.send_message(chnl, embed=embed)
                        log += "\n+ Test message sent!"
                        log += "\n= Creating log message..."
                        tl = "```diff"
                        tl += "\n- TEST LOG MESSAGE -"
                        tl += "\n+ {}".format(server.id)
                        found = []
                        for srv in client.servers:
                            if srv.id == server.id:
                                found.append("+1")
                                break
                            else:
                                print("")
                        tl += "\n+ {}/{}".format(len(found), len(client.servers))
                        tl += "\n```"
                        log += "\n+ Log message created!"
                        log += "\n= Trying to convert the log message into an embed..."
                        embed2 = discord.Embed(colour=0x00FF00, description= "")
                        embed2.title = ""
                        embed2.set_image(url="{}".format(test_msg_img))
                        embed2.set_footer(text=footer_text)
                        embed2.add_field(name="test log message", value="{}".format(tl)) 
                        log += "\n+ Converting finished!"
                        log += "\n= Sending test log..."
                        await client.send_message(log_chnl, embed=embed2)
                        log += "\n+ Test log sent!"
                        log += "\n= Saving the log channel 1/2..."
                        log_channels_ids.append(log_chnl_id)
                        log += "\n+ Saved 1/2!"
                        log += "\n= Saving the log channel 2/2..."
                        lc = client.get_channel(log_channels_chnl)
                        await client.send_message(lc, log_chnl_id)
                        log += "\n+ Saved 2/2!"
                        log += "\n= Saving the channel 1/2..."
                        channels_ids.append(chnl_id)
                        log += "\n+ Saved 1/2!"
                        log += "\n= Saving the channel 2/2..."
                        c = client.get_channel(channels_chnl)
                        await client.send_message(c, chnl_id)
                        log += "\n+ Saved 2/2!"
                        log += "\n= Saving the invite link 1/2..."
                        servers_links.append(invite.url)
                        log += "\n+ Saved 1/2!"
                        log += "\n= Saving the invite link 2/2..."
                        sl = client.get_channel(servers_links_chnl)
                        await client.send_message(sl, invite.url)
                        log += "\n+ Saved 2/2!"
                        log += "\n= Saving the message 1/2..."
                        normal_servers_msgs.append(msg)
                        log += "\n+ Saved 1/2!"
                        log += "\n= Saving the message 2/2..."
                        nsm = client.get_channel(normal_servers_msgs_chnl)
                        await client.send_message(nsm, msg)
                        log += "\n+ Saved 2/2!"
                        log += "\n= Saving the server's ID 1/2..."
                        normal_servers.append(server.id)
                        log += "\n+ Saved 1/2!"
                        log += "\n= Saving the server's ID 2/2..."
                        ns = client.get_channel(normal_servers_chnl)
                        await client.send_message(ns, server.id)
                        log += "\n+ Saved 2/2!"
                        log += "\n= Sending results..."
                        log += "\n+ Finished!"
                        log += "\n--- CLOSING SETUP LOGGER ---"
                        log += "\n```"
                        await client.send_message(log_chnl, log)
                        await client.say("{} Everything should be working now and your server should be advertised.\nYou can use `ad!test` to check if everything is working and you can use `ad!bump` to force the bot to advertise your server.\nThe setup log has been sent to <#{}>.\nIf you have any questions or need any help, just use `ad!support`.\nThank you for using this bot! :grinning: ".format(check_img, log_chnl_id))
                    except:
                        log += "\n- ^ Error!"
                        log += "\n--- CLOSING SETUP LOGGER ---"
                        log += "\n```"
                        try:
                            await client.send_message(log_chnl, log)
                            await client.say("{} Looks like an error occured!\nThe setup log has been sent to <#{}>.\nMake sure the bot has the required permissions.\nYou can use `ad!unsetup` and try again.\nIf you need any help, just use `ad!support`.".format(error_img, log_chnl_id))
                        except:
                            await client.say(log)
                            await client.say("{} Looks like an error occured!\nMake sure the bot has the required permissions.\nYou can use `ad!unsetup` and try again.\nIf you need any help, just use `ad!support`.".format(error_img))
        else:
            await client.say("{} This command can only be used by users with the `Manage Server` permissions and can be bypassed by the bot's staff.".format(error_img))

# ad!unsetup
@client.command(pass_context=True)
async def unsetup(ctx):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    elif author.server_permissions.manage_server or author.id in bot_mods or author.id in bot_admins:
        if server.id in normal_servers:
            await client.say("Removing data... <a:typing:393848431413559296>")
            log = "```diff"
            log += "\n--- STARTING UN-SETUP LOGGER ---"
            try:
                limit = 100000
                print("[UNSETUP] LIMIT SET")
                nsm = client.get_channel(normal_servers_msgs_chnl)
                print("[UNSETUP] CHANNEL GOT NSM")
                cc = client.get_channel(channels_chnl)
                print("[UNSETUP] CHANNEL GOT CC")
                lc = client.get_channel(log_channels_chnl)
                print("[UNSETUP] CHANNEL GOT LC")
                ns = client.get_channel(normal_servers_chnl)
                print("[UNSETUP] CHANNEL GOT NS")
                sl = client.get_channel(servers_links_chnl)
                print("[UNSETUP] CHANNEL GOT SL")
                ts = client.get_channel(toggled_servers_chnl)
                print("[UNSETUP] CHANNEL GOT TS")
                print("[UNSETUP] GOT ALL CHANNELS")
                log += "\n= Looking for used message..."
                print("[UNSETUP] LOOKING FOR MESSAGE")
                try:
                    for m in normal_servers_msgs:
                        a = str(m)
                        if server.id in a:
                            log += "\n+ Message found!"
                            print("[UNSETUP] MESSAGE FOUND")
                            log += "\n= Removing message 1/2..."
                            async for message in client.logs_from(nsm, limit=limit):
                                if message.content == m:
                                    await client.delete_message(message)
                                    log += "\n+ Removed 1/2!"
                                    print("[UNSETUP] MESSAGE REMOVED")
                                    break
                                else:
                                    print("[UNSETUP] MESSAGE DOESN'T MATCH (C)")
                        else:
                            print("[UNSETUP] MESSAGE DOESN'T MATCH (L)")
                    for m in normal_servers_msgs:
                        a = str(m)
                        if server.id in a:
                            log += "\n= Removing message 2/2..."
                            normal_servers_msgs.remove(m)
                            log += "\n+ Removed 2/2!"
                            print("[UNSETUP] MESSAGE REMOVED 2")
                            break
                        else:
                            print("[UNSETUP] MESSAGE DOESN'T MATCH (L 2)")
                except:
                    log += "\n- Message not found!"
                    print("[UNSETUP] MESSAGE NOT FOUND")
                log += "\n= Looking for used channel..."
                print("[UNSETUP] LOOKING FOR CHANNEL")
                try:
                    for c in server.channels:
                        if c.id in channels_ids:
                            log += "\n+ Channel found!"
                            log += "\n= Removing channel 1/2..."
                            print("[UNSETUP] CHANNEL FOUND")
                            async for message in client.logs_from(cc, limit=limit):
                                if message.content == c.id:
                                    await client.delete_message(message)
                                    log += "\n+ Removed 1/2!"
                                    print("[UNSETUP] CHANNEL REMOVED")
                                    break
                                else:
                                    print("[UNSETUP] CHANNEL DOESN'T MATCH (C)")
                        else:
                            print("[UNSETUP] CHANNEL DOESN'T MATCH (L)")
                    for c in server.channels:
                        if c.id in channels_ids:
                            log += "\n= Removing channel 2/2..."
                            channels_ids.remove(c.id)
                            log += "\n+ Removed 2/2!"
                            print("[UNSETUP] CHANNEL REMOVED 2")
                        else:
                            print("[UNSETUP] CHANNEL DOESN'T MATCH (L 2)")
                except:
                    log += "\n- Channel not found!"
                    print("[UNSETUP] CHANNEL NOT FOUND")
                print("[UNSETUP] LOOKING FOR LOG")
                log += "\n= Looking for log channel..."
                try:
                    for c in server.channels:
                        if c.id in log_channels_ids:
                            log += "\n+ Log channel found!"
                            log += "\n= Removing log channel 1/2..."
                            print("[UNSETUP] LOG FOUND")
                            async for message in client.logs_from(lc, limit=limit):
                                if message.content == c.id:
                                    await client.delete_message(message)
                                    log += "\n+ Removed 1/2!"
                                    print("[UNSETUP] LOG REMOVED")
                                    break
                                else:
                                    print("[UNSETUP] LOG DOESN'T MATCH (C)")
                        else:
                            print("[UNSETUP] LOG DOESN'T MATCH (L)")
                    for c in server.channels:
                        if c.id in log_channels_ids:
                            log += "\n= Removing log channel 2/2..."
                            log_channels_ids.remove(c.id)
                            log += "\n+ Removed 2/2!"
                            print("[UNSETUP] LOG REMOVED 2")
                            break
                        else:
                            print("[UNSETUP] LOG DOESN'T MATCH (L 2)")
                except:
                    log += "\n- Log channel not found!"
                    print("[UNSETUP] LOG NOT FOUND")
                log += "\n= Removing server ID 1/2..."
                print("[UNSETUP] REMOVING SERVER ID")
                async for message in client.logs_from(ns, limit=limit):
                    if message.content == server.id:
                        await client.delete_message(message)
                        log += "\n+ Removed 1/2!"
                        print("[UNSETUP] SERVER ID REMOVED")
                        break
                    else:
                        print("[UNSETUP] SERVER ID DOESN'T MATCH (C)")
                log += "\n= Removing server ID 2/2..."
                for s in normal_servers:
                    if s == server.id:
                        normal_servers.remove(s)
                        log += "\n+ Removed 2/2!"
                        print("[UNSETUP] SERVER ID REMOVED 2")
                    else:
                        print("[UNSETUP] SERVER ID DOESN'T MATCH (L)")
                print("[UNSETUP] GETTING LINKS")
                log += "\n= Collecting server links..."
                invites = await client.invites_from(server)
                log += "\n+ Collected links!"
                log += "\n= Removing used link 1/2..."
                print("[UNSETUP] LINKS GOT")
                for link in invites:
                    if link.url in servers_links:
                        async for message in client.logs_from(sl):
                            if message.content == link.url:
                                await client.delete_message(message)
                                log += "\n+ Removed 1/2!"
                                print("[UNSETUP] REMOVED LINK")
                                break
                            else:
                                print("[UNSETUP] LINK DOESN'T MATCH (C)")
                    else:
                        print("[UNSETUP] LINK DOESN'T MATCH (L)")
                log += "\n= Removing used link 2/2..."
                for link in invites:
                    if link.url in servers_links:
                        servers_links.remove(link.url)
                        log += "\n+ Removed 2/2!"
                        print("[UNSETUP] REMOVED LINK 2")
                        break
                    else:
                        print("[UNSETUP] LINK DOESN'T MATCH (L 2)")
                log += "\n= Checking if the server is toggled..."
                print("[UNSETUP] CHECKING FOR TOGGLE")
                if server.id in toggled_servers:
                    log += "\n+ Server is toggled!"
                    log += "\n= Removing toggle 1/2..."
                    print("[UNSETUP] TOGGLE FOUND")
                    for t in toggled_servers:
                        if t == server.id:
                            async for message in client.logs_from(ts, limit=limit):
                                if message.content == server.id:
                                    await client.delete_message(message)
                                    log += "\n+ Removed 1/2!"
                                    print("[UNSETUP] TOGGLE REMOVED")
                                    break
                                else:
                                    print("[UNSETUP] TOGGLE DOESN'T MATCH (C)")
                        else:
                            print("[UNSETUP] TOGGLE DOESN'T MATCH (L)")
                    for t in toggled_servers:
                        if t == server.id:
                            toggled_servers.remove(t)
                            log += "\n+ Removed 2/2!"
                            print("[UNSETUP] TOGGLE REMOVED 2")
                            break
                        else:
                            print("[UNSETUP] TOGGLE DOESN'T MATCH (L 2)")
                else:
                    log += "\n+ Server is not toggled!"
                    print("[UNSETUP] SERVER IS NOT TOGGLED")
                print("[UNSETUP] FINISHING")
                log += "\n= Sending results..."
                log += "\n+ Finished!"
                log += "\n--- CLOSING UN-SETUP LOGGER ---"
                log += "\n```"
                await client.say(log)
                await client.say("{} Everything should be done now.\nYou can setup the server again with `ad!setup`.".format(check_img))
                print("[UNSETUP] FINISHED!!!!")
            except:
                print("[UNSETUP] ERROR!!!!")
                log += "\n- ^ Error!"
                log += "\n--- CLOSING UN-SETUP LOGGER ---"
                log += "\n```"
                await client.say(log)
                await client.say("{} Looks like there has been an error!\nMake sure the bot has the required permissions and try again.\nIf you need any help you can use `ad!support`.".format(error_img))
                print("[UNSETUP] ERROR!!!!")
        else:
            await client.say("{} The server is not setup!\nYou can set it up with `ad!setup`.\nIf you need any help you can use `ad!support`.".format(error_img))
    else:
        await client.say("{} This command can only be used by users with the `Manage Server` permissions and can be bypassed by the bot's staff.".format(error_img))

# ad!test
@client.command(pass_context=True)
async def test(ctx):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    elif author.server_permissions.manage_server or author.id in bot_mods or author.id in bot_admins:
        if server.id in normal_servers:
            await client.say("Testing... <a:typing:393848431413559296>")
            log = "```diff"
            log += "\n--- STARTING TEST LOGGER (NORMAL) ---"
            limit = 100000
            nsm = client.get_channel(normal_servers_msgs_chnl)
            cc = client.get_channel(channels_chnl)
            lc = client.get_channel(log_channels_chnl)
            ns = client.get_channel(normal_servers_chnl)
            sl = client.get_channel(servers_links_chnl)
            ts = client.get_channel(toggled_servers_chnl)
            msgs = []
            try:
                log += "\n= Searching for used message..."
                for m in normal_servers_msgs:
                    a = str(m)
                    if server.id in a:
                        async for message in client.logs_from(nsm, limit=limit):
                            if message.content == m:
                                msgs.append(m)
                                log += "\n+ Message found!"
                                break
                            else:
                                print("")
                    else:
                        print("")
                        
                log += "\n= Searching for used channel..."
                for c in server.channels:
                    if c.id in channels_ids:
                        async for message in client.logs_from(cc, limit=limit):
                            if message.content == c.id:
                                chnl = c
                                log += "\n+ Channel found!"
                                break
                            else:
                                print("")
                    else:
                        print("")

                log += "\n= Searching for log channel..."
                for c in server.channels:
                    if c.id in log_channels_ids:
                        async for message in client.logs_from(lc, limit=limit):
                            if message.content == c.id:
                                log_chnl = c
                                log += "\n+ Log channel found!"
                                break
                            else:
                                print("")
                    else:
                        print("")
                        
                log += "\n= Searching for server's ID..."
                if server.id in normal_servers:
                    log += "\n+ Server's ID found 1/2!"
                    async for message in client.logs_from(ns, limit=limit):
                        if message.content == server.id:
                            log += "\n+ Server's ID found 2/2!"
                            break
                        else:
                            print("")
                else:
                    log += "\n- Server ID not found!"
                    
                log += "\n= Collecting links..."
                invites = await client.invites_from(server)
                log += "\n+ Links collected!"
                log += "\n= Searching for used link..."
                for link in invites:
                    if link.url in servers_links:
                        async for message in client.logs_from(sl, limit=limit):
                            if message.content == link.url:
                                log += "\n+ Link found!"
                                break
                            else:
                                print("")
                    else:
                        print("")
                log += "\n= Creating test message..."
                msg = msgs[0]
                embed = discord.Embed(colour=0x00FF00, description= "")
                embed.title = ""
                embed.set_image(url="{}".format(test_msg_img))
                embed.set_footer(text=footer_text)
                embed.add_field(name="test message", value="{}".format(msg))
                log += "\n+ Message created!"
                log += "\n= Sending test message..."
                await client.send_message(chnl, embed=embed)
                log += "\n+ Test message sent!"
                log += "\n= Creating test log message..."
                tl = "```diff"
                tl += "\n- TEST LOG MESSAGE -"
                tl += "\n+ {}".format(server.id)
                found = []
                for srv in client.servers:
                    if srv.id == server.id:
                        found.append("+1")
                        break
                    else:
                        print("")
                tl += "\n+ {}/{}".format(len(found), len(client.servers))
                tl += "\n```"
                embed2 = discord.Embed(colour=0x00FF00, description= "")
                embed2.title = ""
                embed2.set_image(url="{}".format(test_msg_img))
                embed2.set_footer(text=footer_text)
                embed2.add_field(name="test log message", value="{}".format(tl))
                log += "\n+ Test log message created!"
                log += "\n= Sending test log message..."
                await client.send_message(log_chnl, embed=embed2)
                log += "\n+ Test log message sent!"
                log += "\n= Sending results..."
                log += "\n+ Finished!"
                log += "\n--- CLOSING SETUP LOGGER ---"
                log += "\n```"
                await client.send_message(log_chnl, log)
                await client.say("{} Everything should be working like it should!\nIf you have any problems you can use `ad!support`.\nThe test log has been sent to <#{}>.".format(check_img, log_chnl.id))
            except:
                log += "\n- ^ Error!"
                log += "\n--- CLOSING TEST LOGGER ---"
                log += "\n```"
                try:
                    chnl = client.get_channel(log_chnls[0])
                    await client.send_message(chnl, log)
                    await client.say("{} Looks like there is an error!\nMake sure the bot has the required permissiosn and try again.\nIf you need any help you can use `ad!support`.\nThe test log has been sent to <#{}>.".format(error_img, chnl.id))
                except:
                    await client.say(log)
                    await client.say("{} Looks like there is an error!\nMake sure the bot has the required permissiosn and try again.\nIf you need any help you can use `ad!support`.".format(error_img))
        elif server.id in special_servers:
            await client.say("Testing... <a:typing:393848431413559296>")
            log = "```diff"
            log += "\n--- STARTING TEST LOGGER (SPECIAL) ---"
            limit = 100000
            ssm = client.get_channel(special_servers_msgs_chnl)
            cc = client.get_channel(channels_chnl)
            lc = client.get_channel(log_channels_chnl)
            ss = client.get_channel(special_servers_chnl)
            sl = client.get_channel(servers_links_chnl)
            ts = client.get_channel(toggled_servers_chnl)
            msgs = []
            try:
                log += "\n= Searching for used message..."
                for m in special_servers_msgs:
                    a = str(m)
                    if server.id in a:
                        async for message in client.logs_from(ssm, limit=limit):
                            if message.content == m:
                                msgs.append(m)
                                log += "\n+ Message found!"
                                break
                            else:
                                print("")
                    else:
                        print("")
                        
                log += "\n= Searching for used channel..."
                for c in server.channels:
                    if c.id in channels_ids:
                        async for message in client.logs_from(cc, limit=limit):
                            if message.content == c.id:
                                chnl = c
                                log += "\n+ Channel found!"
                                break
                            else:
                                print("")
                    else:
                        print("")

                log += "\n= Searching for log channel..."
                for c in server.channels:
                    if c.id in log_channels_ids:
                        async for message in client.logs_from(lc, limit=limit):
                            if message.content == c.id:
                                log_chnl = c
                                log += "\n+ Log channel found!"
                                break
                            else:
                                print("")
                    else:
                        print("")
                        
                log += "\n= Searching for server's ID..."
                if server.id in special_servers:
                    log += "\n+ Server's ID found 1/2!"
                    async for message in client.logs_from(ss, limit=limit):
                        if message.content == server.id:
                            log += "\n+ Server's ID found 2/2!"
                            break
                        else:
                            print("")
                else:
                    log += "\n- Server ID not found!"
                    
                log += "\n= Collecting links..."
                invites = await client.invites_from(server)
                log += "\n+ Links collected!"
                log += "\n= Searching for used link..."
                for link in invites:
                    if link.url in servers_links:
                        async for message in client.logs_from(sl, limit=limit):
                            if message.content == link.url:
                                log += "\n+ Link found!"
                                break
                            else:
                                print("")
                    else:
                        print("")
                log += "\n= Creating test message..."
                msg = msgs[0]
                embed = discord.Embed(colour=0x00FF00, description= "")
                embed.title = ""
                embed.set_image(url="{}".format(test_msg_img))
                embed.set_footer(text=footer_text)
                embed.add_field(name="test message", value="{}".format(msg))
                log += "\n+ Message created!"
                log += "\n= Sending test message..."
                await client.send_message(chnl, embed=embed)
                log += "\n+ Test message sent!"
                log += "\n= Creating test log message..."
                tl = "```diff"
                tl += "\n- TEST LOG MESSAGE -"
                tl += "\n+ {}".format(server.id)
                found = []
                for srv in client.servers:
                    if srv.id == server.id:
                        found.append("+1")
                        break
                    else:
                        print("")
                tl += "\n+ {}/{}".format(len(found), len(client.servers))
                tl += "\n```"
                embed2 = discord.Embed(colour=0x00FF00, description= "")
                embed2.title = ""
                embed2.set_image(url="{}".format(test_msg_img))
                embed2.set_footer(text=footer_text)
                embed2.add_field(name="test log message", value="{}".format(tl))
                log += "\n+ Test log message created!"
                log += "\n= Sending test log message..."
                await client.send_message(log_chnl, embed=embed2)
                log += "\n+ Test log message sent!"
                log += "\n= Sending results..."
                log += "\n+ Finished!"
                log += "\n--- CLOSING SETUP LOGGER ---"
                log += "\n```"
                await client.send_message(log_chnl, log)
                await client.say("{} Everything should be working like it should!\nIf you have any problems you can use `ad!support`.\nThe test log has been sent to <#{}>.".format(check_img, log_chnl.id))
            except:
                log += "\n- ^ Error!"
                log += "\n--- CLOSING TEST LOGGER ---"
                log += "\n```"
                try:
                    chnl = client.get_channel(log_chnls[0])
                    await client.send_message(chnl, log)
                    await client.say("{} Looks like there is an error!\nMake sure the bot has the required permissiosn and try again.\nIf you need any help you can use `ad!support`.\nThe test log has been sent to <#{}>.".format(error_img, chnl.id))
                except:
                    await client.say(log)
                    await client.say("{} Looks like there is an error!\nMake sure the bot has the required permissiosn and try again.\nIf you need any help you can use `ad!support`.".format(error_img))
        else:
            await client.say("{} The server is not setup!\nYou can set it up with `ad!setup`.\nIf you need any help you can use `ad!support`.".format(error_img))
    else:
        await client.say("{} This command can only be used by users with the `Manage Server` permissions and can be bypassed by the bot's staff.".format(error_img))

# ad!scan
@client.command(pass_context=True)
async def scan(ctx):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    elif author.server_permissions.manage_server or author.id in bot_mods or author.id in bot_admins:
        await client.say("Scanning... <a:typing:393848431413559296>")
        ban = []
        fail = []
        for i in banned_users:
            try:
                await client.http.ban(i, server.id, 0)
                ban.append("+1")
            except:
                fail.append("+1")
        msg = "```diff"
        msg += "\n- SCANNING LOG -"
        msg += "\n+ Scan run by: {} ### {}".format(author, author.id)
        msg += "\n+ Banned users: {}/{}".format(len(ban), len(banned_users))
        msg += "\n+ Failed: {}".format(len(fail))
        msg += "\n```"
        for c in log_channels_ids:
            try:
                chnl = client.get_channel(c)
                if chnl in server.channels:
                    try:
                        await client.send_message(chnl, msg)
                        await client.say("{} Scan complete!\nThe scan log has been sent to <#{}>.".format(check_img, c))
                    except:
                        await client.say("{} Scan complete!\n{}".format(check_img, msg))
                    break
                else:
                    print("")
            except:
                print("")
    else:
        await client.say("{} This command can only be used by users with the `Manage Server` permissions and can be bypassed by the bot's staff.".format(error_img))

# ad!toggle
@client.command(pass_context=True)
async def toggle(ctx):
    author = ctx.message.author
    server = ctx.message.server
    chnl = client.get_channel(toggled_servers_chnl)
    if ctx.message.server.id in banned_servers:
        await client.say("<:xmark:314349398824058880> This server is in the ban list and cannot use the bot.")
    elif ctx.message.author.id in banned_users:
        await client.say("<:xmark:314349398824058880> You are on the blacklist and cannot use the bot.")
    elif author.server_permissions.manage_server or author.id in bot_mods or author.id in bot_admins:
        await client.say("Toggling... <a:typing:393848431413559296>")
        if server.id in toggled_servers:
            try:
                async for message in client.logs_from(chnl):
                    if message.content == server.id:
                        await client.delete_message(message)
                        break
                    else:
                        print("")
                toggled_servers.remove(server.id)
                msg = "```diff"
                msg += "\n- TOGGLE LOG -"
                msg += "\n+ Server has been un-toggled by: {} ### {}".format(author, author.id)
                msg += "\n```"
                for c in log_channels_ids:
                    try:
                        log = client.get_channel(c)
                        if log in server.channels:
                            try:
                                await client.send_message(log, msg)
                                await client.say("{} The bot will now continue advertising your server!\nThe toggle log was sent to <#{}>.".format(check_img, c))
                            except:
                                await client.say("{} The bot will now continue advertising your server!".format(check_img))
                            break
                        else:
                            print("")
                    except:
                        print("")
            except:
                await client.say("{} There has been an error in toggling this server!\nFor any help you can use `ad!support`.".format(error_img))
        else:
            try:
                await client.send_message(chnl, server.id)
                toggled_servers.append(server.id)
                msg = "```diff"
                msg += "\n- TOGGLE LOG -"
                msg += "\n+ Server has been toggled by: {} ### {}".format(author, author.id)
                msg += "\n```"
                for c in log_channels_ids:
                    try:
                        log = client.get_channel(c)
                        if log in server.channels:
                            try:
                                await client.send_message(log, msg)
                                await client.say("{} The bot won't advertise your server until you un-toggle it!\nThe toggle log was sent to <#{}>.".format(check_img, c))
                            except:
                                await client.say("{} The bot won't advertise your server until you un-toggle it!".format(check_img))
                        else:
                            print("")
                    except:
                        print("")
            except:
                await client.say("{} There has been an error in toggling this server!\nFor any help you can use `ad!support`.".format(error_img))
    else:
        await client.say("{} This command can only be used by users with the `Manage Server` permissions and can be bypassed by the bot's staff.".format(error_img))

''' COMMANDS FOR BOT MODERATORS '''
# ad!msg <user/server> <id> <message>
@client.command(pass_context=True)
async def msg(ctx, option = None, target = None, *, args = None):
    author = ctx.message.author
    chnl = client.get_channel(console_chnl)
    if author.id in bot_mods or author.id in bot_admins:
        if option == None or target == None or args == None:
            await client.say("{} Not all arguments were given!\nExamples:\n`ad!msg user 331398432726056961 Hello! How are you?`.\n`ad!msg server 440108166789988353 Hello! How are you?`.".format(error_img))
        else:
            if option == "user" or option == "server":
                if len(str(args)) > 1900:
                    await client.say("{} The message cannot be longer than 1900 characters.".format(error_img))
                else:
                    if option == "user":
                        find = []
                        await client.say("Searching for user... <a:typing:393848431413559296>")
                        try:
                            user = await client.get_user_info(target)
                            await client.say("{} User found: {}#{}!\nSending message... <a:typing:393848431413559296>".format(check_img, user.name, user.discriminator))
                            try:
                                await client.send_message(user, "{}\n \n:label: Message sent by: {} ### {}\n`(Advertiser Bot Staff Member)`".format(args, author, author.id))
                                await client.say("{} Message sent!".format(check_img))
                                msg = "```diff"
                                msg += "\n- USER MESSAGE -"
                                msg += "\n+ Author: {} ### {}".format(author, author.id)
                                msg += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                                msg += "\n+ Target: {} ### {}".format(user, user.id)
                                msg += "\n+ Message:"
                                msg += "\n```"
                                msg += "\n{}".format(args)
                                await client.send_message(chnl, msg)
                            except:
                                await client.say("{} Could not send the message to the user!\nEither the bot has no permission to send DMs to that user or they don't have a mutual server.".format(error_img))
                        except:
                            await client.say("{} User not found!".format(error_img))
                    elif option == "server":
                        find = []
                        finish = []
                        await client.say("Searching for server... <a:typing:393848431413559296>")
                        for server in client.servers:
                            if server.id == target:
                                try:
                                    if len(finish) == 0:
                                        await client.say("{} Server found: {}!\nSending message... <a:typing:393848431413559296>".format(check_img, server.name))
                                        find.append("+1")
                                        await client.send_message(server.owner, "{}\n \n:label: Message sent by: {} ### {}\n`(Advertiser Bot Staff Member)`".format(args, author, author.id))
                                        await client.say("{} Message sent!".format(check_img))
                                        msg = "```diff"
                                        msg += "\n- SERVER MESSAGE -"
                                        msg += "\n+ Author: {} ### {}".format(author, author.id)
                                        msg += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                                        msg += "\n+ Target: {} ### {}".format(server.name, server.id)
                                        msg += "\n+ Message:"
                                        msg += "\n```"
                                        msg += "\n{}".format(args)
                                        await client.send_message(chnl, msg)
                                        finish.append("+1")
                                    else:
                                        print("")
                                except:
                                    print("")
                            else:
                                print("")
                        if len(finish) == 0:
                            await client.say("{} Server not found!".format(error_img))
                        else:
                            print("")
                    else:
                        await client.say("{} Invalid option!\nOptions: `user`, `server`.".format(error_img))
            else:
                await client.say("{} Invalid option!\nOptions: `user`, `server`.".format(error_img))
    else:
        await client.say("{} This command can only be used by the bot's staff!".format(error_img))

# ad!ban <user/server> <id> <reason>
@client.command(pass_context=True)
async def ban(ctx, option = None, target = None, *, reason = None):
    author = ctx.message.author
    cnsl = client.get_channel(console_chnl)
    chnl = client.get_channel(banned_users_chnl)
    chnl2 = client.get_channel(banned_servers_chnl)
    if author.id in bot_mods or author.id in bot_admins:
        if option == None or target == None or reason == None:
            await client.say("{} Not all arguments were given!\nExamples:\n`ad!ban user 412201413335056386 Raiding servers`.\n`ad!ban server 452865346081128448 Not following the bot's TOS.`.".format(error_img))
        else:
            if option == "user" or option == "server":
                if len(str(reason)) > 1900:
                    await client.say("{} The reason cannot be longer than 1900 characters.".format(error_img))
                elif option == "user":
                    if target in banned_users:
                        await client.say("{} This user is already banned!".format(error_img))
                    else:
                        await client.say("Banning user... <a:typing:393848431413559296>")
                        await client.send_message(chnl, target)
                        banned_users.append(target)
                        a = []
                        f = []
                        for server in client.servers:
                            for c in server.channels:
                                if c.id in log_channels_ids:
                                    try:
                                        msg = "```diff"
                                        msg += "\n- BAN -"
                                        msg += "\n+ Banned user's ID: {}".format(target)
                                        msg += "\n+ Banned by: {} ### {}".format(author, author.id)
                                        msg += "\n+ You can use 'ad!scan' to ban all the black listed users."
                                        msg += "\n+ Reason:"
                                        msg += "\n```"
                                        msg += "\n{}".format(reason)
                                        await client.send_message(c, msg)
                                        a.append("+1")
                                    except:
                                        f.append("+1")
                                    break
                                else:
                                    print("")
                        await client.say("{} Finished!\nCheck the console for information.".format(check_img))
                        log = "```diff"
                        log += "\n- USER BAN -"
                        log += "\n+ Author: {} ### {}".format(author, author.id)
                        log += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                        log += "\n+ Notified: {}/{}".format(len(a), len(client.servers))
                        log += "\n+ Failed: {}/{}".format(len(f), len(client.servers))
                        log += "\n+ Reason:"
                        log += "\n```"
                        log += "\n{}".format(reason)
                        await client.send_message(cnsl, log)
                elif option == "server":
                    if target in banned_servers:
                        await client.say("{} This server is already banned!".format(error_img))
                    else:
                        await client.say("Banning server... <a:typing:393848431413559296>")
                        await client.send_message(chnl2, target)
                        banned_servers.append(target)
                        a = []
                        f = []
                        for server in client.servers:
                            for c in server.channels:
                                if c.id in log_channels_ids:
                                    try:
                                        msg = "```diff"
                                        msg += "\n- BAN -"
                                        msg += "\n+ Banned server's ID: {}".format(target)
                                        msg += "\n+ Banned by: {} ### {}".format(author, author.id)
                                        msg += "\n+ Reason:"
                                        msg += "\n```"
                                        msg += "\n{}".format(reason)
                                        await client.send_message(c, msg)
                                        a.append("+1")
                                        break
                                    except:
                                        f.append("+1")
                                else:
                                    print("")
                        await client.say("{} Finished!\nCheck the console for information.".format(check_img))
                        log = "```diff"
                        log += "\n- SERVER BAN -"
                        log += "\n+ Author: {} ### {}".format(author, author.id)
                        log += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                        log += "\n+ Notified: {}/{}".format(len(a), len(client.servers))
                        log += "\n+ Failed: {}/{}".format(len(f), len(client.servers))
                        log += "\n+ Reason:"
                        log += "\n```"
                        log += "\n{}".format(reason)
                        await client.send_message(cnsl, log)
                else:
                    await client.say("{} Invalid option!\nOptions: `user`, `server`.".format(error_img))
            else:
                await client.say("{} Invalid option!\nOptions: `user`, `server`.".format(error_img))
    else:
        await client.say("{} This command can only be used by the bot's staff!".format(error_img))

# ad!unban <user/server> <id>
@client.command(pass_context=True)
async def unban(ctx, option = None, target = None):
    author = ctx.message.author
    chnl = client.get_channel(banned_users_chnl)
    chnl2 = client.get_channel(banned_servers_chnl)
    cnsl = client.get_channel(console_chnl)
    if author.id in bot_mods or author.id in bot_admins:
        if option == None or target == None:
            await client.say("{} Not all arguments were given!\nExamples:\n`ad!unban user 412201413335056386`.\n`ad!unban server 440108166789988353`.".format(error_img))
        else:
            if option == "user":
                await client.say("Unbanning... <a:typing:393848431413559296>")
                try:
                    async for message in client.logs_from(chnl):
                        if message.content == target:
                            await client.delete_message(message)
                            break
                        else:
                            print("")
                    try:
                        banned_users.remove(target)
                        await client.say("{} The user has been unbanned!".format(check_img))
                        msg = "```diff"
                        msg += "\n- USER UNBAN -"
                        msg += "\n+ Author: {} ### {}".format(author, author.id)
                        msg += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                        msg += "\n+ Target: {}".format(target)
                        msg += "\n```"
                        await client.send_message(cnsl, msg)
                    except:
                        await client.say("{} That user is not banned!".format(error_img))
                except:
                    await client.say("{} There was an error while trying to unban that user!".format(error_img))
            elif option == "server":
                await client.say("Unbanning... <a:typing:393848431413559296>")
                try:
                    async for message in client.logs_from(chnl2):
                        if message.content == target:
                            await client.delete_message(message)
                            break
                        else:
                            print("")
                    try:
                        banned_servers.remove(target)
                        await client.say("{} The server has been unbanned!".format(check_img))
                        msg = "```diff"
                        msg += "\n- SERVER UNBAN -"
                        msg += "\n+ Author: {} ### {}".format(author, author.id)
                        msg += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                        msg += "\n+ Target: {}".format(target)
                        msg += "\n```"
                        await client.send_message(cnsl, msg)
                    except:
                        await client.say("{} That server is not banned!".format(error_img))
                except:
                    await client.say("{} There was an error while trying to unban that server!".format(error_img))
            else:
                await client.say("{} Invalid option!\nOptions: `user`, `server`.".format(error_img))
    else:
        await client.say("{} This command can only be used by the bot's staff!".format(error_img))

# ad!reset <server id>
@client.command(pass_context=True)
async def reset(ctx, target = None):
    author = ctx.message.author
    if author.id in bot_mods or author.id in bot_admins:
        if target == None:
            await client.say("{} No server ID given!".format(error_img))
        else:
            ts = client.get_channel(toggled_servers_chnl)
            ss = client.get_channel(special_servers_chnl)
            ns = client.get_channel(normal_servers_chnl)
            nsm = client.get_channel(normal_servers_msgs_chnl)
            ssm = client.get_channel(special_servers_msgs_chnl)
            c = client.get_channel(channels_chnl)
            lc = client.get_channel(log_channels_chnl)
            sl = client.get_channel(servers_links_chnl)
            cnsl = client.get_channel(console_chnl)
            try:
                find = []
                await client.say("Searching for server... <a:typing:393848431413559296>")
                for server in client.servers:
                    if server.id == target:
                        find.append(server.id)
                        break
                    else:
                        print("")
                if len(find) == 0:
                    await client.say("{} Server not found!\nMaybe the bot is not in that server.".format(error_img))
                else:
                    server = client.get_server(find[0])
                    await client.say("{} Server found ( {} )!".format(check_img, server.name))
                    await client.say("Resetting the server... <a:typing:393848431413559296>")
                    try:
                        async for message in client.logs_from(ns):
                            if message.content == target:
                                await client.delete_message(message)
                                break
                            else:
                                print("")
                        try:
                            normal_servers.remove(target)
                        except:
                            print("")
                        async for message in client.logs_from(nsm):
                            a = str(message.content)
                            if target in a:
                                await client.delete_message(message)
                                break
                            else:
                                print("")
                        for i in normal_servers_msgs:
                            a = str(i)
                            if target in a:
                                normal_servers_msgs.remove(i)
                            else:
                                print("")
                        bb = []
                        for channel in server.channels:
                            if channel.id in channels_ids:
                                channels_ids.remove(channel.id)
                                bb.append(channel.id)
                                break
                            else:
                                print("")
                        async for message in client.logs_from(c):
                            if message.content == bb[0]:
                                await client.delete_message(message)
                                break
                            else:
                                print("")
                        kk = []
                        for channel in server.channels:
                            if channel.id in log_channels_ids:
                                log_channels_ids.remove(channel.id)
                                kk.append(channel.id)
                                break
                            else:
                                print("")
                        async for message in client.logs_from(lc):
                            if message.content == kk[0]:
                                await client.delete_message(message)
                                break
                            else:
                                print("")
                        if target in toggled_servers:
                            async for message in client.logs_from(ts):
                                if message.content == target:
                                    await client.delete_message(message)
                                    break
                                else:
                                    print("")
                            try:
                                toggled_servers.remove(target)
                            except:
                                print("")
                        try:
                            invs = await client.invites_from(server)
                            oo = []
                            for inv in invs:
                                if inv.url in servers_links:
                                    servers_links.remove(inv.url)
                                    oo.append(inv.url)
                                    break
                                else:
                                    print("")
                            async for message in client.logs_from(sl):
                                if message.content == oo[0]:
                                    await client.delete_message(message)
                                    break
                                else:
                                    print("")
                        except:
                            print("")
                        async for message in client.logs_from(ssm):
                            u = str(message.content)
                            if target in u:
                                await client.delete_message(message)
                                break
                            else:
                                print("")
                        for i in special_servers_msgs:
                            u = str(i)
                            if target in u:
                                special_servers_msgs.remove(i)
                                break
                            else:
                                print("")
                        async for message in client.logs_from(ss):
                            if message.content == target:
                                await client.delete_message(message)
                                break
                            else:
                                print("")
                        try:
                            special_servers.remove(target)
                        except:
                            print("")
                        await client.say("{} All finished!\nAll the server's data should now be deleted!".format(check_img))
                        o = "```diff"
                        o += "\n- RESET -"
                        o += "\n+ Author: {} ### {}".format(author, author.id)
                        o += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                        o += "\n+ Target: {}".format(target)
                        o += "\n```"
                        await client.send_message(cnsl, o)
                    except:
                        await client.say("{} Looks like there was an error!\nMake sure the bot has the required permissions in that server!\nFor any help contact a bot administrator.".format(error_img))
            except:
                await client.say("{} An unknown error has occured!".format(error_img))
    else:
        await client.say("{} This command can only be used by the bot's staff!".format(error_img))

# ad!link <server id>
@client.command(pass_context=True)
async def link(ctx, target = None):
    author = ctx.message.author
    if author.id in bot_mods or author.id in bot_admins:
        if target == None:
            await client.say("{} No server ID given.".format(error_img))
        else:
            await client.say("Searching for server... <a:typing:393848431413559296>")
            a = []
            for s in client.servers:
                if s.id == target:
                    await client.say("{} Server found ( {} )!".format(check_img, s.name))
                    a.append("+1")
                    try:
                        invs = await client.invites_from(s)
                        await client.say("The server's link is: {}".format(invs[0]))
                        break
                    except:
                        await client.say("{} Unable to collect invites from that server.\nMake sure the bot has the required permissions in that server.".format(error_img))
                        break
                else:
                    print("")
            if len(a) == 0:
                await client.say("{} Server not found.\nEither the bot is not in that server or it doesn't have the required permissions.".format(error_img))
            else:
                print("")
    else:
        await client.say("{} This command can only be used by the bot's staff!".format(error_img))

''' COMMANDS FOR BOT ADMINISTRATORS '''
# ad!mod <add/del> <user>
@client.command(pass_context=True)
async def mod(ctx, option = None, user: discord.User = None):
    author = ctx.message.author
    cnsl = client.get_channel(console_chnl)
    bm = client.get_channel(bot_mods_chnl)
    if author.id in bot_admins:
        if option == None or user == None:
            await client.say("{} Not all arguments were given!\nExamples:\n`ad!mod add @Bob`.\n`ad!mod del @Bob`.".format(error_img))
        else:
            if option == "add":
                if user.id in bot_mods:
                    await client.say("{} That user is already a bot moderator!".format(error_img))
                else:
                    await client.send_message(bm, "{}".format(user.id))
                    bot_mods.append(user.id)
                    await client.say("{} Added {} to the bot moderators list.".format(check_img, user.name))
                    msg = "```diff"
                    msg += "\n- ADD MOD -"
                    msg += "\n+ Author: {} ### {}".format(author, author.id)
                    msg += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                    msg += "\n+ Target: {} ### {}".format(user, user.id)
                    msg += "\n```"
                    await client.send_message(cnsl, msg)
            elif option == "del":
                if user.id in bot_mods:
                    async for message in client.logs_from(bm):
                        if message.content == user.id:
                            await client.delete_message(message)
                            break
                        else:
                            print("")
                    bot_mods.remove(user.id)
                    await client.say("{} Removed {} from the bot moderators list.".format(check_img, user.name))
                    msg = "```diff"
                    msg += "\n- DEL MOD -"
                    msg += "\n+ Author: {} ### {}".format(author, author.id)
                    msg += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                    msg += "\n+ Target: {} ### {}".format(user, user.id)
                    msg += "\n```"
                    await client.send_message(cnsl, msg)
                else:
                    await client.say("{} That user is not a bot moderator!".format(error_img))
            else:
                await client.say("{} Invalid option!\nOptions: `add`, `del`.")
    else:
        await client.say("{} This command can only be used by the bot's administrators.".format(error_img))

# ad!fbump <server id>
@client.command(pass_context=True)
async def fbump(ctx, target = None):
    author = ctx.message.author
    cnsl = client.get_channel(console_chnl)
    if author.id in bot_admins:
        if target == None:
            await client.say("{} No server ID given!".format(error_img))
        else:
            if target in normal_servers or target in special_servers:
                try:
                    server = client.get_server(target)
                    await client.say("{} Server found!\nBumping the server... <a:typing:393848431413559296>".format(check_img))
                    if server.id in normal_servers:
                        try:
                            msgs = []
                            found = []
                            sent = []
                            for m in normal_servers_msgs:
                                a = str(m)
                                if server.id in a:
                                    msgs.append(m)
                                    break
                                else:
                                    print("")
                            msg = msgs[0]
                            embed = discord.Embed(colour=0x00FFFF, description= "")
                            embed.title = ""
                            embed.set_footer(text=footer_text)
                            embed.add_field(name="forced bump", value="{}".format(msg))
                            for c in channels_ids:
                                try:
                                    chnl = client.get_channel(c)
                                    found.append("+1")
                                    await client.send_message(chnl, embed=embed)
                                    sent.append("+1")
                                except:
                                    print("")
                            await client.say("{} The server has been bumped on {}/{} servers!".format(check_img, len(sent), len(found)))
                            o = "```diff"
                            o += "\n- FORCE BUMP -"
                            o += "\n+ Author: {} ### {}".format(author, author.id)
                            o += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                            o += "\n+ Target: {} ### {}".format(server.name, server.id)
                            o += "\n```"
                            await client.send_message(cnsl, o)
                        except:
                            await client.say("{} Error in bumping the server!\nFor any help use `ad!support`.".format(error_img))
                    elif server.id in special_servers:
                        await client.say("Bumping... <a:typing:393848431413559296>")
                        try:
                            msgs = []
                            found = []
                            sent = []
                            for m in special_servers_msgs:
                                a = str(m)
                                if server.id in a:
                                    msgs.append(m)
                                    break
                                else:
                                    print("")
                            msg = msgs[0]
                            embed = discord.Embed(colour=0xFFAE00, description= "")
                            embed.title = ""
                            embed.set_image(url="{}".format(special_server_img))
                            embed.set_footer(text=footer_text)
                            embed.add_field(name="forced bump", value="{}".format(msg))
                            for c in channels_ids:
                                try:
                                    chnl = client.get_channel(c)
                                    found.append("+1")
                                    await client.send_message(chnl, embed=embed)
                                    sent.append("+1")
                                except:
                                    print("")
                            await client.say("{} The server has been bumped on {}/{} servers!".format(check_img, len(sent), len(found)))
                            o = "```diff"
                            o += "\n- FORCE BUMP -"
                            o += "\n+ Author: {} ### {}".format(author, author.id)
                            o += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                            o += "\n+ Target: {} ### {}".format(server.name, server.id)
                            o += "\n```"
                            await client.send_message(cnsl, o)
                        except:
                            await client.say("{} Error in bumping the server!".format(error_img))
                    else:
                        await client.say("{} Looks like that server isn't setup.".format(error_img))
                except:
                    await client.say("{} Error in bumping the server!".format(error_img))
            else:
                await client.say("{} Server not found!\nMake sure the bot is in that server and it has the required permissions.".format(error_img))
    else:
        await client.say("{} This command can only be used by the bot's administrators.".format(error_img))

# ad!announce <text>
@client.command(pass_context=True)
async def announce(ctx, *, args = None):
    author = ctx.message.author
    cnsl = client.get_channel(console_chnl)
    if author.id in bot_admins:
        if args == None:
            await client.say("{} No text given!\nExample: `ad!announce New update!`.".format(error_img))
        elif len(str(args)) > 1900:
            await client.say("{} The text cannot be longer than 1900 characters.".format(error_img))
        else:
            await client.say("Sending announcement... <a:typing:393848431413559296>")
            done = []
            fail = []
            pos = []
            try:
                for c in log_channels_ids:
                    pos.append("+1")
                    embed = discord.Embed(colour=0xFF0000, description= "")
                    embed.title = ""
                    embed.set_image(url="{}".format(announcement_img))
                    embed.set_footer(text=footer_text)
                    m = "{}".format(args)
                    m += "\n~~__**= = = = = = = = = = = = = = = = = = = =**__~~"
                    m += "\n:label: Message by: `{} ### {}`".format(author, author.id)
                    m += "\n:arrows_counterclockwise: Position: {}/{}".format(len(pos), len(log_channels_ids))
                    m += "\n~~__**= = = = = = = = = = = = = = = = = = = =**__~~"
                    embed.add_field(name="announcement", value="{}".format(m))
                    try:
                        dest = client.get_channel(c)
                        await client.send_message(dest, embed=embed)
                        done.append("+1")
                    except:
                        fail.append("+1")
                o = "```diff"
                o += "\n- ANNOUNCEMENT -"
                o += "\n+ Author: {} ### {}".format(author, author.id)
                o += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                o += "\n+ Sent: {}".format(len(done))
                o += "\n+ Failed: {}".format(len(fail))
                o += "\n+ Text:"
                o += "\n```"
                o += "\n{}".format(args)
                await client.send_message(cnsl, o)
                await client.say("{} Finished!\nCheck the console for more information.".format(check_img))
            except:
                await client.say("{} There was an error while trying to send the announcements!".format(error_img))
    else:
        await client.say("{} This command can only be used by the bot's administrators.".format(error_img))

# ad!force
@client.command(pass_context=True)
async def force(ctx):
    author = ctx.message.author
    if author.id in bot_admins:
        await client.say("Forcing advertisements... <a:typing:393848431413559296>")
        try:
            total = []
            normal = []
            special = []
            fail = []
            cnsl = client.get_channel(console_chnl)
            ss = []
            ns = []
            a_s = []
            cs = []
            for s in client.servers:
                if s.id in banned_servers:
                    print("[FORCED AD] SERVER IS BANNED")
                elif s.id in toggled_servers:
                    print("[FORCED AD] SERVER IS TOGGLED")
                elif s.id in special_servers:
                    ss.append(s.id)
                    a_s.append(s.id)
                    print("[FORCED AD] SERVER FOUND (S)")
                elif s.id in normal_servers:
                    ns.append(s.id)
                    a_s.append(s.id)
                    print("[FORCED AD] SERVER FOUND (N)")
                else:
                    print("[FORCED AD] SERVER NOT FOUND IN ANY LISTS")
            print("[FORCED AD INFO]\nnormal servers: {}\nspecial servers: {}\nall servers: {}".format(ns, ss, a_s))
            for c in channels_ids:
                try:
                    c1 = client.get_channel(c)
                    for srv in client.servers:
                        if srv in toggled_servers:
                            if c1 in srv.channels:
                                print("[FORCED AD] CHANNEL IS TOGGLED")
                            else:
                                cs.append(c)
                                print("[FORCED AD] CHANNEL FOUND")
                        else:
                            if c1 in srv.channels:
                                cs.append(c)
                                print("[FORCED AD] CHANNEL FOUND")
                            else:
                                print("[FORCED AD] CHANNEL NOT FOUND")
                except:
                    print("[FORCED AD] FAILED TO GET CHANNEL")
            print("[FORCED AD INFO]\nchannels: {}".format(cs))
            for c in cs:
                try:
                    chnl = client.get_channel(c)
                    co = random.choice(a_s)
                    if co in ss:
                        print("[FORCED AD] CHOICE: S")
                        m = random.choice(special_servers_msgs)
                        embed = discord.Embed(colour=0xFFAE00, description= "")
                        embed.title = ""
                        embed.set_image(url="{}".format(special_server_img))
                        embed.set_footer(text=footer_text)
                        embed.add_field(name="forced special advertisement", value="{}".format(m))
                        print("[FORCED AD] MESSAGE CREATED")
                    else:
                        print("[FORCED AD] CHOICE: N")
                        m = random.choice(normal_servers_msgs)
                        embed = discord.Embed(colour=0x00FFFF, description= "")
                        embed.title = ""
                        embed.set_footer(text=footer_text)
                        embed.add_field(name="forced advertisement", value="{}".format(m))
                        print("[FORCED AD] MESSAGE CREATED")
                    try:
                        await client.send_message(chnl, embed=embed)
                        print("[FORCED AD] SENT")
                        if co in ss:
                            special.append("+1")
                        else:
                            normal.append("+1")
                        total.append("+1")
                    except:
                        fail.append("+1")
                except:
                    print("[FORCED AD ERRORS] MAIN")
            log = "```diff"
            log += "\n- FORCED ADVERTISEMENT -"
            log += "\n+ Author: {} ### {}".format(author, author.id)
            log += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
            log += "\n+ Total sent: {}".format(len(total))
            log += "\n+ Failed: {}".format(len(fail))
            log += "\n+ Normal sent: {}".format(len(normal))
            log += "\n+ Special sent: {}".format(len(special))
            log += "\n```"
            await client.send_message(cnsl, log)
            await client.say("{} Finished!\nCheck the console for more information.".format(check_img))
            print("[FORCED AD] FINISHED")
        except:
            print("[FORCED AD ERRORS] GLOBAL")
    else:
        await client.say("{} This command can only be used by the bot's administrators.".format(error_img))

# ad!log <title> | <message>
@client.command(pass_context=True)
async def log(ctx, *, args = None):
    author = ctx.message.author
    cnsl = client.get_channel(console_chnl)
    if author.id in bot_admins:
        if args == None:
            await client.say("{} Not all arguments were given!\nExample: `ad!log SMALL UPDATE | The bot just got updated.`.".format(error_img))
        elif len(str(args)) > 1500:
            await client.say("{} The arguments cannot be longer than 1500 characters.".format(error_img))
        else:
            try:
                args.split('|')
            except:
                await client.say("{} The command was used wrongly!\nExample: `ad!log SMALL UPDATE | The bot just got updated.`.".format(error_img))
            a = args.split('|')
            if len(a) != 2:
                await client.say("{} The command was used wrongly!\nExample: `ad!log SMALL UPDATE | The bot just got updated.`.".format(error_img))
            else:
                await client.say("Sending logs... <a:typing:393848431413559296>")
                done = []
                fail = []
                pos = []
                try:
                    for c in log_channels_ids:
                        pos.append("+1")
                        m = "```diff"
                        m += "\n- FORCED LOG -"
                        m += "\n- {} -".format(a[0])
                        m += "\n+ Logged by: {} ### {}".format(author, author.id)
                        m += "\n+ Position: {}/{}".format(len(pos), len(log_channels_ids))
                        m += "\n```"
                        m += "\n{}".format(a[1])
                        try:
                            dest = client.get_channel(c)
                            await client.send_message(dest, m)
                            done.append("+1")
                        except:
                            fail.append("+1")
                    o = "```diff"
                    o += "\n- FORCED LOG -"
                    o += "\n+ Author: {} ### {}".format(author, author.id)
                    o += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                    o += "\n+ Sent: {}".format(len(done))
                    o += "\n+ Failed: {}".format(len(fail))
                    o += "\n+ Text:"
                    o += "\n```"
                    o += "\n{}".format(args)
                    await client.send_message(cnsl, o)
                    await client.say("{} Finished!\nCheck the console for more information.".format(check_img))
                except:
                    await client.say("{} There was an error while trying to send the logs!".format(error_img))
    else:
        await client.say("{} This command can only be used by the bot's administrators.".format(error_img))

# ad!special <add/del> <server id>
@client.command(pass_context=True)
async def special(ctx, option = None, target = None):
    author = ctx.message.author
    cnsl = client.get_channel(console_chnl)
    chnl1 = client.get_channel(normal_servers_chnl)
    chnl2 = client.get_channel(normal_servers_msgs_chnl)
    c1 = client.get_channel(special_servers_chnl)
    c2 = client.get_channel(special_servers_msgs_chnl)
    if author.id in bot_admins:
        if option == None or target == None:
            await client.say("{} Not all arguments were given!\nExamples:\n`ad!special add 440108166789988353`.\n`ad!special del 440108166789988353`.".format(error_img))
        elif option == "add":
            if target in special_servers:
                await client.say("{} That server is already in the special list.".format(error_img))
            else:
                try:
                    await client.say("Searching for the server... <a:typing:393848431413559296>")
                    s = client.get_server(target)
                    await client.say("{} Server found ( {} )!\nAdding the server to the special list... <a:typing:393848431413559296>".format(check_img, s.name))
                    try:
                        if s.id in normal_servers:
                            log = "```diff"
                            log += "\n--- STARTING SPECIAL LOG ---"
                            log += "\n= Searching for used message..."
                            for i in normal_servers_msgs:
                                a = str(i)
                                if s.id in i:
                                    log += "\n+ Message found!"
                                    special_servers_msgs.append(i)
                                    await client.send_message(c2, i)
                                    normal_servers_msgs.remove(i)
                                    break
                                else:
                                    print("")
                            log += "\n= Saving message..."
                            special_servers.append(s.id)
                            normal_servers.remove(s.id)
                            log += "\n+ Saved!"
                            log += "\n= Removing message from old lists..."
                            async for message in client.logs_from(chnl1):
                                if message.content == s.id:
                                    await client.delete_message(message)
                                    log += "\n+ Removed!"
                                    break
                                else:
                                    print("")
                            log += "\n= Removing server ID from old lists..."
                            async for message in client.logs_from(chnl2):
                                a = str(message.content)
                                if s.id in a:
                                    await client.delete_message(message)
                                    log += "\n+ Removed!"
                                    break
                                else:
                                    print("")
                            log += "\n= Saving new data..."
                            await client.send_message(c1, s.id)
                            log += "\n+ Saved!"
                            log += "\n= Sending results..."
                            log += "\n+ Finished!"
                            log += "\n--- CLOSING SPECIAL LOG ---"
                            log += "\n```"
                            b = []
                            for i in s.channels:
                                if i.id in log_channels_ids:
                                    t = "```diff"
                                    t += "\n- SPECIAL ADVERTISEMENTS -"
                                    t += "\n+ This server has been added to the special list and it will now have special advertisements."
                                    t += "\n+ Added by: {} ### {}".format(author, author.id)
                                    t += "\n```"
                                    await client.send_message(i, log)
                                    await client.send_message(i, t)
                                    b.append(i.id)
                                    break
                                else:
                                    print("")
                            if len(b) == 0:
                                await client.say(log)
                                await client.say("{} The server should now have special advertisements!".format(check_img))
                            else:
                                await client.say("{} The server should now have special advertisements!\nYou can find the log in <#{}>.".format(check_img, b[0]))
                            o = "```diff"
                            o += "\n- ADD SPECIAL -"
                            o += "\n+ Author: {} ### {}".format(author, author.id)
                            o += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                            o += "\n+ Target: {}".format(target)
                            o += "\n```"
                            await client.send_message(cnsl, o)
                        else:
                            await client.say("{} That server isn't setup.\nTry again once the server has been setup.".format(error_img))
                    except:
                        log += "\n- ^ Error!"
                        log += "\n--- CLOSING SPECIAL LOG ---"
                        log += "\n```"
                        await client.say(log)
                        await client.say("{} There was an error while trying to add the server to the special list.".format(error_img))
                except:
                    await client.say("{} Server not found!\nMake sure the bot is in that server and it has the required permissions.".format(error_img))
        elif option == "del":
            try:
                await client.say("Searching for the server... <a:typing:393848431413559296>")
                s = client.get_server(target)
                await client.say("{} Server found ( {} )!\nRemoving the server from the special list... <a:typing:393848431413559296>".format(check_img, s.name))
                try:
                    if s.id in special_servers:
                        log = "```diff"
                        log += "\n--- STARTING SPECIAL LOG ---"
                        log += "\n= Searching for used message..."
                        for i in special_servers_msgs:
                            a = str(i)
                            if s.id in a:
                                special_servers_msgs.remove(i)
                                log += "\n+ Message found!"
                                break
                            else:
                                print("")
                        log += "\n= Removing message..."
                        special_servers.remove(s.id)
                        log += "\n+ Removed!"
                        log += "\n= Removing old data 1/2..."
                        async for message in client.logs_from(c1):
                            a = str(message.content)
                            if s.id in a:
                                await client.delete_message(message)
                                log += "\n+ Removed 1/2!"
                                break
                            else:
                                print("")
                        log += "\n= Removing old data 2/2..."
                        async for message in client.logs_from(c2):
                            a = str(message.content)
                            if s.id in a:
                                await client.delete_message(message)
                                log += "\n+ Removed 2/2!"
                                break
                            else:
                                print("")
                        log += "\n= Sending results..."
                        log += "\n+ Finished!"
                        log += "\n--- CLOSING SPECIAL LOG ---"
                        log += "\n```"
                        b = []
                        for i in s.channels:
                            if i.id in log_channels_ids:
                                t = "```diff"
                                t += "\n- SPECIAL ADVERTISEMENTS -"
                                t += "\n+ This server has been removed from the special list and will no longer get special advertisements."
                                t += "\n+ Removed by: {} ### {}".format(author, author.id)
                                t += "\n```"
                                await client.send_message(i, log)
                                await client.send_message(i, t)
                                b.append(i.id)
                                break
                            else:
                                print("")
                        if len(b) == 0:
                            await client.say(log)
                            await client.say("{} The server has been removed from the special list!".format(check_img))
                        else:
                            await client.say("{} The server has been removed from the special list!\nYou can find the special log in <#{}>.".format(check_img, b[0]))
                        o = "```diff"
                        o += "\n- DEL SPECIAL -"
                        o += "\n+ Author: {} ### {}".format(author, author.id)
                        o += "\n+ From: {} ### {}".format(ctx.message.server.name, ctx.message.server.id)
                        o += "\n+ Target: {}".format(target)
                        o += "\n```"
                        await client.send_message(cnsl, o)
                    else:
                        await client.say("{} The server is not in the special list.".format(error_img))
                except:
                    log += "\n- ^ Error!"
                    log += "\n--- CLOSING SPECIAL LOG ---"
                    log += "\n```"
                    await client.say(log)
                    await client.say("{} There was an error while trying to remove the server from the special list.".format(error_img))
            except:
                await client.say("{} Server not found!\nMake sure the bot is in that server and it has the required permissions.".format(error_img))
        else:
            await client.say("{} Invalid option!\nOptions: `add`, `del`.".format(error_img))
    else:
        await client.say("{} This command can only be used by the bot's administrators.".format(error_img))

# ad!say <text>
@client.command(pass_context=True)
async def say(ctx, *, args = None):
    author = ctx.message.author
    if author.id in bot_admins:
        if args == None:
            await client.say("{} No text given!".format(error_img))
        else:
            if len(str(args)) > 1900:
                await client.say("{} The text cannot be longer than 1900 characters.".format(error_img))
            else:
                await client.say("{}".format(args))
    else:
        await client.say("{} This command can only be used by the bot's administrators.".format(error_img))

# TURNS THE BOT ON
client.run(os.environ['BOT_TOKEN'])
