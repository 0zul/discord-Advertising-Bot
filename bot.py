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
footer_text = "[+]Advertisement Bot[+]"

help_msg1 = "**__COMMANDS FOR EVERYONE__**"
help_msg1 += "\n "
help_msg1 += "\n`ad!help` - Gives you a list of commands."
help_msg1 += "\n`ad!ping` - Pings the bot. Used to check if the bot is lagging."
help_msg1 += "\n`ad!support` - Gives you the support server link and a list of bot moderators.`"
help_msg1 += "\n`ad!info` - Shows information about the bot."
help_msg1 += "\n`ad!servers` - Gives you a list of servers that aren't setup."
help_msg1 += "\n`ad!rnd` - Gives you a random server."
help_msg1 += "\n`ad!serverinfo [server id]` - Shows information about a server."
help_msg1 += "\n`ad!invite` - Gives you the invite link for the bot."
help_msg1 += "\n`ad!tos` - Gives you bot's rules and TOS."
help_msg1 += "\n`ad!suggest <suggestion>` - Sends a suggestion to the bot moderators."
help_msg1 += "\n`ad!report <user/server> <id> <reason>` - Reports a server or user to the bot moderators."
help_msg1 += "\n`ad!uptime` - Shows you how long the bot's been online for."

help_msg2 = "**__COMMANDS FOR SERVER ADMINISTRATORS__**"
help_msg2 += "\n "
help_msg2 += "\n`ad!setup [channel] [message]` - Shows you help on how to setup your server or starts the setup if you put the arguments."
help_msg2 += "\n`ad!unsetup` - Removes your server from all lists and stops advertising it."
help_msg2 += "\n`ad!test` - Checks if your server is setup correctly."

help_msg3 = "**__COMMANDS FOR BOT MODERATORS__**"
help_msg3 += "\n "
help_msg3 += "\n`ad!msg <user/server> <id> <message>` - DMs an user or the owner of the specified server."
help_msg3 += "\n`ad!ban <user/server> <id> <reason>` - Bans an user from all servers or prevents a server from using the bot."
help_msg3 += "\n`ad!unban <user/server> <id>` - Unbans an user from all servers or gives access to a server that was banned."
help_msg3 += "\n`ad!reset <server id>` - Removes a server from all lists."
help_msg3 += "\n`ad!ignore <server id>` - Ignores a server. Ignored servers won't be shown in the lists."

help_msg4 = "**__COMMANDS FOR BOT ADMINISTRATORS__**"
help_msg4 += "\n "
help_msg4 += "\n`ad!mod <add/del> <user>` - Adds or removes a bot moderator."
help_msg4 += "\n`ad!special <add/del> <server id> - Adds or removes a server from the special list.`"
help_msg4 += "\n`ad!announce <text>` - Sends an announcement to all servers."
help_msg4 += "\n`ad!force` - Forces the bot to advertise."

tos_msg = "**__By using this bot you agree to the following:__**"
tos_msg += "\n**~~=~~** Letting the bot ban and unban users that are known for harming other discord servers and/or breaking the discord TOS!"
tos_msg += "\n**~~=~~** Letting the bot create invite linnks for your server!"
tos_msg += "\n**~~=~~** Letting the bot send advertisements for other discord servers on your server and sending your server links to other servers!"
tos_msg += "\n**~~=~~** Giving the required permissions to the bot!"
tos_msg += "\n**~~=~~** Letting the bot get your server information such as members, server id, channel count, owner id etc."
tos_msg += "\n "
tos_msg += "\n**__Bot rules:__**"
tos_msg += "\n**~~=~~** Everyone must be able to see the channel that the bot uses!"
tos_msg += "\n**~~=~~** Spamming bot commands or trying to make the bot lag is not allowed!"
tos_msg += "\n**~~=~~** Asking to become a bot moderator is not allowed!"
tos_msg += "\n**~~=~~** Only DM the bot administrators or bot moderators if you have any questions or if you need help!"
tos_msg += "\n**~~=~~** Do not send stupid suggestions!"
tos_msg += "\n**~~=~~** Do not false report users or servers!"
tos_msg += "\n**~~=~~** Breaking any of these rules will get you and/or your server banned!"
tos_msg += "\n "
tos_msg += "\n**__You can use `ad!help` to see a list of commands!__**"

console_channel = '440108804844290048'
suggestions_channel = '441542347453366272'
reports_channel = '441542722348908562'
backups_channel = '441543178177478658'
support_server_id = "440108166789988353"

test_msg_img = "https://i.imgur.com/3zHcRpt.png"
announcement_img = "https://i.imgur.com/2m9gzUm.png"
new_server_img = "https://i.imgur.com/79FgWOd.png"
special_server_img = "https://i.imgur.com/G5SWYtL.png"

bot_mods = ['412201413335056386', '278478326014803968', '288872682492133378', '367417841563074570']
bot_admins = ["412201413335056386"]

servers_ids = ['424282235554889742', '384884562582437889', '430564956497510410', '416108185498419206', '439448228165844993', '441652820148748335', '439526724854743040', '286875870176477184', '412662563789078549', '445551461858803735', '414089074870321153', '441712376358895617', '440314931212976128', '445766228594917407', '442108025935888385']
special_servers_ids = ['414089074870321153']

channels_ids = ['439629288891875340', '401161763749494785', '442692512889438209', '440027866810548234', '440045431733354497', '441664448269385739', '441684937393831947', '443489988936597524', '442033265637982218', '437742612078919681', '445555285101379594', '432135342569553920', '441966421765783562', '443535295971983371', '446281190677282816', '442135555678011394']

servers_msgs = ['.\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:busts_in_silhouette: 32 members!\n:credit_card: ID: 424282235554889742\n:link: Link: http://discord.gg/UX52RQb\n**~~= = = = = = = = = = = = = == = = = =~~**', 'This is Maple Realm™, a chatting server, where you can just hang out with your friends!\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:busts_in_silhouette: 232 members!\n:credit_card: ID: 384884562582437889\n:link: Link: http://discord.gg/Zcz6nB8\n**~~= = = = = = = = = = = = = == = = = =~~**', 'This is a social server as well as abit of a game server made by @big mami , here you can talk about anything with other cool people.\nWe hope to see you all there!\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:busts_in_silhouette: 50 members!\n:credit_card: ID: 430564956497510410\n:link: Link: http://discord.gg/6qhtWT2\n**~~= = = = = = = = = = = = = == = = = =~~**', 'if u like roblox join\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:busts_in_silhouette: 45 members!\n:credit_card: ID: 416108185498419206\n:link: Link: http://discord.gg/AHyrjCm\n**~~= = = = = = = = = = = = = == = = = =~~**', '.\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:busts_in_silhouette: 88 members!\n:credit_card: ID: 439448228165844993\n:link: Link: http://discord.gg/hHbhyR2\n**~~= = = = = = = = = = = = = == = = = =~~**', 'Welcome To The VinternoZ Community.A Gaming Community Owned by VinternoZ#3843.Play,Make Friends And have fun!\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:busts_in_silhouette: 21 members!\n:credit_card: ID: 441652820148748335\n:link: Link: http://discord.gg/akJ4Hcs\n**~~= = = = = = = = = = = = = == = = = =~~**', "ad!setup <#435392629769764864>  welcome everyone to World of Music A server of music If u like music u will like this server and i'm hoping for it to get more active when some of you join i need a couple more staff who will be active and not lazy\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Name: World of Music\n:busts_in_silhouette: 85 members!\n:credit_card: ID: 427289292692258826\n:link: Link: http://discord.gg/997ZeeT\n**~~= = = = = = = = = = = = = == = = = =~~**", "Thanks for checking out Five Star Roleplay! We are a roleplaying community based on the popular GTA5 modification FiveM! Join us if you're looking for a cool gaming community!\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Name: Five Star Roleplay\n:busts_in_silhouette: 44 members!\n:credit_card: ID: 439526724854743040\n:link: Link: http://discord.gg/4bP6xjf\n**~~= = = = = = = = = = = = = == = = = =~~**", "Do you search for cool bots?  (like game bots, verification bots). If yes that's the right place for you! Join and enjoy!\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Name: The Bot Farms\n:busts_in_silhouette: 81 members!\n:credit_card: ID: 401126058243522560\n:link: Link: http://discord.gg/PU2HtW7\n**~~= = = = = = = = = = = = = == = = = =~~**", '🍪 Friendly Members 🍪 \n🎶 Voice and Music Room 🎶 \n⚔  Roleplaying ⚔ \n🐹  Uniques Roles 🐹 \n☀  Leveling sysem 🌕\n🍆 Hentai channels (verified) 🍑 \n🔨  Events coming soon! 🔨\n🆕 Building more and improving! 🆕\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Name: Role play and Hentai Gods\n:busts_in_silhouette: 25 members!\n:credit_card: ID: 388498690081423370\n:link: Link: http://discord.gg/ej9uFF3\n**~~= = = = = = = = = = = = = == = = = =~~**', 'Wanna have fun with bots? JOIN!\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Name: BOT Playplace and Leisure Lounge OFFICIAL(NTRS)\n:busts_in_silhouette: 56 members!\n:credit_card: ID: 337458654682808320\n:link: Link: http://discord.gg/hQtBY2s\n**~~= = = = = = = = = = = = = == = = = =~~**', 'Special V.I.P Community Super Chilling server\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Name: :BattleGaming=Hurricane G a m e r s:\n:busts_in_silhouette: 59 members!\n:credit_card: ID: 439033705693184002\n:link: Link: http://discord.gg/dK92PdW\n**~~= = = = = = = = = = = = = == = = = =~~**', 'Looking for a developing community? Well look no more! Arce Deving Community offers you to get help from other users and meet new friends! Join and see the magic!\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Name: Arce Deving Community\n:busts_in_silhouette: 12 members!\n:credit_card: ID: 444516771794255892\n:link: Link: http://discord.gg/AWgAMYY\n**~~= = = = = = = = = = = = = == = = = =~~**', '**__~~`>>>>>>>>>>×××<<<<<<<<<<`~~__**\n**__~~`>>>>>>>>>>×××<<<<<<<<<<`~~__**\n__**~~====================~~**__\n❄ CHILL PEOPLE ❄ \n💯 TONS OF MEMES 💯 \n🌌 ANIME CHANNELS 🌌 \n🕹 GAMING CHANNELS 🕹 \n🔞 NSFW CHANNELS 🔞 \n🙂 VENTING AND ADVICE CHANNELS 🙂 \n💻 PROGRAMMING CHANNELS 💻 \n🛡 CLEAN CHATS 🛡 \n🌐 RARE everyone AND here TAGS 🌐 \n🎁 EVENTS AND 24/7 GIVEAWAYS 🎁 \n👥 PARTNERSHIPS 👥 \n🤖 FUN BOTS 🤖 \n🗺 SPECIAL ADVERTISEMENTS FOR FREE 🗺 \n📦 AND A LOT MORE 📦 \n__**~~====================~~**__\n**__~~`>>>>>>>>>>×××<<<<<<<<<<`~~__**\n**__~~`>>>>>>>>>>×××<<<<<<<<<<`~~__**\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Name: The Realm Of Darkness\n:busts_in_silhouette: 383 members!\n:credit_card: ID: 414089074870321153\n:link: Link: http://discord.gg/uW5whT5\n**~~= = = = = = = = = = = = = == = = = =~~**', 'Join my discord please\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Name: THE SQUAD\n:busts_in_silhouette: 34 members!\n:credit_card: ID: 441712376358895617\n:link: Link: http://discord.gg/U7Yejx7\n**~~= = = = = = = = = = = = = == = = = =~~**', 'game\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Name: Virtual Junkies Land\n:busts_in_silhouette: 13 members!\n:credit_card: ID: 440314931212976128\n:link: Link: http://discord.gg/dqFkeRK\n**~~= = = = = = = = = = = = = == = = = =~~**', "Special server let's try to get up to 100 members and make it active last old server I had almost 100 member until someone ruined it but it will not happen again join\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Name: The Community Hurricanes 🌀\n:busts_in_silhouette: 9 members!\n:credit_card: ID: 445766228594917407\n:link: Link: http://discord.gg/AsMVSvT\n**~~= = = = = = = = = = = = = == = = = =~~**", '🍑HENTAI HEAVEN🍆\n\n |WARNING]\n🚫 WE DO NOT ACCEPT USERS UNDER THE AGE OF 16 🚫\n\n👪 Growing fast and strong 👪 🎉 Giveaways all the time :tada\n💦Tons of nsfw and lots of hentai, porn, sex, and nudes and lots more💦\n🛡Active chat🛡\n🤝 We Partner with everyone 🤝\n\n[Thanks! We hope to see you here!]\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Name: Hentai Heaven\n:busts_in_silhouette: 1471 members!\n:credit_card: ID: 442108025935888385\n:link: Link: http://discord.gg/s3MhWQm\n**~~= = = = = = = = = = = = = == = = = =~~**', ':peach:HENTAI HEAVEN:eggplant:\n\n |WARNING]\n:no_entry_sign: WE DO NOT ACCEPT USERS UNDER THE\nAGE OF 16 :no_entry_sign:\n \n:family: Growing fast and strong :family:\n :tada: Giveaways all the time :tada\n:sweat_drops:Tons of nsfw and lots of hentai, porn, sex, and nudes and lots more:sweat_drops:\n:shield:Active chat:shield:\n:handshake: We Partner with everyone :handshake:\n \n[Thanks! We hope to see you here!]\n  \n= = = = = = = = = = = = = == = = = =\n:label: Name: Hentai Heaven\n:busts_in_silhouette: 1471 members!\n:credit_card: ID: 442108025935888385\n:link: Link:\nhttp://discord.gg/s3MhWQm\n= = = = = = = = = = = = = == = = = =']

special_servers_msgs = ['**__~~`>>>>>>>>>>×××<<<<<<<<<<`~~__**\n**__~~`>>>>>>>>>>×××<<<<<<<<<<`~~__**\n__**~~====================~~**__\n❄ CHILL PEOPLE ❄ \n💯 TONS OF MEMES 💯 \n🌌 ANIME CHANNELS 🌌 \n🕹 GAMING CHANNELS 🕹 \n🔞 NSFW CHANNELS 🔞 \n🙂 VENTING AND ADVICE CHANNELS 🙂 \n💻 PROGRAMMING CHANNELS 💻 \n🛡 CLEAN CHATS 🛡 \n🌐 RARE everyone AND here TAGS 🌐 \n🎁 EVENTS AND 24/7 GIVEAWAYS 🎁 \n👥 PARTNERSHIPS 👥 \n🤖 FUN BOTS 🤖 \n🗺 SPECIAL ADVERTISEMENTS FOR FREE 🗺 \n📦 AND A LOT MORE 📦 \n__**~~====================~~**__\n**__~~`>>>>>>>>>>×××<<<<<<<<<<`~~__**\n**__~~`>>>>>>>>>>×××<<<<<<<<<<`~~__**\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Name: The Realm Of Darkness\n:busts_in_silhouette: 383 members!\n:credit_card: ID: 414089074870321153\n:link: Link: http://discord.gg/uW5whT5\n**~~= = = = = = = = = = = = = == = = = =~~**']

servers_links = ['http://discord.gg/s3MhWQm', 'http://discord.gg/DkPFrBg', 'http://discord.gg/UX52RQb', 'http://discord.gg/Zcz6nB8', 'http://discord.gg/6qhtWT2', 'http://discord.gg/AHyrjCm', 'http://discord.gg/hHbhyR2', 'http://discord.gg/akJ4Hcs', 'http://discord.gg/pWpUwC9', 'http://discord.gg/6aW4vBQ', 'http://discord.gg/vayR7Tf', 'http://discord.gg/uW5whT5', 'http://discord.gg/Ys768Nj', 'http://discord.gg/U7Yejx7', 'http://discord.gg/dqFkeRK', 'http://discord.gg/AsMVSvT', 'http://discord.gg/s3MhWQm']
special_servers_links = ['https://discord.gg/jN6CcpY']

ignored_servers_ids = ['412201413335056386', '278478326014803968', '288872682492133378', '367417841563074570', '438095161541787648', '426162708484980739', '440652723504021504', '437321903066185729', '440108166789988353', '441003406371454986', '444866585661014016', '443834435620831232', '413458499176235017', '337458654682808320', '440974481905811458', '440314931212976128', '439749890156003328', '439605324593364992', '343820652697878539', '443907495371735042', '433822549273739264', '418893238490103808', '401126058243522560', '395624386075426826', '367836965242011649', '434776674421309441', '412088408463114240', '421435329484947458', '410077580658606081', '390912888954421249', '415719893854322719', '443601722183778324', '413458499176235017', '439538127586066432', '440974481905811458', '439749890156003328', '433822549273739264', '444516771794255892', '441651763792183316', '418893238490103808', '395624386075426826', '401126058243522560', '395624386075426826', '412088408463114240', '421435329484947458', '445966355494338561', '414949377241776148', '410077580658606081', '410247327559843851', '419839275333320704', '441568242335612948', '390912888954421249', '415719893854322719', '323889558594912266', '443601722183778324']
banned_servers_ids = []
toggled_servers = []

ut_seconds = []
ut_minutes = []
ut_hours = []

# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    t1 = time.perf_counter()
    await client.change_presence(game=discord.Game(name='ad!help | ad!support'))
    await client.wait_until_ready()
    chnl = client.get_channel(console_channel)
    msg = "```diff"
    msg += "\n- LOGGED IN -"
    msg += "\n+ Name: {}".format(client.user.name)
    msg += "\n+ ID: {}".format(client.user.id)
    msg += "\n+ Total Server Count: {}".format(len(client.servers))
    msg += "\n+ Normal Servers: {}".format(len(servers_ids))
    msg += "\n+ Special Servers: {}".format(len(special_servers_ids))
    msg += "\n+ Ignored Servers: {}".format(len(ignored_servers_ids))
    msg += "\n+ Bot Moderator Count: {}".format(len(bot_mods))
    msg += "\n+ Bot Administrator Count: {}".format(len(bot_admins))
    t2 = time.perf_counter()
    msg += "\n+ Ping: {}".format(round((t2-t1)*1000))
    msg += "```"
    await client.send_message(chnl, msg)

# SERVER COUNT
@client.event
async def on_server_join(server):
    await client.wait_until_ready()
    chnl = client.get_channel(console_channel)
    await client.send_message(chnl, "```diff\n- JOINED SERVER -\n+ Name: {}\n+ ID: {}\n```".format(server.name, server.id))
    try:
        await client.send_message(server.owner, tos_msg)
    except:
        print("")

@client.event
async def on_server_remove(server):
    await client.wait_until_ready()
    chnl = client.get_channel(console_channel)
    await client.send_message(chnl, "```diff\n- LEFT SERVER -\n+ Name: {}\n+ ID: {}\n```".format(server.name, server.id))
    if server.id in servers_ids or server.id in special_servers_ids:
        try:
            servers_ids.remove(server.id)
            for msg in servers_msgs:
                a = str(msg)
                if server.id in a:
                    servers_msgs.remove(msg)
                else:
                    print("")
            if server.id in special_servers_ids:
                spcial_servers_ids.remove(server.id)
                for msg1 in special_servers_msgs:
                    b = str(msg1)
                    if server.id in b:
                        special_servers_msgs.remove(msg1)
                    else:
                        print("")
            else:
                print("")
        except:
            print("")
    else:
        print("")

# AUTO ADVERTISING SYSTEM
async def autoad():
    await client.wait_until_ready()
    while not client.is_closed:
        cnsl = client.get_channel(console_channel)
        nor = []
        spe = []
        total = []
        failed = []
        try:
            for channel in channels_ids:
                c = random.randint(0, 10)
                if c <= 6:
                    m = random.choice(servers_msgs)
                    embed = discord.Embed(colour=0x00FFF7, description= "")
                    embed.title = ""
                    embed.set_footer(text=footer_text)
                    embed.add_field(name="advertisement", value="{}".format(m))
                else:
                    m = random.choice(special_servers_msgs)
                    embed = discord.Embed(colour=0xFFAE00, description= "")
                    embed.title = ""
                    embed.set_image(url="{}".format(special_server_img))
                    embed.set_footer(text=footer_text)
                    embed.add_field(name="special advertisement", value="{}".format(m))
                try:
                    dest = client.get_channel(channel)
                    await client.send_message(dest, embed=embed)
                    if c <= 6:
                        nor.append("+1")
                    else:
                        spe.append("+1")
                    total.append("+1")
                except:
                    failed.append("+1")
            msg = "```diff"
            msg += "\n- AUTO ADVERTISEMENT -"
            msg += "\n+ Total sent: {}".format(len(total))
            msg += "\n+ Failed: {}".format(len(failed))
            msg += "\n+ Special sent: {}".format(len(spe))
            msg += "\n+ Normal sent: {}".format(len(nor))
            msg += "\n```"
            await client.send_message(cnsl, msg)
        except:
            print("")
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
    await client.say("Sliding in your DMs...")
    try:
        await client.send_message(author, help_msg1)
        await client.send_message(author, help_msg2)
        await client.send_message(author, help_msg3)
        await client.send_message(author, help_msg4)
    except:
        await client.say(":octagonal_sign: Make sure the bot has permission to send you DMs!")

# ad!ping
@client.command(pass_context=True)
async def ping(ctx):
    if ctx.message.server.id in banned_servers_ids:
        await client.say(":no_entry_sign: This server is banned! For more information join the support server and contact a bot moderator (`ad!support`).")
    else:
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        ping = round((t2-t1)*1000)
        msg = "My ping: `{}`.".format(ping)
        if ping > 350:
            msg += "\nThe bot is lagging! :slight_frown: "
        elif ping > 200:
            msg += "\nThe bot might be lagging! :neutral_face: "
        else:
            msg += "\nThe bot isn't lagging! :slight_smile: "
        await client.say(msg)

# ad!info
@client.command(pass_context=True)
async def info(ctx):
    if ctx.message.server.id in banned_servers_ids:
        await client.say(":no_entry_sign: This server is banned! For more information join the support server and contact a bot moderator (`ad!support`).")
    else:
        author = ctx.message.author
        big = []
        await client.say("Collecting information...")
        msg = "I'm in currently in `{}` servers!".format(len(client.servers))
        for server in client.servers:
            if len(server.members) >= 500:
                big.append("+1")
            else:
                print("")
        msg += "\nI'm in currently in `{}` big servers!".format(len(big))
        msg += "\nI've saved `{}` links in total!".format(len(servers_links) + len(special_servers_links))
        msg += "\nI've saved `{}` special links!".format(len(special_servers_links))
        msg += "\nI'm currently advertising `{}` servers in total!".format(len(servers_ids) + len(special_servers_ids))
        msg += "\nI'm currently advertising `{}` special servers!".format(len(special_servers_ids))
        msg += "\nI'm currently ignoring `{}` servers!".format(len(ignored_servers_ids))
        msg += "\nCurrently there are `{}` bot moderators and `{}` bot administrators!".format(len(bot_mods), len(bot_admins))
        await client.say(msg)

# ad!support
@client.command(pass_context=True)
async def support(ctx):
    author = ctx.message.author
    server = client.get_server(support_server_id)
    await client.say("Sliding in your DMs...")
    msg = "**__Here are the bot moderators:__**"
    for mod in bot_mods:
        try:
            user = server.get_member(mod)
            msg += "\n<@{}> - {}".format(mod, user.status)
        except:
            print("")
    msg += "\n \n**__Here are the bot administrators:__**"
    for admin in bot_admins:
        try:
            user = server.get_member(admin)
            msg += "\n<@{}> - {}".format(admin, user.status)
        except:
            print("")
    msg += "\n \nYou can DM a bot moderator and ask for help if you need any."
    try:
        await client.send_message(author, msg)
    except:
        await client.say(":octagonal_sign: Make sure the bot has permission to send you DMs!")

# ad!servers
@client.command(pass_context=True)
async def servers(ctx):
    if ctx.message.server.id in banned_servers_ids:
        await client.say(":no_entry_sign: This server is banned! For more information join the support server and contact a bot moderator (`ad!support`).")
    else:
        author = ctx.message.author
        failed = []
        msg = "**__Servers that aren't setup:__**"
        await client.say("Collecting data...")
        print(">>>SERVERS THAT ARE NOT SETUP<<<")
        for server in client.servers:
            if server.id in servers_ids or server.id in special_servers_ids or server.id in ignored_servers_ids:
                print("")
            else:
                try:
                    links = await client.invites_from(server)
                    msg += "\n{} `-` {} `-` {}".format(server.name, server.id, links[1])
                except:
                    failed.append("+1")
                try:
                    print("\n{} - {} - {} - {}\n".format(server.name, server.id, links[1], len(server.members)))
                except:
                    try:
                        print("\n[?] - {} - {} - {}\n".format(server.id, links[1], len(server.members)))
                    except:
                        print("\nError in loading server\n")
        if len(failed) == 0:
            msg += "\n \n`Collected links from all servers!`"
        else:
            msg += "\n \n`Unable to collect links from {} servers!`".format(len(failed))
        await client.say("Sliding in your DMs...")
        try:
            await client.send_message(author, msg)
        except:
            await client.say(":octagonal_sign: Error! Either there are too many servers in the list or the bot has no permission to DM you!")

# ad!rnd
@client.command(pass_context=True)
async def rnd(ctx):
    if ctx.message.server.id in banned_servers_ids:
        await client.say(":no_entry_sign: This server is banned! For more information join the support server and contact a bot moderator (`ad!support`).")
    else:
        author = ctx.message.author
        choices = ["1", "2"]
        choice = random.choice(choices)
        msg = "**__Random server:__**"
        if choice == "1":
            msg += "\n{}".format(random.choice(servers_links))
        else:
            msg += "\n{}".format(random.choice(special_servers_links))
        await client.say(msg)

# ad!serverinfo [server id]
@client.command(pass_context=True)
async def serverinfo(ctx, target = None):
    if ctx.message.server.id in banned_servers_ids:
        await client.say(":no_entry_sign: This server is banned! For more information join the support server and contact a bot moderator (`ad!support`).")
    else:
        if target == None:
            try:
                author = ctx.message.author
                server = ctx.message.server
                msg = "**__INFORMATION ABOUT `{}`__**".format(server.name)
                msg += "\nMembers: `{}`".format(len(server.members))
                msg += "\nChannels: `{}`".format(len(server.channels))
                msg += "\nEmojis: `{}`".format(len(server.emojis))
                msg += "\nID: `{}`".format(server.id)
                msg += "\nRegion: `{}`".format(server.region)
                msg += "\nRoles: `{}`".format(len(server.roles))
                msg += "\nOwner: `{}`".format(server.owner)
                msg += "\nCreated at: `{}`".format(server.created_at)
                if server.id in servers_ids:
                    msg += "\nSetup: `True`"
                    msg += "\nSpecial ADs: `False`"
                elif server.id in special_servers_ids:
                    msg += "\nSetup: `True`"
                    msg += "\nSpecial ADs: `True`"
                else:
                    msg += "\nSetup: `False`"
                    msg += "\nSpecial ADs: `False`"
                if server.id in toggled_servers:
                    msg += "\nToggled: `True`"
                else:
                    msg += "\nToggled: `False`"
                await client.say(msg)
            except:
                await client.say(":octagonal_sign: Error in collecting information!\nMake sure the bot has the required permissions.")
        else:
            author = ctx.message.author
            try:
                server = client.get_server(target)
                try:
                    msg = "**__INFORMATION ABOUT `{}`__**".format(server.name)
                    msg += "\nMembers: `{}`".format(len(server.members))
                    msg += "\nChannels: `{}`".format(len(server.channels))
                    msg += "\nEmojis: `{}`".format(len(server.emojis))
                    msg += "\nID: `{}`".format(server.id)
                    msg += "\nRegion: `{}`".format(server.region)
                    msg += "\nRoles: `{}`".format(len(server.roles))
                    msg += "\nOwner: `{}`".format(server.owner)
                    msg += "\nCreated at: `{}`".format(server.created_at)
                    if server.id in servers_ids:
                        msg += "\nSetup: `True`"
                        msg += "\nSpecial ADs: `False`"
                    elif server.id in special_servers_ids:
                        msg += "\nSetup: `True`"
                        msg += "\nSpecial ADs: `True`"
                    else:
                        msg += "\nSetup: `False`"
                        msg += "\nSpecial ADs: `False`"
                    if server.id in toggled_servers:
                        msg += "\nToggled: `True`"
                    else:
                        msg += "\nToggled: `False`"
                    await client.say(msg)
                except:
                    await client.say(":octagonal_sign: Error in collecting information!\nMaybe the bot doesn't have the required permissions in that server.")
            except:
                await client.say(":octagonal_sign: Server not found!")

# ad!invite
@client.command(pass_context=True)
async def invite(ctx):
    await client.say("Here is the link to invite the bot:\nhttps://discordapp.com/oauth2/authorize?client_id=439051827384680449&scope=bot&permissions=537259127")

# ad!tos
@client.command(pass_context=True)
async def tos(ctx):
    await client.say(tos_msg)

# ad!suggest <suggestion>
@client.command(pass_context=True)
async def suggest(ctx, *, args = None):
    author = ctx.message.author
    server = ctx.message.server
    server2 = client.get_server(support_server_id)
    chnl = client.get_channel(suggestions_channel)
    if args == None:
        await client.say(":octagonal_sign: No suggestion given!\n`ad!suggest <suggestion>`")
    else:
        if len(str(args)) > 1700:
            await client.say(":octagonal_sign: The suggestion message cannot be longer than 1700 characters!")
        else:
            await client.say("Sending suggestion...")
            try:
                msg = "```diff"
                msg += "\n- SUGGESTION -"
                msg += "\n+ Author: {} - {}".format(author, author.id)
                msg += "\n+ From: {} - {}".format(server.name, server.id)
                msg += "\n+ Suggestion:\n{}".format(args)
                msg += "\n```"
                msg += "\nTag: <@{}>".format(random.choice(bot_mods))
                await client.send_message(chnl, msg)
                await client.say(":white_check_mark: Suggestion sent!")
            except:
                await client.say(":x: Suggestion didn't send!")

# ad!report <user/server> <id> <reason>
@client.command(pass_context=True)
async def report(ctx, option = None, target = None, *, reason = None):
    author = ctx.message.author
    server = ctx.message.server
    server2 = client.get_server(support_server_id)
    chnl = client.get_channel(reports_channel)
    if option == None or target == None or reason == None:
        await client.say(":octagonal_sign: Argument(s) missing!\n`ad!report <user/server> <id> <reason>`")
    else:
        if option == "user" or option == "server":
            if len(str(reason)) > 1700:
                await client.say(":octagonal_sign: The reason cannot be longer than 1700 characters!")
            else:
                await client.say("Sending report...")
                try:
                    msg = "```diff"
                    msg += "\n- REPORT -"
                    msg += "\n+ Author: {} - {}".format(author, author.id)
                    msg += "\n+ From: {} - {}".format(server.name, server.id)
                    msg += "\n+ Reporting ({}): {}".format(option, target)
                    msg += "\n+ Reason:\n{}".format(reason)
                    msg += "\n```"
                    msg += "\nTag: <@{}>".format(random.choice(bot_mods))
                    await client.send_message(chnl, msg)
                    await client.say(":white_check_mark: Report sent!")
                except:
                    await client.say(":x: Report didn't send!")
        else:
            await client.say(":octagonal_sign: Invalid option! Please choose from `user` and `server`.")

# ad!uptime
@client.command(pass_context=True)
async def uptime(ctx):
    if ctx.message.server.id in banned_servers_ids:
        await client.say(":no_entry_sign: This server is banned! For more information join the support server and contact a bot moderator (`ad!support`).")
    elif len(ut_hours) == 0:
        if len(ut_minutes) == 0:
            msg = "`{}` seconds.".format(len(ut_seconds))
        else:
            msg = "`{}` minutes,".format(len(ut_minutes))
            msg += "\n`{}` seconds.".format(len(ut_seconds))
    else:
        msg = "`{}` hours,".format(len(ut_hours))
        msg += "\n`{}` minutes,".format(len(ut_minutes))
        msg += "\n`{}` seconds.".format(len(ut_seconds))
    await client.say("I've been online for:\n{}".format(msg))

''' COMMANDS FOR SERVER ADMINS '''
# ad!setup [channel] [message]
@client.command(pass_context=True)
async def setup(ctx, channel: discord.Channel = None, *, args = None):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.server.id in banned_servers_ids:
        await client.say(":no_entry_sign: This server is banned! For more information join the support server and contact a bot moderator (`ad!support`).")
    elif author.server_permissions.manage_server or author.id in bot_mods or author.id in bot_admins:
        if channel == None:
            msg = "**~~=~~** Make sure the bot has the following permissions: `Manage Server`, `Manage Channels`, `Kick Members`, `Ban Members`, `Create Instant Invite`, `Manage Webhooks`, `Read Messages`, `Send Messages`, `Manage Messages`, `Embed Links`, `Attach Files`, `Read Message History`, `Add Reactions`, `Use External Emojis`. The bot should already have these permissions if you use the official invite link (`ad!invite`)."
            msg += "\n**~~=~~** If you are using a bot to log stuff, make an exception for this bot so it doesn't spam your logs."
            msg += "\n**~~=~~** Use `ad!setup [channel] [message]`. Replace [channel] with the channel you want the bot to send advertisements to and [message] with the message you want the bot to use. The message cannot be longer than 1000 characters. Do not add any links to the message!"
            msg += "\n**~~=~~** Once the bot is done setting up, use `ad!test` to check if everything is working correctly."
            msg += "\n**~~=~~** Remember the read the bot's rules and TOS (`ad!tos`)."
            msg += "\n**~~=~~** If you have any issues with the bot just join the support server and ask for help (`ad!support`)."
            await client.say(msg)
        else:
            if args == None:
                await client.say(":octagonal_sign: No message given! Please add the message you want the bot to use to the command.\n`ad!setup [channel] [message]`")
            else:
                if server.id in servers_ids or server.id in special_servers_ids:
                    await client.say(":octagonal_sign: Looks like this server is already being advertised! If you think that this is an error or if you want to re-setup your server, you can use the `ad!unsetup` command.")
                else:
                    text = "{}".format(args)
                    if len(str(text)) > 1000:
                        await client.say(":octagonal_sign: The message cannot be longer than 1000 characters!")
                    else:
                        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
                        if len(urls) != 0:
                            await client.say(":octagonal_sign: Please do not put any links in your message!")
                        else:
                            await client.say("Setting up...")
                            log = "`THIS IS THE BOT'S LOG:`"
                            log += "\n**Starting logger...**\n```diff"
                            try:
                                log += "\n= Trying to get the channel's ID..."
                                chnl_id = channel.id
                                log += "\n+ Channel ID found!"
                                log += "\n= Trying to find the channel using its ID..."
                                chnl = client.get_channel(chnl_id)
                                log += "\n+ Channel found!"
                                log += "\n= Trying to create an invite for the channel..."
                                invite = await client.create_invite(destination = chnl, xkcd = True, max_uses = 0)
                                log += "\n+ Invite created!"
                                log += "\n= Creating message..."
                                msg = "{}".format(args)
                                msg += "\n \n**~~= = = = = = = = = = = = = == = = = =~~**"
                                msg += "\n:label: Name: {}".format(server.name)
                                msg += "\n:busts_in_silhouette: {} members!".format(len(server.members))
                                msg += "\n:credit_card: ID: {}".format(server.id)
                                msg += "\n:link: Link: {}".format(invite)
                                msg += "\n**~~= = = = = = = = = = = = = == = = = =~~**"
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
                                log += "\n+ Message sent!"
                                log += "\n= Saving the message to the list..."
                                servers_msgs.append(msg)
                                log += "\n+ Message saved!"
                                log += "\n= Saving the server ID to the list..."
                                servers_ids.append(server.id)
                                log += "\n+ Server ID saved!"
                                log += "\n= Saving the invite to the list..."
                                servers_links.append(invite.url)
                                log += "\n+ Invite link saved!"
                                log += "\n= Saving the channel's ID..."
                                channels_ids.append(chnl_id)
                                log += "\n+ Channel ID saved!"
                                log += "\n= Creating a new message..."
                                embed1 = discord.Embed(colour=0x0017FF, description= "")
                                embed1.title = ""
                                embed1.set_image(url="{}".format(new_server_img))
                                embed1.set_footer(text=footer_text)
                                embed1.add_field(name="new server", value="{}".format(msg))
                                log += "\n+ New message created!"
                                log += "\n= Trying to send a message about the server to all other servers..."
                                s = []
                                for c in channels_ids:
                                    try:
                                        c1 = client.get_channel(c)
                                        await client.send_message(c1, embed=embed1)
                                        s.append("+1")
                                    except:
                                        print("")
                                log += "\n+ Sent message to {}/{} channels!".format(len(s), len(channels_ids))
                                log += "\n= Sending results..."
                                log += "\n+ Finished!"
                                log += "\n```\n**Closing logger...**"
                                await client.say(log)
                                await client.say(":white_check_mark: This server is good to go! You can do `ad!test` anytime to test if your server is setup correctly.")
                            except:
                                log += "\n- ^ Error!"
                                log += "\n= Sending results..."
                                log += "\n+ Results sent!\n```\n**Closing logger...**"
                                await client.say(log)
                                await client.say(":octagonal_sign: Looks like there has been an error! Make sure the bot has the required permissions. For more help use `ad!setup`.\nUse `ad!unsetup` and try again.")
    else:
        await client.say(":octagonal_sign: This command can only be used by users who have the `Manage Server` permission and can be bypassed by the bot's staff!")

# ad!unsetup
@client.command(pass_context=True)
async def unsetup(ctx):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.server.id in banned_servers_ids:
        await client.say(":no_entry_sign: This server is banned! For more information join the support server and contact a bot moderator (`ad!support`).")
    elif author.server_permissions.manage_server or author.id in bot_mods or author.id in bot_admins:
        await client.say("Reseting server...")
        log = "`THIS IS THE BOT'S LOG:`"
        log += "\n**Starting logger...**\n```diff"
        log += "\n= Trying to remove the server's ID from the normal servers list..."
        try:
            servers_ids.remove(server.id)
            log += "\n+ Removed!"
        except:
            log += "\n- Server ID not removed!"
        log += "\n= Searching for used channel..."
        for channel in channels_ids:
            try:
                chnl = client.get_channel(channel)
                if chnl in server.channels:
                    log += "\n+ Channel found!"
                    log += "\n= Trying to remove the channel from the list..."
                    channels_ids.remove(channel)
                    log += "\n+ Removed!"
                else:
                    print("")
            except:
                log += "\n- Channel not found!"
        log += "\n= Searching for used message..."
        find = []
        for msg in servers_msgs:
            a = str(msg)
            if server.id in a:
                log += "\n+ Message found!"
                log += "\n= Trying to remove the message from the list..."
                servers_msgs.remove(msg)
                log += "\n+ Removed!"
                find.append("+1")
            else:
                print("")
        if len(find) == 0:
            log += "\n- Message not found!"
        else:
            print("")
        log += "\n= Removing all server links..."
        try:
            invites = await client.invites_from(server)
            log += "\n+ Links found!"
            done = []
            done2 = []
            for invite in invites:
                try:
                    servers_links.remove(invite)
                    done.append("+1")
                except:
                    print("")
                try:
                    special_servers_links.remove(invite)
                    done2.append("+1")
                except:
                    print("")
        except:
            log += "\n- Links not found!"
        log += "\n+ Removed {} normal links!".format(len(done))
        log += "\n+ Removed {} special links!".format(len(done2))
        log += "\n= Sending results..."
        log += "\n+ Finished!"
        log += "\n```\n**Closing logger...**"
        await client.say(log)
        await client.say("You can now try to setup your server again, or leave it like this if you do not want it to be advertised.\nDo not worry if you got any erros, try to set it up again, if it doesn't work you should contact a bot moderator (`ad!support`) and ask for help.")
    else:
        await client.say(":octagonal_sign: This command can only be used by users who have the `Manage Server` permission and can be bypassed by the bot's staff!")

# ad!test
@client.command(pass_context=True)
async def test(ctx):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.server.id in banned_servers_ids:
        await client.say(":no_entry_sign: This server is banned! For more information join the support server and contact a bot moderator (`ad!support`).")
    elif author.server_permissions.manage_server or author.id in bot_mods or author.id in bot_admins:
        if server.id in servers_ids or server.id in special_servers_ids:
            await client.say("Testing...")
            log = "`THIS IS THE BOT'S LOG:`"
            log += "\n**Starting logger...**\n```diff"
            log += "\n= Searching for used channel..."
            find = []
            for channel in channels_ids:
                try:
                    chnl = client.get_channel(channel)
                    if chnl in server.channels:
                        log += "\n+ Channel found!"
                        find.append("+1")
                        log += "\n= Saving channel..."
                        chnl2 = channel
                        log += "\n+ Channel saved!"
                    else:
                        print("")
                except:
                    print("")
            if len(find) == 0:
                log += "\n- Channel not found!"
                log += "\n= Sending results..."
                log += "\n+ Finished!"
                log += "\n```\n**Closing logger...**"
                await client.say(log)
                await client.say(":octagonal_sign: This server is not setup correctly! Please use `ad!unsetup` and then `ad!setup` to get help on how to set it up. If you have any issues or need help, just contact a bot moderator (`ad!support`).")
            else:
                log += "\n= Searching for message..."
                find2 = []
                for msg in servers_msgs:
                    a = str(msg)
                    if server.id in a:
                        log += "\n+ Message found!"
                        find2.append("+1")
                        log += "\n= Saving message..."
                        msg2 = msg
                        log += "\n+ Message saved!"
                    else:
                        print("")
                if len(find2) == 0:
                    log += "\n- Message not found!"
                    log += "\n= Sending results..."
                    log += "\n+ Finished!"
                    log += "\n```\n**Closing logger...**"
                    await client.say(log)
                    await client.say(":octagonal_sign: This server is not setup correctly! Please use `ad!unsetup` and then `ad!setup` to get help on how to set it up. If you have any issues or need help, just contact a bot moderator (`ad!support`).")
                else:
                    try:
                        log += "\n= Creating test message..."
                        embed = discord.Embed(colour=0x00FF00, description= "")
                        embed.title = ""
                        embed.set_image(url="{}".format(test_msg_img))
                        embed.set_footer(text=footer_text)
                        embed.add_field(name="test message", value="{}".format(msg2))
                        log += "\n+ Test message created!"
                        log += "\n= Trying to find the channel..."
                        chnl3 = client.get_channel(chnl2)
                        log += "\n+ Channel found!"
                        log += "\n= Sending test message..."
                        await client.send_message(chnl3, embed=embed)
                        log += "\n+ Message sent!"
                        log += "\n= Sending results..."
                        log += "\n+ Finished!"
                        log += "\n```\n**Closing logger...**"
                        await client.say(log)
                        await client.say(":white_check_mark: Looks like everything is working like it should! If you have issues or need any help, please contact a bot moderator (`ad!support`).")
                        if server.id in toggled_servers:
                            await client.say("WARNING: Your server is toggled! Use `ad!toggle` for it to be advertised again!")
                        else:
                            print("")
                    except:
                        log += "\n- ^ Error!"
                        log += "\n= Sending results..."
                        log += "\n+ Finished!"
                        log += "\n```**Closing logger...**"
                        await client.say(log)
                        await client.say(":octagonal_sign: Looks like there is an error! Make sure the bot has the required permissions and try again. If you need any help, please contact a bot moderator (`ad!support`).")
        else:
            await client.say(":octagonal_sign: Looks like this server isn't setup. Use `ad!setup` to get help on how to set it up. If you believe that this is an error, please contact a bot moderator (`ad!support`).")
    else:
        await client.say(":octagonal_sign: This command can only be used by users who have the `Manage Server` permission and can be bypassed by the bot's staff!")

# ad!toggle
@client.command(pass_context=True)
async def toggle(ctx):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.server.id in banned_servers_ids:
        await client.say(":no_entry_sign: This server is banned! For more information join the support server and contact a bot moderator (`ad!support`).")
    elif author.server_permissions.manage_server or author.id in bot_mods or author.id in bot_admins:
        if server.id in toggled_servers:
            try:
                toggled_servers.remove(server.id)
                await client.say("This server will be advertised again!")
            except:
                await client.say(":octagonal_sign: Unable to toggle this server!")
        else:
            try:
                toggled_servers.append(server.id)
                await client.say("This server won't be advertised untill you run this command again!")
            except:
                await client.say(":octagonal_sign: Unable to toggle this server!")
    else:
        await client.say(":octagonal_sign: This command can only be used by users who have the `Manage Server` permission and can be bypassed by the bot's staff!")

''' COMMANDS FOR BOT MODS '''
# ad!msg <user/server> <id> <message>
@client.command(pass_context=True)
async def msg(ctx, option = None, target = None, *, args = None):
    author = ctx.message.author
    if author.id in bot_mods or author.id in bot_admins:
        if option == None:
            await client.say(":octagonal_sign: No option given!\nOptions: `user`, `server`.")
        elif option == "user" or option == "server":
            if target == None:
                await client.say(":octagonal_sign: No target given!\nTarget has to be a user/server's ID depending on the option!")
            else:
                if args == None:
                    await client.say(":octagonal_sign: No message given!")
                else:
                    chnl = client.get_channel(console_channel)
                    if option == "user":
                        await client.say("Searching for user...")
                        find = []
                        for server in client.servers:
                            try:
                                user = server.get_member(target)
                                find.append("+1")
                                if len(find) == 0:
                                    await client.say("User not found!")
                                else:
                                    await client.say("User found!\n{} `-` {}\nSending message...".format(user, user.id))
                                    try:
                                        await client.send_message(user, "{}\n \n:label: Message from: {} ### {}".format(args, author, author.id))
                                        await client.say("Message sent!")
                                        msg = "```diff"
                                        msg += "\n- MESSAGE -"
                                        msg += "\n+ Author: {} - {}".format(author, author.id)
                                        msg += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
                                        msg += "\n+ Target (user): {} - {}".format(user, user.id)
                                        if len(str(args)) > 1900:
                                            msg += "\n+ Message: Too big to show."
                                        else:
                                            msg += "\n+ Message:\n{}".format(args)
                                        msg += "\n```"
                                        await client.send_message(chnl, msg)
                                    except:
                                        await client.say("Unable to message that user!")
                                    break
                            except:
                                print("")
                    elif option == "server":
                        await client.say("Searching for server...")
                        try:
                            server = client.get_server(target)
                            await client.say("Server found!\n{} `-` {}\nOwner: {} `-` {}\nSending message...".format(server.name, server.id, server.owner, server.owner.id))
                            try:
                                await client.send_message(server.owner, "{}\n \n:label: Message from: {} ### {}".format(args, author, author.id))
                                await client.say("Message sent!")
                                msg = "```diff"
                                msg += "\n- MESSAGE -"
                                msg += "\n+ Author: {} - {}".format(author, author.id)
                                msg += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
                                msg += "\n+ Target (server): {} - {} ### {} - {}".format(server.name, server.id, server.owner, server.owner.id)
                                if len(str(args)) > 1850:
                                    msg += "\n+ Message: Too big to show!"
                                else:
                                    msg += "\n+ Message:\n{}".format(args)
                                msg += "\n```"
                                await client.send_message(chnl, msg)
                            except:
                                await client.say("Unable to message that server's owner!")
                        except:
                            await client.say("Server not found!")
                    else:
                        await client.say(":octagonal_sign: Invalid option!\nOptions: `user`, `server`.")
        else:
            await client.say(":octagonal_sign: Invalid option!\nOptions: `user`, `server`.")
    else:
        await client.say(":octagonal_sign: This command can only be used by the bot's staff!")

# ad!ban <user/server> <id> <reason>
@client.command(pass_context=True)
async def ban(ctx, option = None, target = None, *, reason = None):
    author = ctx.message.author
    if author.id in bot_mods or author.id in bot_admins:
        if option == None:
            await client.say(":octagonal_sign: No option given!\nOptions: `user`, `server`.")
        elif option == "user" or option == "server":
            if target == None:
                await client.say(":octagonal_sign: No target given!\nTarget has to be a user/server's ID depending on the option!")
            elif reason == None:
                await client.say(":octagonal_sign: No reason given!")
            else:
                chnl = client.get_channel(console_channel)
                if option == "user":
                    await client.say("Banning the user from all servers...")
                    find = []
                    for server in client.servers:
                        try:
                            await client.http.ban(target, server.id, 0)
                            find.append("+1")
                        except:
                            print("")
                    await client.say("User has been banned from {} servers out of {}!".format(len(find), len(client.servers)))
                    msg = "```diff"
                    msg += "\n- BAN -"
                    msg += "\n+ Author: {} - {}".format(author, author.id)
                    msg += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
                    msg += "\n+ Target (user): <@{}> - {}".format(target, target)
                    msg += "\n+ Reason: {}".format(reason)
                    msg += "\n+ Banned: {}".format(len(find))
                    msg += "\n```"
                    await client.send_message(chnl, msg)
                elif option == "server":
                    await client.say("Banning server...")
                    try:
                        await client.say("Server found!")
                        if target in banned_servers_ids:
                            await client.say("This server is already banned!")
                        else:
                            await client.say("Banning server...")
                            banned_servers_ids.append(target)
                            for message in servers_msgs:
                                if target in str(message):
                                    servers_msgs.remove(message)
                                else:
                                    print("")
                            for message2 in special_servers_msgs:
                                if target in str(message2):
                                    special_servers_msgs.remove(message2)
                                else:
                                    print("")
                            try:
                                server = client.get_server(target)
                                for channels in server.channels:
                                    if channels.id in channels_ids:
                                        channels_ids.remove(channels)
                                    else:
                                        print("")
                            except:
                                print("")
                            await client.say("Server banned!")
                    except:
                        await client.say("Error in tryingt to ban the server!")
                    msg = "```diff"
                    msg += "\n- BAN -"
                    msg += "\n+ Author: {} - {}".format(author, author.id)
                    msg += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
                    msg += "\n+ Target (server): {}".format(target)
                    msg += "\n+ Reason:\n{}".format(reason)
                    msg += "\n```"
                    await client.send_message(chnl, msg)
                else:
                    await client.say(":octagonal_sign: Invalid option!\nOptions: `user`, `server`.")
        else:
            await client.say(":octagonal_sign: Invalid option!\nOptions: `user`, `server`.")
    else:
        await client.say(":octagonal_sign: This command can only be used by the bot's staff!")

# ad!unban <user/server> id
@client.command(pass_context=True)
async def unban(ctx, option = None, target = None):
    author = ctx.message.author
    if author.id in bot_mods or author.id in bot_admins:
        if option == None:
            await client.say(":octagonal_sign: No option given!\nOptions: `user`, `server`.")
        elif option == "user" or option == "server":
            if target == None:
                await client.say(":octagonal_sign: No target given!\nTarget has to be a user/server's ID depending on the option!")
            else:
                chnl = client.get_channel(console_channel)
                if option == "user":
                    await client.say("Unbanning user...")
                    find = []
                    for server in client.servers:
                        try:
                            banned_users = await client.get_bans(server)
                            user = discord.utils.get(banned_users,id=target)
                            try:
                                await client.unban(server, user)
                                find.append("+1")
                            except:
                                print("")
                        except:
                            print("")
                    await client.say("User has been unbanned from {} servers out of {}!".format(len(find), len(client.servers)))
                    msg = "```diff"
                    msg += "\n- UNBAN -"
                    msg += "\n+ Author: {} - {}".format(author, author.id)
                    msg += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
                    msg += "\n+ Target (user): <@{}> - {}".format(target, target)
                    msg += "\n+ Unbanned: {}".format(len(find))
                    msg += "\n```"
                    await client.send_message(chnl, msg)
                elif option == "server":
                    if target not in banned_servers_ids:
                        await client.say("That server is not banned!")
                    else:
                        try:
                            banned_servers_ids.remove(target)
                            await client.say("Server has been unbanned!")
                        except:
                            await client.say("Unable to unban server!")
                else:
                    await client.say(":octagonal_sign: Invalid option!\nOptions: `user`, `server`.")
        else:
            await client.say(":octagonal_sign: Invalid option!\nOptions: `user`, `server`.")
    else:
        await client.say(":octagonal_sign: This command can only be used by the bot's staff!")

# ad!reset <server id>
@client.command(pass_context=True)
async def reset(ctx, target = None):
    author = ctx.message.author
    if author.id in bot_mods or author.id in bot_admins:
        if target == None:
            await client.say(":octagonal_sign: No server given!\n`ad!reset <server id>`.")
        else:
            cnsl = client.get_channel(console_channel)
            await client.say("Restarting server...")
            log = "`THIS IS THE BOT'S LOG`"
            log += "\n**Starting logger...**\n```diff"
            log += "\n= Searching for server..."
            try:
                server = client.get_server(target)
                log += "\n+ Server found!"
                log += "\n= Searching for server ID in lists..."
                try:
                    servers_ids.remove(target)
                    log += "\n+ Server found and removed from the lists 1/2!"
                except:
                    log += "\n- Server not found 1/2!"
                try:
                    special_servers_ids.remove(target)
                    log += "\n+ Server found and removed from the lists 2/2!"
                except:
                    log += "\n- Server not found 2/2!"
                log += "\n= Searching for the server's message..."
                for msg in servers_msgs:
                    a = str(msg)
                    if target in a:
                        try:
                            servers_msgs.remove(msg)
                            log += "\n+ Server's message found and removed from the lists 1/2!"
                        except:
                            log += "\n- Server's message not found 1/2!"
                    else:
                        print("")
                for msg2 in special_servers_msgs:
                    b = str(msg2)
                    if target in b:
                        try:
                            special_servers_msgs.remove(msg2)
                            log += "\n+ Server's message found and removed from the lists 2/2!"
                        except:
                            log += "\n- Server's message not found 2/2!"
                    else:
                        print("")
                log += "\n= Searching for the channel used by the bot in the server..."
                for channel in channels_ids:
                    try:
                        chanel = client.get_channel(channel)
                        if chanel in server.channels:
                            try:
                                channels_ids.remove(channel)
                                log += "\n+ Channel found and removed from the list!"
                            except:
                                log += "\n- Channel not found!"
                        else:
                            print("")
                    except:
                        print("")
                log += "\n= Removing all server links..."
                try:
                    invites = await client.invites_from(server)
                    log += "\n+ Links found!"
                    done = []
                    done2 = []
                    for invite in invites:
                        try:
                            servers_links.remove(invite)
                            done.append("+1")
                        except:
                            print("")
                        try:
                            special_servers_links.remove(invite)
                            done2.append("+1")
                        except:
                            print("")
                except:
                    log += "\n- Links not found!"
                log += "\n+ Removed {} normal links!".format(len(done))
                log += "\n+ Removed {} special links!".format(len(done2))
                log += "\n= Checking if the server is toggled..."
                if target in toggled_servers:
                    try:
                        toggled_servers.remove(target)
                        log += "\n+ Server removed from the toggled list!"
                    except:
                        log += "\n- Unable to remove server from the toggled list!"
                else:
                    log += "\n+ Server is not toggled!"
                log += "\n= Sending results..."
                log += "\n+ Finished!"
                log += "\n```\n**Closing logger...**"
                await client.say(log)
                await client.say(":white_check_mark: Server has been restarted! For any errors or help, contact a bot administrator!")
                m = "```diff"
                m += "\n- RESET -"
                m += "\n+ Author: {} - {}".format(author, author.id)
                m += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
                m += "\n+ Target: {} - {}".format(server.name, server.id)
                m += "\n```"
                await client.send_message(cnsl, m)
            except:
                log += "\n- Server not found!"
    else:
        await client.say(":octagonal_sign: This command can only be used by the bot's staff!")

# ad!ignore <server id>
@client.command(pass_context=True)
async def ignore(ctx, target = None):
    author = ctx.message.author
    if author.id in bot_mods or author.id in bot_admins:
        if target == None:
            await client.say(":octagonal_sign: No server given!\n`ad!ignore <server id>`.")
        else:
            cnsl = client.get_channel(console_channel)
            if target in ignored_servers_ids:
                await client.say("Removing the given ID from the ignored list...")
                try:
                    ignored_servers_ids.remove(target)
                    await client.say("Removed! Now I am no longer ignoring the server with the following ID: {}".format(target))
                    msg = "```diff"
                    msg += "\n- IGNORE (del) -"
                    msg += "\n+ Author: {} - {}".format(author, author.id)
                    msg += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
                    msg += "\n+ Target: {}".format(target)
                    msg += "\n```"
                    await client.send_message(cnsl, msg)
                except:
                    await client.say("Unable to un-ignore server!")
            else:
                await client.say("Adding the given ID to the ignored list...")
                try:
                    ignored_servers_ids.append(target)
                    await client.say("Added! Now I am ignoring the server with the following ID: {}".format(target))
                    msg = "```diff"
                    msg += "\n- IGNORE (add) -"
                    msg += "\n+ Author: {} - {}".format(author, author.id)
                    msg += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
                    msg += "\n+ Target: {}".format(target)
                    msg += "\n```"
                    await client.send_message(cnsl, msg)
                except:
                    await client.say("Unable to ignore server!")
    else:
        await client.say(":octagonal_sign: This command can only be used by the bot's staff!")

''' COMMANDS FOR BOT ADMINS '''
# ad!mod <add/del> <user>
@client.command(pass_context=True)
async def mod(ctx, option = None, user: discord.User = None):
    author = ctx.message.author
    if author.id in bot_admins:
        if option == None:
            await client.say(":octagonal_sign: No option given!\nOptions: `add`, `del`.")
        elif option == "add" or option == "del":
            cnsl = client.get_channel(console_channel)
            if user == None:
                await client.say(":octagonal_sign: No user given!\nPlease mention an user you want to add/remove to/from the bot list!")
            elif option == "add":
                if user.id in bot_mods:
                    await client.say("This user is already a bot moderator!")
                else:
                    await client.say("Adding the mentioned user to the moderator list...")
                    try:
                        bot_mods.append(user.id)
                        await client.say("Added! They should now be able to use all bot moderator commands.\nMake sure to also give them the bot moderator role on the support server!")
                        msg = "```diff"
                        msg += "\n- MOD (add) -"
                        msg += "\n+ Author: {} - {}".format(author, author.id)
                        msg += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
                        msg += "\n+ Target: {} - {}".format(user, user.id)
                        msg += "\n```"
                        await client.send_message(cnsl, msg)
                    except:
                        await client.say("Unable to add the user to the moderator list!")
            elif option == "del":
                if user.id not in bot_mods:
                    await client.say("This user is not a bot moderator!")
                else:
                    await client.say("Removing the mentioned user from the moderator list...")
                    try:
                        bot_mods.remove(user.id)
                        await client.say("Removed! They shouldn't be able to use any bot moderator commands.\nMake sure to remove their role from the support server!")
                        msg = "```diff"
                        msg += "\n- MOD (del) -"
                        msg += "\n+ Author: {} - {}".format(author, author.id)
                        msg += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
                        msg += "\n+ Target: {} - {}".format(user, user.id)
                        msg += "\n```"
                        await client.send_message(cnsl, msg)
                    except:
                        await client.say("Unable to remove the user from the moderator list!")
            else:
                await client.say(":octagonal_sign: Invalid option!\nOptions: `add`, `del`.")
        else:
            await client.say(":octagonal_sign: Invalid option!\nOptions: `add`, `del`.")
    else:
        await client.say(":octagonal_sign: This command can only be used by the bot's administrators!")

# ad!special <add/del> <server id>
@client.command(pass_context=True)
async def special(ctx, option = None, target = None):
    author = ctx.message.author
    if author.id in bot_admins:
        if option == None:
            await client.say(":octagonal_sign: No option given!\nOptions: `add`, `del`.")
        elif option == "add" or option == "del":
            cnsl = client.get_channel(console_channel)
            if option == "add":
                try:
                    server = client.get_server(target)
                    if server.id in servers_ids:
                        if server.id in special_servers_ids:
                            await client.say("This server is already in the special list!")
                        else:
                            log = "`THIS IS THE BOT'S LOG:`"
                            log += "\n**Starting logger...**\n```diff"
                            try:
                                log += "\n= Searching for used message..."
                                for m in servers_msgs:
                                    ab = "{}".format(server.id)
                                    a = str(m)
                                    if ab in a:
                                        log += "\n+ Message found!"
                                        log += "\n= Saving message..."
                                        special_servers_msgs.append(m)
                                        log += "\n+ Message saved!"
                                    else:
                                        print("")
                                log += "\n= Saving server's ID to the list..."
                                special_servers_ids.append(server.id)
                                log += "\n+ Saved!"
                                log += "\n= Trying to get a list of links for the server..."
                                invites = await client.invites_from(server)
                                invite = invites[1]
                                log += "\n= Saving most used link..."
                                special_servers_links.append(invite.url)
                                log += "\n+ Saved!"
                                log += "\n= Sending results..."
                                log += "\n+ Finished!"
                                log += "\n```\n**Closing logger...**"
                                await client.say(log)
                                await client.say(":white_check_mark: The server should now have special perks! Make sure to give the special role to the server owner!")
                                msg = "```diff"
                                msg += "\n- SPECIAL (add) -"
                                msg += "\n+ Author: {} - {}".format(author, author.id)
                                msg += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
                                msg += "\n+ Target: {} - {}".format(server.name, server.id)
                                msg += "\n```"
                                await client.send_message(cnsl, msg)
                            except:
                                log += "\n- ^ Error!"
                                log += "\n= Sending results..."
                                log += "\n+ Finished!"
                                log += "\n```\n**Closing logger...**"
                                await client.say(log)
                                await client.say(":octagonal_sign: Looks like there is an error!\nMake sure the bot has all permissions in the server and try again.")
                    else:
                        await client.say("This server isn't setup! Try adding it after their staff has set it up.")
                except:
                    await client.say(":octagonal_sign: Server not found! Make sure the bot is in that server.")
            elif option == "del":
                try:
                    server = client.get_server(target)
                    if server.id in special_servers_ids:
                        log = "`THIS IS THE BOT'S LOG:`"
                        log += "\n**Starting logger...**\n```diff"
                        try:
                            log += "\n= Searching for used message..."
                            for m in special_servers_msgs:
                                a = str(m)
                                if server.id in a:
                                    log += "\n+ Message found!"
                                    log += "\n= Removing message..."
                                    special_servers_msgs.remove(m)
                                    log += "\n+ Removed!"
                                else:
                                    print("")
                            log += "\n= Removing the server's ID from the list..."
                            special_servers_ids.remove(target)
                            log += "\n+ Removed!"
                            log += "\n= Trying to get all server links..."
                            invites = await client.invites_from(server)
                            log += "\n+ Links found!"
                            log += "\n= Removing links..."
                            done = []
                            for invite in invites:
                                try:
                                    special_servers_links.remove(invite)
                                    done.append("+1")
                                except:
                                    print("")
                            log += "\n+ Removed {} links out of {}!".format(len(done), len(invites))
                            log += "\n= Sending results..."
                            log += "\n+ Finished!"
                            log += "\n```\n**Closing logger...**"
                            await client.say(log)
                            await client.say(":white_check_mark: The server should no longer have special perks!\nMake sure to remove the special role from the server owner!")
                            msg = "```diff"
                            msg += "\n- SPECIAL (del) -"
                            msg += "\n+ Author: {} - {}".format(author, author.id)
                            msg += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
                            msg += "\n+ Target: {} - {}".format(server.name, server.id)
                            msg += "\n```"
                            await client.send_message(cnsl, msg)
                        except:
                            log += "\n- ^ Error!"
                            log += "\n= Sending results..."
                            log += "\n+ Finished!"
                            log += "\n```\n**Closing logger...**"
                            await client.say(log)
                            await client.say(":octagonal_sign: Looks like there is an error!\nMake sure the bot has all permissions in that server and try again.")
                    else:
                        await client.say("This server is not in the special list!")
                except:
                    await client.say(":octagonal_sign: Server not found! Make sure the bot is in that server.")
            else:
                await client.say(":octagonal_sign: Invalid option!\nOptions: `add`, `del`.")
        else:
            await client.say(":octagonal_sign: Invalid option!\nOptions: `add`, `del`.")
    else:
        await client.say(":octagonal_sign: This command can only be used by the bot's administrators!")

# ad!announce <text>
@client.command(pass_context=True)
async def announce(ctx, *, args = None):
    author = ctx.message.author
    if author.id in bot_admins:
        if args == None:
            await client.say(":octagonal_sign: No message given!")
        else:
            if len(str(args)) > 1800:
                await client.say(":octagonal_sign: The message cannot be longer than 1800 characters!")
            else:
                cnsl = client.get_channel(console_channel)
                done = []
                pos = []
                await client.say("Sending announcement...")
                for channel in channels_ids:
                    pos.append("+1")
                    try:
                        dest = client.get_channel(channel)
                        for server in client.servers:
                            if dest in server.channels:
                                try:
                                    embed = discord.Embed(colour=0xFF0000, description= "")
                                    embed.title = ""
                                    embed.set_image(url="{}".format(announcement_img))
                                    embed.set_footer(text=footer_text)
                                    embed.add_field(name="announcement", value="{}\n \n**~~= = = = = = = = = = = = = == = = = =~~**\n:label: Message by: {} - {}\n:arrows_counterclockwise: Position: {}/{}\n**~~= = = = = = = = = = = = = == = = = =~~**".format(args, author, author.id, len(pos), len(channels_ids)))
                                    await client.send_message(dest, "<@{}>".format(server.owner.id), embed=embed)
                                    done.append("+1")
                                except:
                                    print("")
                            else:
                                print("")
                    except:
                        print("")
                await client.say("Finished! Check console for more information.")
                msg = "```diff"
                msg += "\n- ANNOUNCE -"
                msg += "\n+ Author: {} - {}".format(author, author.id)
                msg += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
                msg += "\n+ Message:\n{}".format(args)
                msg += "\n+ Sent: {}/{}".format(len(done), len(channels_ids))
                msg += "\n```"
                await client.send_message(cnsl, msg)
    else:
        await client.say(":octagonal_sign: This command can only be used by the bot's administrators!")

# ad!force
@client.command(pass_context=True)
async def force(ctx):
    author = ctx.message.author
    if author.id in bot_admins:
        await client.say("Forcing advertisements...")
        cnsl = client.get_channel(console_channel)
        nor = []
        spe = []
        total = []
        failed = []
        try:
            for channel in channels_ids:
                c = random.randint(0, 10)
                if c <= 6:
                    m = random.choice(servers_msgs)
                    embed = discord.Embed(colour=0x00FFF7, description= "")
                    embed.title = ""
                    embed.set_footer(text=footer_text)
                    embed.add_field(name="forced advertisement", value="{}".format(m))
                else:
                    m = random.choice(special_servers_msgs)
                    embed = discord.Embed(colour=0xFFAE00, description= "")
                    embed.title = ""
                    embed.set_image(url="{}".format(special_server_img))
                    embed.set_footer(text=footer_text)
                    embed.add_field(name="forced special advertisement", value="{}".format(m))
                try:
                    dest = client.get_channel(channel)
                    await client.send_message(dest, embed=embed)
                    if c <= 6:
                        nor.append("+1")
                    else:
                        spe.append("+1")
                    total.append("+1")
                except:
                    failed.append("+1")
            await client.say("Finished! Check the console for more info!")
            msg = "```diff"
            msg += "\n- FORCE ADVERTISEMENT -"
            msg += "\n+ Author: {} - {}".format(author, author.id)
            msg += "\n+ From: {} - {}".format(ctx.message.server.name, ctx.message.server.id)
            msg += "\n+ Total sent: {}".format(len(total))
            msg += "\n+ Failed: {}".format(len(failed))
            msg += "\n+ Special sent: {}".format(len(spe))
            msg += "\n+ Normal sent: {}".format(len(nor))
            msg += "\n```"
            await client.send_message(cnsl, msg)
        except:
            print("")
    else:
        await client.say(":octagonal_sign: This command can only be used by the bot's administrators!")

# ad!backup
@client.command(pass_context=True)
async def backup(ctx):
    author = ctx.message.author
    if author.id in bot_admins:
        await client.say("Backing up...")
        msg = "`THIS IS THE BOT'S LOG:`"
        msg += "\n**Starting logger...**\n```diff"
        try:
            msg += "\n= Backing up servers ids..."
            print(">>>SERVERS IDS<<<\nservers_ids")
            print(servers_ids)
            print("")
            print("")
            print("")
            msg += "\n+ Backed up!"
        except:
            msg += "\n- Error in backing up!"
        try:
            msg += "\n= Backing up special servers ids..."
            print(">>>SPECIAL SERVERS IDS<<<\nspecial_servers_ids")
            print(special_servers_ids)
            print("")
            print("")
            print("")
            msg += "\n+ Backed up!"
        except:
            msg += "\n- Error in backing up!"
        try:
            msg += "\n= Backing up channels ids..."
            print(">>>CHANNELS IDS<<<\nchannels_ids")
            print(channels_ids)
            print("")
            print("")
            print("")
            msg += "\n+ Backed up!"
        except:
            msg += "\n- Error in backing up!"
        try:
            msg += "\n= Backing up servers messages..."
            print(">>>SERVERS MESSAGES<<<\nservers_msgs")
            print(servers_msgs)
            print("")
            print("")
            print("")
            msg += "\n+ Backed up!"
        except:
            msg += "\n- Error in backing up!"
        try:
            msg += "\n= Backing up special servers messages..."
            print(">>>SPECIAL SERVERS MESSAGES<<<\nspecial_servers_msgs")
            print(special_servers_msgs)
            print("")
            print("")
            print("")
            msg += "\n+ Backed up!"
        except:
            msg += "\n- Error in backing up!"
        try:
            msg += "\n= Backing up servers links..."
            print(">>>SERVERS LINKS<<<\nservers_links")
            print(servers_links)
            print("")
            print("")
            print("")
            msg += "\n+ Backed up!"
        except:
            msg += "\n- Error in backing up!"
        try:
            msg += "\n= Backing up special servers links..."
            print(">>>SPECIAL SERVERS LINKS<<<\nspecial_servers_links")
            print(special_servers_links)
            print("")
            print("")
            print("")
            msg += "\n+ Backed up!"
        except:
            msg += "\n- Error in backing up!"
        try:
            msg += "\n= Backing up ignored servers ids..."
            print(">>>IGNORED SERVERS IDS<<<\nignored_servers_ids")
            print(ignored_servers_ids)
            print("")
            print("")
            print("")
            msg += "\n+ Backed up!"
        except:
            msg += "\n- Error in backing up!"
        try:
            msg += "\n= Backing up banned servers ids..."
            print(">>>BANNED SERVERS IDS<<<\nbanned_servers_ids")
            print(banned_servers_ids)
            print("")
            print("")
            print("")
            msg += "\n+ Backed up!"
        except:
            msg += "\n- Error in backing up!"
        try:
            msg += "\n= Backing up toggled servers..."
            print(">>>TOGGLED SERVERS<<<\ntoggled_servers")
            print(toggled_servers)
            print("")
            print("")
            print("")
            msg += "\n+ Backed up!"
        except:
            msg += "\n- Error in backing up!"
        try:
            msg += "\n= Backing up bot moderators..."
            print(">>>BOT MODERATORS<<<\nbot_mods")
            print(bot_mods)
            print("")
            print("")
            print("")
            msg += "\n+ Backed up!"
        except:
            msg += "\n- Error in backing up!"
        try:
            msg += "\n= Backing up bot administrators..."
            print(">>>BOT ADMINISTRATORS<<<\nbot_admins")
            print(bot_admins)
            print("")
            print("")
            print("")
            msg += "\n+ Backed up!"
        except:
            msg += "\n- Error in backing up!"
        msg += "\n= Sending results..."
        msg += "\n+ Finished!"
        msg += "\n```\n**Closing logger...**"
        await client.say(msg)
    else:
        await client.say(":octagonal_sign: This command can only be used by the bot's administrators!")

# TURNS THE BOT ON
client.run(os.environ['BOT_TOKEN'])
