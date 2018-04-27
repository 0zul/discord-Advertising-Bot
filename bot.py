import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
import time

''''''

Client = discord.Client()
bot_prefix= "ad!"
client = commands.Bot(command_prefix=bot_prefix)
footer_text = "[+]Advertisement Bot[+]"

bot_moderators = ["412201413335056386"]
bot_creator = '412201413335056386'
main_channel = '439050292471005205'
support_server = '414089074870321153'
console_channel = '439049428381466634'
special_server_img = "https://i.imgur.com/G5SWYtL.png"
announcement_img = "https://i.imgur.com/2m9gzUm.png"
test_msg_img = "https://i.imgur.com/3zHcRpt.png"
new_server_img = "https://i.imgur.com/79FgWOd.png"

# SPECIAL LINKS
special_links = []
# ALL SERVERS' IDS
servers_ids = []
# SPECIAL SERVERS' IDS
special_servers_ids = []
# CHANNELS IDS
channels_ids = []
# BANNED SERVERS
banned_servers = []

# TYPES LINKS
gaming_servers = []
anime_servers = []
nsfw_servers = []
programming_servers = []
community_servers = []
memes_servers = []
other_servers = []
none_servers = []

# TYPES IDS
gaming_servers_ids = []
anime_servers_ids = []
nsfw_servers_ids = []
programming_servers_ids = []
community_servers_ids = []
memes_servers_ids = []
other_servers_ids = []
none_servers_ids = []

types = ["gaming", "anime", "nsfw", "programming", "community", "memes", "other"]

help_message1 = "**__COMMANDS FOR EVERYONE__**"
help_message1 += "```cs"
help_message1 += "\nad!help"
help_message1 += "\n   # Gives you this list."
help_message1 += "\nad!ping"
help_message1 += "\n   # Pings the bot. Use this to check if the bot is lagging."
help_message1 += "\nad!support"
help_message1 += "\n   # Gives you the invite link to the support server and the creator's ID."
help_message1 += "\nad!info"
help_message1 += "\n   # Shows information about the bot."
help_message1 += "\nad!servers"
help_message1 += "\n   # Gives you a list of servers that aren't in the advertising list."
help_message1 += "\nad!rnd [type]"
help_message1 += "\n   # Gives you a random server matching the type you specify, if no type is given it will give you a completely random server."
help_message1 += "\nad!serverinfo"
help_message1 += "\n   # Shows information about the server."
help_message1 += "\nad!invite"
help_message1 += "\n   # Gives you the invite link for the bot."
help_message1 += "\nad!botinfo"
help_message1 += "\n   # Gives you information about the bot as well as the bot rules."
help_message1 += "\nad!suggest <text>"
help_message1 += "\n   # Sends a suggestion to the bot moderators."
help_message1 += "\nad!report <user/server> <reason>"
help_message1 += "\n   # Reports a server or user to the bot moderators."
help_message1 += "\n```"

help_message2 = "**__COMMANDS FOR SERVER OWNERS__**"
help_message2 += "\n```cs"
help_message2 += "\nad!shelp"
help_message2 += "\n   # Gives you help on how to setup your server."
help_message2 += "\nad!stypes"
help_message2 += "\n   # Gives you a list of server types you can use to setup your server."
help_message2 += "\nad!setup <channel> <type>"
help_message2 += "\n   # Starts setting up your server with the specified type."
help_message2 += "\nad!test"
help_message2 += "\n   # Tests if your server is setup correctly."
help_message2 += "\n```"

help_message3 = "**__COMMANDS FOR BOT MODERATORS__**"
help_message3 += "\n```cs"
help_message3 += "\nad!announce <text>"
help_message3 += "\n   # Sends an announcement to every server that has the bot setup."
help_message3 += "\nad!say <server id> <text>"
help_message3 += "\n   # Sends a message to the server with the matching ID as the one given."
help_message3 += "\nad!force"
help_message3 += "\n   # Forces the bot to advertise."
help_message3 += "\nad!ban <user/server> <id> <reason>"
help_message3 += "\n   # Either bans an user or a server with the matching ID as the one given. Depends on which option you choose."
help_message3 += "\nad!unban <user/server> <id>"
help_message3 += "\n   # Either unbans an user or a server with the matching ID as the one given. Depends on the which option you choose."
help_message3 += "\nad!delete <server link>"
help_message3 += "\n   # Deletes a server link from both the normal and special list."
help_message3 += "\nad!dm <server id> <message>"
help_message3 += "\n   # DMs the owner of the server with the matching ID as the one given."
help_message3 += "\nad!delete <server id>"
help_message3 += "\n   # Removes a server and all its links from the lists."
help_message3 += "\n```"

help_message4 = "**__COMMANDS FOR THE BOT CREATOR__**"
help_message4 += "\n```cs"
help_message4 += "\nad!mod <del/add> <user>"
help_message4 += "\n   # Adds or removes a bot moderator"
help_message4 += "\nad!special <add/del> <server id> <server link>"
help_message4 += "\n   # Adds or removes the server from the special list."
help_message4 += "\n```"

# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    t1 = time.perf_counter()
    await client.change_presence(game=discord.Game(name='ad!help - For help.'))
    await client.wait_until_ready()
    t2 = time.perf_counter()
    chnl = client.get_channel(console_channel)
    msg = ":white_check_mark: "
    msg += "\n**~~`==========`~~**"
    msg += "\nAdvertiser Bot - Logged in!"
    msg += "\n**~~`==========`~~**"
    msg += "\nName: {}".format(client.user.name)
    msg += "\nID: {}".format(client.user.id)
    msg += "\n**~~`==========`~~**"
    msg += "\nPing: {}ms".format(round((t2-t1)*1000))
    msg += "\n**~~`==========`~~**"
    await client.send_message(chnl, msg)

# AUTO CHANGING PLAYING STATUS
async def gamechanger():
    await client.wait_until_ready()
    while not client.is_closed:
        servers = client.servers
        await client.change_presence(game=discord.Game(name='in {} servers!'.format(len(servers))))
        await asyncio.sleep(1800)

client.loop.create_task(gamechanger())
            
# AUTO ADVERTISING SYSTEM
async def autoad():
    await client.wait_until_ready()
    while not client.is_closed:
        sent = []
        total = []
        log = ":a: :regional_indicator_d: "
        log += "\n**~~`==========`~~**"
        for channel in channels_ids:
            rnd_server_id = random.choice(servers_ids)
            msg = "**~~__====================__~~**"
            if rnd_server_id in special_servers_ids:
                msg += "\n:star:   :a: :regional_indicator_d:   :star: "
            else:
                msg += "\n:a: :regional_indicator_d: "
            msg += "\n**~~__====================__~~**"
            msg += "\n "
            if rnd_server_id in special_servers_ids:
                invite = random.choice(special_links)
                msg += "\n:star2: __**AMAZING SERVER**__ :star2:"
                msg += "\n "
                msg += "\n:link: Link: {}".format(invite)
            else:
                if rnd_server_id in gaming_servers_ids:
                    invite = random.choice(gaming_servers)
                    msg += "\n:video_game: GAMING SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                elif rnd_server_id in anime_servers_ids:
                    invite = random.choice(anime_servers)
                    msg += "\n:milky_way: ANIME SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                elif rnd_server_id in nsfw_servers_ids:
                    invite = random.choice(nsfw_servers)
                    msg += "\n:underage: NSFW SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                elif rnd_server_id in community_servers_ids:
                    invite = random.choice(community_servers)
                    msg += "\n:speech_balloon: COMMUNITY SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                elif rnd_server_id in programming_servers_ids:
                    invite = random.choice(programming_servers)
                    msg += "\n:computer: PROGRAMMING SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                elif rnd_server_id in memes_servers_ids:
                    invite = random.choice(memes_servers)
                    msg += "\n:100: MEMES SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                elif rnd_server_id in other_servers_ids:
                    invite = random.choice(other_servers)
                    msg += "\n:confetti_ball: FUN SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                else:
                    invite = random.choice(none_servers)
                    msg += "\n:grey_question: MYSTERIOUS SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
            msg += "\n "
            msg += "\n**~~__====================__~~**"
            msg += "\n:regional_indicator_j: :regional_indicator_o: :regional_indicator_i: :regional_indicator_n:   :regional_indicator_n: :regional_indicator_o: :regional_indicator_w: "
            msg += "\n**~~__====================__~~**"
            if rnd_server_id in special_servers_ids:
                embd = discord.Embed(colour=0xFF9B00, description= "")
                embd.set_image(url="{}".format(special_server_img))
                embd.add_field(name="special advertisement", value=msg)
            else:
                embd = discord.Embed(colour=0x00ECFF, description= "")
                embd.add_field(name="advertisement", value=msg)
            embd.title = ""
            embd.set_footer(text=footer_text)
            try:
                chnl = client.get_channel(channel)
                await client.send_message(chnl, "{}".format(invite), embed=embd)
                sent.append("+1")
            except:
                total.append("+1")
        log += "\nAds sent: {}\nAds failed: {}".format(len(sent), len(total))
        log += "\n**~~`==========`~~**"
        cnsl_chnl = client.get_channel(console_channel)
        await client.send_message(cnsl_chnl, log)
        await asyncio.sleep(1200)

client.loop.create_task(autoad())

''' COMMANDS FOR EVERYONE '''
# ad!help
client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    await client.say("Sliding in your DMs...")
    try:
        await client.send_message(author, help_message1)
        await client.send_message(author, help_message2)
        await client.send_message(author, help_message3)
        await client.send_message(author, help_message4)
    except:
        await client.say(":octagonal_sign: Make sure the bot has permission to send you DMs!")

# ad!ping
@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    await client.say("My ping: `{}ms`.".format(round((t2-t1)*1000)))

# ad!support
@client.command(pass_context=True)
async def support(ctx):
    author = ctx.message.author
    await client.say("Sliding in your DMs...")
    msg = "Here is the invite link to the support server:\nhttps://discord.gg/7BU8Uty\n \nHere are the bot moderators:"
    for ids in bot_moderators:
        msg += "\n<@{}>".format(ids)
    try:
        await client.send_message(author, msg)
    except:
        await client.say(":octagonal_sign: Make sure the bot has permission to send you DMs!")

# ad!info
@client.command(pass_context=True)
async def info(ctx):
    a = len(gaming_servers)
    b = len(anime_servers)
    c = len(nsfw_servers)
    d = len(community_servers)
    e = len(programming_servers)
    f = len(memes_servers)
    g = len(other_servers)
    h = len(none_servers)
    i = len(special_links)
    total = a + b + d + c + e + f + g + h + i
    normal = total - len(special_links)
    msg = "Current server count:  `{}`".format(len(client.servers))
    msg += "\nCurrent link count:  `{}`".format(total)
    msg += "\nNormal link count:  `{}`".format(normal)
    msg += "\nSpecial link count:  `{}`".format(len(special_links))
    await client.say(msg)

# ad!servers
@client.command(pass_context=True)
async def servers(ctx):
    author = ctx.message.author
    skipped = []
    msg = "**Servers that are not in the advertising list:**"
    for server in client.servers:
        if server.id in servers_ids:
            print(".")
        else:
            try:
                links = await client.invites_from(server)
                msg += "\n{} `-` {} `-` {}".format(server.name, server.id, links[1])
            except:
                skipped.append("+1")
    if len(skipped) == 0:
        msg += "\n`Collected all links!`"
    else:
        msg += "\n`Unable to collect links from {} servers!`".format(len(skipped))
    await client.say("Sliding in your DMs...")
    try:
        await client.send_message(author, msg)
    except:
        await client.say(":octagonal_sign: Make sure the bot has permission to send you DMs!")

# ad!rnd [type]
@client.command(pass_context=True)
async def rnd(ctx, args = None):
    author = ctx.message.author
    if args == None:
        msg = "**Radnom server:**"
        rnd_server_id = random.choice(servers_ids)
        if rnd_server_id in gaming_servers_ids:
            msg += "\nGaming server: {}".format(random.choice(gaming_servers))
        elif rnd_server_id in anime_servers_ids:
            msg += "\nAnime server: {}".format(random.choice(anime_servers))
        elif rnd_server_id in nsfw_servers_ids:
            msg += "\nNSFW server: {}".format(random.choice(nsfw_servers))
        elif rnd_server_id in community_servers_ids:
            msg += "\nCommunity server: {}".format(random.choice(community_servers))
        elif rnd_server_id in programming_servers_ids:
            msg += "\nProgramming server: {}".format(random.choice(programming_servers))
        elif rnd_server_id in other_servers_ids:
            msg += "\nFun server: {}".format(random.choice(other_servers))
        elif rnd_server_id in memes_servers_ids:
            msg += "\nMemes server: {}".format(random.choice(memes_servers))
        else:
            msg += "\nMysterious server: {}".format(random.choice(none_servers))
        await client.say("Sliding in your DMs...")
        try:
            await client.send_message(author, msg)
        except:
            await client.say(":octagonal_sign: Make sure the bot has permission to send you DMs!")
    else:
        if args not in types:
            await client.say(":octagonal_sign: Invalid type! List of types to chose from:\n`gaming`, `anime`, `community`, `nsfw`, `programming`, `memes`, `other`.")
        else:
            if args == "gaming":
                msg = "**Random gaming server:** {}".format(random.choice(gaming_servers))
            elif args == "anime":
                msg = "**Random anime server:** {}".format(random.choice(anime_servers))
            elif args == "nsfw":
                msg = "**Random NSFW server:** {}".format(random.choice(nsfw_servers))
            elif args == "community":
                msg = "**Random community server:** {}".format(random.choice(community_servers))
            elif args == "programming":
                msg = "**Random programming server:** {}".format(random.choice(programming_servers))
            elif args == "memes":
                msg = "**Random memes server:** {}".format(random.choice(memes_servers))
            elif args == "other":
                msg = "**Random fun server:** {}".format(random.choice(other_servers))
            else:
                msg = "**Random mysterious server:** {}".format(random.choice(none_servers))
            await client.say("Sliding in your DMs...")
            try:
                await client.send_message(author, msg)
            except:
                await client.say(":octagonal_sign: Make sure the bot has permission to send you DMs!")

# ad!serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    author = ctx.message.author
    server = ctx.message.server
    msg = "**INFORMATION ABOUT {}**".format(server.name)
    msg += "\nMembers: `{}`".format(len(server.members))
    msg += "\nChannels: `{}`".format(len(server.channels))
    msg += "\nEmojis: `{}`".format(len(server.emojis))
    msg += "\nID: `{}`".format(server.id)
    msg += "\nRegion: `{}`".format(server.region)
    msg += "\nRoles: `{}`".format(len(server.roles))
    msg += "\nOwner: `{}`".format(server.owner)
    msg += "\nCreated at: `{}`".format(server.created_at)
    if server.id in gaming_servers_ids:
        msg += "\nType: `Gaming`"
    elif server.id in anime_servers_ids:
        msg += "\nType: `Anime`"
    elif server.id in nsfw_servers_ids:
        msg += "\nType: `NSFW`"
    elif server.id in programming_servers_ids:
        msg += "\nType: `Programming`"
    elif server.id in community_servers_ids:
        msg += "\nType: `Community`"
    elif server.id in memes_servers_ids:
        msg += "\nType: `Memes`"
    elif server.id in other_servers_ids:
        msg += "\nType: `Other`"
    elif server.id in none_servers_ids:
        msg += "\nType: `Mysterious`"
    else:
        msg += "\nType: `?`"

    if server.id in special_servers_ids:
        msg += "\nSpecial ADs: `True`"
    else:
        msg += "\nSpecial ADs: `False`"

    await client.say(msg)

# ad!invite
@client.command(pass_context=True)
async def invite(ctx):
    author = ctx.message.author
    await client.say("Sliding in your DMs...")
    try:
        await client.send_message(author, "Here is the link to invite the bot:\nhttps://discordapp.com/oauth2/authorize?client_id=439051827384680449&scope=bot&permissions=8")
    except:
        await client.say(":octagonal_sign: Make sure the bot has permission to send you DMs!")

# ad!botinfo
@client.command(pass_context=True)
async def botinfo(ctx):
    author = ctx.message.author
    msg = "**__By using this bot you agree to the following:__**"
    msg += "\n~~**=**~~ Giving Administrator permissions to the bot so it runs correctly!"
    msg += "\n~~**=**~~ Letting the bot ban and unban users that are known for harming other servers or breaking the discord TOS!"
    msg += "\n~~**=**~~ Letting the bot create invite links for your server without notice!"
    msg += "\n~~**=**~~ Letting the bot send advertisements for other discord servers on your server and sending your server links to other servers!"
    msg += "\n~~**=**~~ Receiving announcements from the bot!"
    msg += "\n "
    msg += "\n**__Bot rules:__**"
    msg += "\n~~**=**~~ Everyone must be able to see the channel that the bot uses!"
    msg += "\n~~**=**~~ Spamming bot commands or trying to make the bot lag is not allowed!"
    msg += "\n~~**=**~~ Asking to become a bot moderator is not allowed!"
    msg += "\n~~**=**~~ Only DM the bot creator or bot moderators if you have any questions or if you need help!"
    msg += "\n~~**=**~~ Do not send suggestions just to troll the bot moderators/creator!"
    msg += "\n~~**=**~~ Do not false report users or servers!"
    msg += "\n~~**=**~~ Breaking any of these rules will get you and/or your server banned!"
    msg += "\n "
    msg += "\n**__You can use `ad!help` to see a list of commands!__**"
    await client.say(msg)

# ad!suggest <text>
@client.command(pass_context=True)
async def suggest(ctx, *, args = None):
    author = ctx.message.author
    chnl = client.get_channel(main_channel)
    if args == None:
        await client.say(":octagonal_sign: Please add your suggestion.\n`ad!suggest <text>`")
    else:
        await client.say("Sending suggestion...")
        msg = "**__SUGGESTION__**"
        msg += "\n "
        msg += "\n**~~`==========`~~**"
        msg += "\nFrom: {} ### {}".format(author, author.id)
        msg += "\nSuggestion: {}".format(args)
        msg += "\n**~~`==========`~~**"
        await client.send_message(chnl, msg)

# ad!report <user/server> <id> <reason>
@client.command(pass_context=True)
async def report(ctx, option = None, target = None, reason = None):
    author = ctx.message.author
    chnl = client.get_channel(main_channel)
    if option == None or target == None or reason == None:
        await client.say(":octagonal_sign: Please use the command correctly.\n`ad!report <user/server> <id> <reason>`")
    else:
        if option == "user":
            await client.say("Reporting...")
            msg = "**__REPORT__**"
            msg += "\n "
            msg += "\n**~~`==========`~~**"
            msg += "\nFrom: {} ### {}".format(author, author.id)
            msg += "\nReported: user - {}".format(target)
            msg += "\nReason: {}".format(reason)
            msg += "\n**~~`==========`~~**"
            await client.send_message(chnl, msg)
        elif option == "server":
            await client.say("Reporting...")
            msg = "**__REPORT__**"
            msg += "\n "
            msg += "\n**~~`==========`~~**"
            msg += "\nFrom: {} ### {}".format(author, author.id)
            msg += "\nReported: server - {}".format(target)
            msg += "\nReason: {}".format(reason)
            msg += "\n**~~`==========`~~**"
            await client.send_message(chnl, msg)
        else:
            await client.say(":octagonal_sign: Please use the command correctly.\n`ad!report <user/server> <id> <reason>`")

''' COMMANDS FOR SERVER OWNERS '''
# ad!shelp
@client.command(pass_context=True)
async def shelp(ctx):
    author = ctx.message.author
    server = ctx.message.server
    if author == server.owner or author.id in bot_moderators:
        msg = "~~**=**~~ Make sure the bot has Administrator permission."
        msg += "\n~~**=**~~ If you are using a bot to log stuff, make an exception for this bot so it doesn't spam your logs."
        msg += "\n~~**=**~~ Use `ad!stypes` to get a list of server types."
        msg += "\n~~**=**~~ Once you find the type you want, use `ad!setup <channel> <type>` and the setup will start. Replace <channel> with the channel you want the bot to use (tag the channel) and <type> with the chosen type. This is case sensitive."
        msg += "\n~~**=**~~ Once the bot is done setting up, use `ad!test` to test if everything is working correctly."
        msg += "\n~~**=**~~ Remember to read the bot's information (`ad!botinfo`)."
        msg += "\n~~**=**~~ If you have any issues with the bot just DM the bot moderators (`ad!support`)."
        await client.say(msg)
    else:
        await client.say(":octagonal_sign: This command can only be used by the server owner and can be bypassed by bot moderators!")

# ad!stypes
@client.command(pass_context=True)
async def stypes(ctx):
    author = ctx.message.author
    server = ctx.message.server
    if author == server.owner or author.id in bot_moderators:
        msg = "~~**=**~~ These are the server types you can chose from: `gaming`, `anime`, `memes`, `nsfw`, `programming`, `community`, `other`."
        await client.say(msg)
    else:
        await client.say(":octagonal_sign: This command can only be used by the server owner and can be bypassed by bot moderators!")

# ad!setup <channel> <type>
@client.command(pass_context=True)
async def setup(ctx, args: discord.Channel = None, args2 = None):
    author = ctx.message.author
    server = ctx.message.server
    if author == server.owner or author.id in bot_moderators:
        if args == None and args2 == None:
            await client.say(":octagonal_sign: Please use the command correctly.\n`ad!shelp` - Gives you help on how to setup your server.\n`ad!stypes` - Gives you a list of types.\n`ad!setup <channel> <type>` - Starts setting up the server.")
        else:
            if server.id in banned_servers:
                await client.say(":octagonal_sign: This server is in the banned list! If you wish to get unbanned, you can contact the bot creator (`ad!support`).")
            elif server.id in servers_ids:
                await client.say(":octagonal_sign: This server is already being advertised! You can use `ad!test` to check if everything is working correctly.")
            elif args2 not in types:
                await client.say(":octagonal_sign: Invalid type! Use `ad!stypes` to see a list of types you can chose from.")
            else:
                try:
                    log = "`THIS IS THE BOT'S SETUP LOG:`"
                    log += "\n**Starting logger...**\n```diff"
                    log += "\n= Trying to get the specified channel's ID..."
                    chnl_id = args.id
                    log += "\n+ Channel's ID found!"
                    log += "\n= Searching for the channel using its ID..."
                    chnl = client.get_channel(chnl_id)
                    log += "\n+ Channel found!"
                    log += "\n= Adding the channel to the list..."
                    channels_ids.append(chnl_id)
                    log += "\n+ Added!"
                    log += "\n= Trying to create an invite for the channel..."
                    invite = await client.create_invite(destination = chnl, xkcd = True, max_uses = 0)
                    log += "\n+ Invite created!"
                    log += "\n= Adding the server's ID to the list..."
                    servers_ids.append(server.id)
                    log += "\n+ Added!"
                    log += "\n= Creating test message..."
                    msg = "**~~__====================__~~**"
                    msg += "\n:a: :regional_indicator_d: "
                    msg += "\n**~~__====================__~~**"
                    msg += "\n "
                    log += "\n= Searching for the server's type..."
                    if args2 == "gaming":
                        log += "\n+ Gaming type found!"
                        msg += "\n:video_game: GAMING SERVER:"
                        log += "\n= Adding the server's ID to the list..."
                        gaming_servers_ids.append(server.id)
                        log += "\n+ Added!"
                        log += "\n= Adding the server's invite to the list..."
                        gaming_servers.append(invite)
                        log += "\n+ Added!"
                    elif args2 == "anime":
                        log += "\n+ Anime type found!"
                        msg += "\n:milky_way: ANIME SERVER:"
                        log += "\n= Adding the server's ID to the list..."
                        anime_servers_ids.append(server.id)
                        log += "\n+ Added!"
                        log += "\n= Adding the server's invite to the list..."
                        anime_servers.append(invite)
                        log += "\n+ Added!"
                    elif args2 == "nsfw":
                        log += "\n+ NSFW type found!"
                        msg += "\n:underage: NSFW SERVER:"
                        log += "\n= Adding the server's ID to the list..."
                        nsfw_servers_ids.append(server.id)
                        log += "\n+ Added!"
                        log += "\n= Adding the server's invite to the list..."
                        nsfw_servers.append(invite)
                        log += "\n+ Added!"
                    elif args2 == "memes":
                        log += "\n+ Memes type found!"
                        msg += "\n:100: MEMES SERVER:"
                        log += "\n= Adding the server's ID to the list..."
                        memes_servers_ids.append(server.id)
                        log += "\n+ Added!"
                        log += "\n= Adding the server's invite to the list..."
                        memes_servers.append(invite)
                        log += "\n+ Added!"
                    elif args2 == "other":
                        log += "\n+ Other type found!"
                        msg += "\n:confetti_ball: FUN SERVER:"
                        log += "\n= Adding the server's ID to the list..."
                        other_servers_ids.append(server.id)
                        log += "\n+ Added!"
                        log += "\n= Adding the server's invite to the list..."
                        other_servers.append(invite)
                        log += "\n+ Added!"
                    elif args2 == "programming":
                        log += "\n+ Programming type found!"
                        msg += "\n:computer: PROGRAMMING SERVER:"
                        log += "\n= Adding the server's ID to the list..."
                        programming_servers_ids.append(server.id)
                        log += "\n+ Added!"
                        log += "\n= Adding the server's invite to the list..."
                        programming_servers.append(invite)
                        log += "\n+ Added!"
                    elif args2 == "community":
                        log += "\n+ Community type found!"
                        msg += "\n:speech_balloon: COMMUNITY SERVER:"
                        log += "\n= Adding the server's ID to the list..."
                        community_servers_ids.append(server.id)
                        log += "\n+ Added!"
                        log += "\n= Adding the server's invite to the list..."
                        community_servers.append(invite)
                        log += "\n+ Added!"
                    else:
                        log += "\n- No type found!"
                        msg += "\n:grey_question: MYSTERIOUS SERVER:"
                        log += "\n= Adding the server's ID to the list..."
                        none_servers_ids.append(server.id)
                        log += "\n+ Added!"
                        log += "\n= Adding the server's invite to the list..."
                        none_servers.append(invite)
                        log += "\n+ Added!"
                    msg += "\n "
                    log += "\n= Compliting the test message... 1/2"
                    log += "\n= Checking server members..."
                    msg += "\n:busts_in_silhouette: {} members!".format(len(server.members))
                    log += "\n= Checking server ID..."
                    msg += "\n:credit_card: ID: {}".format(server.id)
                    log += "\n= Checking server invite link..."
                    msg += "\n:link: Link: {}".format(invite)
                    msg += "\n "
                    log += "\n= Compliting the test message... 2/2"
                    msg += "\n**~~__====================__~~**"
                    msg += "\n:regional_indicator_j: :regional_indicator_o: :regional_indicator_i: :regional_indicator_n:   :regional_indicator_n: :regional_indicator_o: :regional_indicator_w: "
                    msg += "\n**~~__====================__~~**"
                    log += "\n+ Test message created!"
                    log += "\n= Trying to convert the test message into an embed..."
                    embd = discord.Embed(colour=0x00ECFF, description= "")
                    embd.title = ""
                    embd.set_footer(text=footer_text)
                    embd.add_field(name="advertisement", value=msg)
                    log += "\n+ Converting finished!"
                    log += "\n= Sending test message to '{}'...".format(chnl.name)
                    await client.send_message(chnl, "{}".format(invite), embed=embd)
                    log += "\n+ Message sent!"
                    log += "\n= Creating and sending 'new server' message to all other servers..."
                    msg2 = "**~~__====================__~~**"
                    msg2 += "\n:a: :regional_indicator_d: "
                    msg2 += "\n**~~__====================__~~**"
                    msg2 += "\n "
                    if server.id in gaming_servers_ids:
                        msg2 += "\n:video_game: GAMING SERVER:"
                    elif server.id in anime_servers_ids:
                        msg2 += "\n:milky_way: ANIME SERVER:"
                    elif server.id in nsfw_servers_ids:
                        msg2 += "\n:underage: NSFW SERVER:"
                    elif server.id in memes_servers_ids:
                        msg2 += "\n:100: MEMES SERVER:"
                    elif server.id in programming_servers_ids:
                        msg2 += "\n:computer: PROGRAMMING SERVER:"
                    elif server.id in community_servers_ids:
                        msg2 += "\n:speech_balloon: COMMUNITY SERVER:"
                    elif server.id in other_servers_ids:
                        msg2 += "\n:confetti_ball: FUN SERVER:"
                    else:
                        msg2 += "\n:grey_question: MYSTERIOUS SERVER:"
                    msg2 += "\n "
                    msg2 += "\n:busts_in_silhouette: {} members!".format(len(server.members))
                    msg2 += "\n:credit_card: ID: {}".format(server.id)
                    msg2 += "\n:link: Link: {}".format(invite)
                    msg2 += "\n "
                    msg2 += "\n**~~__====================__~~**"
                    msg2 += "\n:regional_indicator_j: :regional_indicator_o: :regional_indicator_i: :regional_indicator_n:   :regional_indicator_n: :regional_indicator_o: :regional_indicator_w: "
                    msg2 += "\n**~~__====================__~~**"
                    embd2 = discord.Embed(colour=0x0017FF, description= "")
                    embd2.set_image(url="{}".format(new_server_img))
                    embd2.title = ""
                    embd2.set_footer(text=footer_text)
                    embd2.add_field(name="new server", value=msg2)
                    for chunel in channels_ids:
                        try:
                            last_channel = client.get_channel(chunel)
                            await client.send_message(last_channel, "{}".format(invite), embed=embd2)
                        except:
                            print("")
                    log += "\n+ Finished sending!"
                    log += "\n= Sending results..."
                    log += "\n+ Finished!"
                    log += "\n```"
                    log += "\n**Closing logger...**"
                    await client.say("This server should be good to go! You can use `ad!test` any time to check if everything is working correctly.")
                    await client.say(log)
                except:
                    log += "\n- ^ Error!"
                    log += "\n```"
                    log += "\n**Closing logger...**"
                    await client.say(":octagonal_sign: Looks like there is an error! Please make sure the bot has all permissions (Administrator) and try again. If you believe that this is a bug, please contact the creator (`ad!support`).")
                    await client.say(log)
    else:
        await client.say(":octagonal_sign: This command can only be used by the server owner and can be bypassed by bot moderators!")

# ad!test <channel>
@client.command(pass_context=True)
async def test(ctx, args: discord.Channel = None):
    author = ctx.message.author
    server = ctx.message.server
    owner = server.owner.id
    if author == server.owner or author.id in bot_moderators:
        if server.id in banned_servers:
            await client.say(":octagonal_sign: This server is in the banned list! If you wish to get unbanned, you can contact the bot creator (`ad!support`).")
        elif server.id in servers_ids or server.id in special_servers_ids:
            if args == None:
                await client.say(":octagonal_sign: Please specify the channel the bot uses in your server!\n`ad!test <channel>`")
            else:
                bot_id = client.user.id
                bot = server.get_member(bot_id)
                log = "`THIS IS THE BOT'S TEST LOG:`"
                log += "\n**Starting logger...**\n```diff"
                log += "\n= Checking if the bot has administrator permissions..."
                if bot.server_permissions.administrator:
                    log += "\n+ The bot has the required permissions!"
                    log += "\n= Searching for the channel's ID in the lists..."
                    if args.id in channels_ids:
                        log += "\n+ Channel found!"
                        log += "\n= Searching for the server's ID in the lists..."
                        if server.id in servers_ids:
                            log += "\n+ Server found!"
                            try:
                                log += "\n= Trying to find the the channel using its ID..."
                                chnl_id = args.id
                                chnl = client.get_channel(chnl_id)
                                log += "\n+ Channel found!"
                                log += "\n= Trying to create a test invite link..."
                                invite = await client.create_invite(destination = chnl, xkcd = True, max_uses = 1)
                                log += "\n+ Test invite created!"
                                log += "\n= Creating test message..."
                                msg = "**~~__====================__~~**"
                                msg += "\n:a: :regional_indicator_d: "
                                msg += "\n**~~__====================__~~**"
                                msg += "\n "
                                log += "\n= Checking the server's type..."
                                if server.id in gaming_servers_ids:
                                    msg += "\n:video_game: GAMING SERVER:"
                                    log += "\n+ Gaming type found!"
                                elif server.id in anime_servers_ids:
                                    msg += "\n:milky_way: ANIME SERVER:"
                                    log += "\n+ Anime type found!"
                                elif server.id in nsfw_servers_ids:
                                    msg += "\n:underage: NSFW SERVER:"
                                    log += "\n+ NSFW type found!"
                                elif server.id in programming_servers_ids:
                                    msg += "\n:computer: PROGRAMMING SERVER:"
                                    log += "\n+ Programming type found!"
                                elif server.id in community_servers_ids:
                                    msg += "\n:speech_balloon: COMMUNITY SERVER:"
                                    log += "\n+ Community type found!"
                                elif server.id in memes_servers_ids:
                                    msg += "\n:100: MEMES SERVER:"
                                    log += "\n+ Memes type found!"
                                elif server.id in other_servers_ids:
                                    msg += "\n:confetti_ball: FUN SERVER:"
                                    log += "\n+ Other type found!"
                                else:
                                    msg += "\n:grey_question: MYSTERIOUS SERVER:"
                                    log += "\n- No type found!"
                                msg += "\n "
                                log += "\n= Checking server members..."
                                msg += "\n:busts_in_silhouette: {} members!".format(len(server.members))
                                log += "\n= Checking server ID..."
                                msg += "\n:credit_card: ID: {}".format(server.id)
                                log += "\n= Checking test invite link..."
                                msg += "\n:link: Test Link: {}".format(invite)
                                log += "\n= Compliting test message..."
                                msg += "\n "
                                msg += "\n**~~__====================__~~**"
                                msg += "\n:regional_indicator_j: :regional_indicator_o: :regional_indicator_i: :regional_indicator_n:   :regional_indicator_n: :regional_indicator_o: :regional_indicator_w: "
                                msg += "\n**~~__====================__~~**"
                                log += "\n+ Test message created!"
                                log += "\n= Trying to convert the test message into an embed..."
                                embd = discord.Embed(colour=0x2AFF00, description= "")
                                embd.set_image(url="{}".format(test_msg_img))
                                embd.title = ""
                                embd.set_footer(text=footer_text)
                                embd.add_field(name="test message", value=msg)
                                log += "\n+ Converting finished!"
                                log += "\n= Sending test message..."
                                await client.send_message(chnl, "<@{}>\n{}".format(owner, invite), embed=embd)
                                log += "\n+ Message sent!"
                                log += "\n= Sending results..."
                                await client.say(":white_check_mark: Looks like everything is working correctly! If you have any issues or believe that there is a bug, please contact the bot creator (`ad!support`). Thanks for using this bot!")
                                log += "\n+ Finished!"
                                log += "\n```\n**Closing logger...**"
                                await client.say(log)
                            except:
                                log += "\n- ^ Error!"
                                log += "\n```\n**Closing logger...**"
                                await client.say(":octagonal_sign: Looks like there is an error! Please contact the bot creator for help (`ad!support`).")
                                await client.say(log)
                        else:
                            log += "\n- Server not found!"
                            log += "\n```\n**Closing logger...**"
                            await client.say(":octagonal_sign: Looks like the server's ID isn't in any of the lists! Please contact the bot creator for help (`ad!support`).")
                            await client.say(log)
                    else:
                        log += "\n- Channel not found!"
                        log += "\n```\n**Closing logger...**"
                        await client.say(":octagonal_sign: Looks like the channel isn't in any lists! Please make sure you mentioned the right channel. Contact the bot creator for help (`ad!support`).")
                        await client.say(log)
                else:
                    log += "\n- The bot doesn't have the required permissions!"
                    log += "\n```\n**Closing logger...**"
                    await client.say(":octagonal_sign: Please give the bot `Administrator` permission and try again!")
                    await client.say(log)
        else:
            await client.say(":octagonal_sign: Looks like this server isn't advertised! Please use `ad!shelp` to setup your server.")
    else:
        await client.say(":octagonal_sign: This command can only be used by the server owner and can be bypassed by bot moderators!")

''' COMMANDS FOR BOT MODERATORS '''
# ad!announce <text>
@client.command(pass_context=True)
async def announce(ctx, *, args = None):
    author = ctx.message.author
    cnsl = client.get_channel(console_channel)
    if author.id in bot_moderators:
        if args == None:
            await client.say(":octagonal_sign: Please use the command correctly.\n`ad!announce <text>`")
        else:
            total = []
            log1 = "**__ANNOUNCE__**"
            log1 += "\n "
            log1 += "\n**~~`==========`~~**"
            log1 += "\nFrom: {} to {} servers...".format(author, len(client.servers))
            log1 += "\n**~~`==========`~~**"
            await client.say("Sending announcement to all servers...")
            await client.send_message(cnsl, log1)
            log = "**__ANNOUNCE__**"
            log += "\n"
            log += "\n**~~`==========`~~**"
            number = []
            for srv in client.servers:
                for chnl_id in channels_ids:
                    try:
                        chnl = client.get_channel(chnl_id)
                        if chnl in srv.channels:
                            number.append("+1")
                            msg = "**~~__>>>>>>>>>>X<<<<<<<<<<__~~**"
                            msg += "\n**`A N N O U N C E M E N T`**"
                            msg += "\n**~~__>>>>>>>>>>X<<<<<<<<<<__~~**"
                            msg += "\n"
                            msg += "\n:loudspeaker: {}".format(args)
                            msg += "\n"
                            msg += "\n:label: Message sent by: `{}`".format(author)
                            msg += "\n"
                            msg += "\n**~~__>>>>>>>>>>X<<<<<<<<<<__~~**"
                            msg += "\n{}/{}".format(len(number), len(client.servers))
                            msg += "\n**~~__>>>>>>>>>>X<<<<<<<<<<__~~**"

                            embd = discord.Embed(colour=0xFF0000, description= "")
                            embd.set_image(url="{}".format(announcement_img))
                            embd.title = ""
                            embd.set_footer(text=footer_text)
                            embd.add_field(name="ANNOUNCEMENT", value=msg)
                            await client.send_message(chnl, embed=embd)
                            total.append("+1")
                        else:
                            print("")
                    except:
                        print("")
            log += "\nFrom: {}\n{}/{}".format(author, len(total), len(client.servers))
            log += "\n**~~`==========`~~**"
            await client.send_message(cnsl, log)      
    else:
        await client.say(":octagonal_sign: This command can only be used by bot moderators!")

# ad!say <server id> <message>
@client.command(pass_context=True)
async def say(ctx, server = None, *, args = None):
    author = ctx.message.author
    cnsl = client.get_channel(console_channel)
    if author.id in bot_moderators:
        if server == None or args == None:
            await client.say(":octagonal_sign: Please use the command correctly.\n`ad!say <server id> <message>`")
        else:
            log = "**__SAY__**"
            log += "\n "
            log += "\n**~~`==========`~~**"
            log += "\nFrom: {}\nTo the server with the following ID: {}...".format(author, server)
            log += "\n**~~`==========`~~**"
            await client.send_message(cnsl, log)
            await client.say("Sending message...")
            log1 = "**__SAY__**"
            log1 += "\n "
            log1 += "\n**~~`==========`~~**"
            for srv in client.servers:
                for chnl_id in channels_ids:
                    if srv.id == server:
                        try:
                            owner = srv.owner.id
                            chnl = client.get_channel(chnl_id)
                            if chnl in srv.channels:
                                await client.send_message(chnl, ":loudspeaker: {}\n \n:label: Message sent by: `{}`\n \n<@{}>".format(args, author, owner))
                                log1 += "\nFrom: {}\nTo the server with the following ID: {}!".format(author, server)
                            else:
                                print("")
                        except:
                            print("")
                    else:
                        print("")
            log1 += "\n**~~`==========`~~**"
            await client.send_message(cnsl, log1)
    else:
        await client.say(":octagonal_sign: This command can only be used by bot moderators!")

# ad!force
@client.command(pass_context=True)
async def force(ctx):
    author = ctx.message.author
    cnsl_chnl = client.get_channel(console_channel)
    if author.id in bot_moderators:
        await client.say("Sending advertisements...")
        sent = []
        total = []
        log1 = "**__FORCE AD__**"
        log1 += "\n "
        log1 += "\n**~~`==========`~~**"
        log1 += "\nFrom: {}".format(author)
        await client.send_message(cnsl_chnl, log1)
        log1 += "\n**~~`==========`~~**"
        log = "**__FORCE AD__**"
        log += "\n "
        log += "\n**~~`==========`~~**"
        for channel in channels_ids:
            rnd_server_id = random.choice(servers_ids)
            msg = "**~~__====================__~~**"
            if rnd_server_id in special_servers_ids:
                msg += "\n:star:   :a: :regional_indicator_d:   :star: "
            else:
                msg += "\n:a: :regional_indicator_d: "
            msg += "\n**~~__====================__~~**"
            msg += "\n "
            if rnd_server_id in special_servers_ids:
                invite = random.choice(special_links)
                msg += "\n:star2: __**AMAZING SERVER**__ :star2:"
                msg += "\n "
                msg += "\n:link: Link: {}".format(invite)
            else:
                if rnd_server_id in gaming_servers_ids:
                    invite = random.choice(gaming_servers)
                    msg += "\n:video_game: GAMING SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                elif rnd_server_id in anime_servers_ids:
                    invite = random.choice(anime_servers)
                    msg += "\n:milky_way: ANIME SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                elif rnd_server_id in nsfw_servers_ids:
                    invite = random.choice(nsfw_servers)
                    msg += "\n:underage: NSFW SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                elif rnd_server_id in community_servers_ids:
                    invite = random.choice(community_servers)
                    msg += "\n:speech_balloon: COMMUNITY SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                elif rnd_server_id in programming_servers_ids:
                    invite = random.choice(programming_servers)
                    msg += "\n:computer: PROGRAMMING SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                elif rnd_server_id in memes_servers_ids:
                    invite = random.choice(memes_servers)
                    msg += "\n:100: MEMES SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                elif rnd_server_id in other_servers_ids:
                    invite = random.choice(other_servers)
                    msg += "\n:confetti_ball: FUN SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
                else:
                    invite = random.choice(none_servers)
                    msg += "\n:grey_question: MYSTERIOUS SERVER:"
                    msg += "\n "
                    msg += "\n:link: Link: {}".format(invite)
            msg += "\n "
            msg += "\n**~~__====================__~~**"
            msg += "\n:regional_indicator_j: :regional_indicator_o: :regional_indicator_i: :regional_indicator_n:   :regional_indicator_n: :regional_indicator_o: :regional_indicator_w: "
            msg += "\n**~~__====================__~~**"
            if rnd_server_id in special_servers_ids:
                embd = discord.Embed(colour=0xFF9B00, description= "")
                embd.set_image(url="{}".format(special_server_img))
                embd.add_field(name="special advertisement", value=msg)
            else:
                embd = discord.Embed(colour=0x00ECFF, description= "")
                embd.add_field(name="advertisement", value=msg)
            embd.title = ""
            embd.set_footer(text=footer_text)
            try:
                chnl = client.get_channel(channel)
                await client.send_message(chnl, "{}".format(invite), embed=embd)
                sent.append("+1")
            except:
                total.append("+1")
        log += "\nFrom: {}\nSent: {}\nFailed: {}".format(author, len(sent), len(total))
        log += "\n**~~`==========`~~**"
        await client.send_message(cnsl_chnl, log)
    else:
        await client.say(":octagonal_sign: This command can only be used by bot moderators!")

# ad!ban <user/server> <id> <reason>
@client.command(pass_context=True)
async def ban(ctx, args = None, target = None, *, reason = None):
    author = ctx.message.author
    cnsl_chnl = client.get_channel(console_channel)
    if author.id in bot_moderators:
        if args == None or target == None or reason == None:
            await client.say(":octagonal_sign: Please use the command correctly.\n`ad!ban <user/server> <id> <reason>`")
        else:
            if args == "user":
                banned = []
                await client.say("Banning user from all servers...")
                for server in client.servers:
                    try:
                        user = server.get_member(target)
                        await client.ban(user)
                    except:
                        banned.append("+1")
                log = "**__USER BAN__**"
                log += "\n "
                log += "\n**~~`==========`~~**"
                log += "\nBanner: {}\n Target's ID: {}\nBanned from {} servers out of {}\nReason: {}".format(author, target, len(banned), len(client.servers), reason)
                log += "\n**~~`==========`~~**"
                await client.send_message(cnsl_chnl, log)
            elif args == "server":
                await client.say("Banning server...")
                try:
                    banned_servers.append(target)
                    servers_ids.remove(target)
                    if target in special_servers_ids:
                        special_servers_ids.remove(target)
                    elif target in gaming_servers_ids:
                        gaming_servers_ids.remove(target)
                    elif target in anime_servers_ids:
                        anime_servers_ids.remove(target)
                    elif target in nsfw_servers_ids:
                        nsfw_servers_ids.remove(target)
                    elif target in community_servers_ids:
                        community_servers_ids.remove(target)
                    elif target in programming_servers_ids:
                        programming_servers_ids.remove(target)
                    elif target in memes_servers_ids:
                        memes_servers_ids.remove(target)
                    elif target in other_servers_ids:
                        other_servers_ids.remove(target)
                    else:
                        none_servers_ids.remove(target)
                except:
                    print("")
                log = "**__SERVER BAN__**"
                log += "\n "
                log += "\n**~~`==========`~~**"
                log += "\nBanner: {}\nServer ID: {}\nReason: {}".format(author, target, reason)
                log += "\n**~~`==========`~~**"
                await client.send_message(cnsl_chnl, log)
            else:
                await client.say(":octagonal_sign: Please use the command correctly.\n`ad!ban <user/server> <id> <reason>`")
    else:
        await client.say(":octagonal_sign: This command can only be used by bot moderators!")

# ad!unban <user/server> <id>
@client.command(pass_context=True)
async def unban(ctx, option = None, target = None):
    author = ctx.message.author
    cnsl_chnl = client.get_channel(console_channel)
    if author.id in bot_moderators:
        if option == None:
            await client.say(":octagonal_sign: Please use the command correctly.\n`ad!unban <user/server> <id>`")
        elif option == "user":
            await client.say("Unbanning...")
            total = []
            for server in client.servers:
                try:
                    banned_users = await client.get_bans(server)
                    user = discord.utils.get(banned_users,id=target)
                    await client.unban(server, user)
                    total.append("+1")
                except:
                    print("")
            log = "**__USER UNBAN__**"
            log += "\n "
            log += "\n**~~`==========`~~**"
            log += "\nUnbanner: {}\nTarget's ID: {}\nUnbanned from {} servers out of {}!".format(author, target, len(total), len(client.servers))
            log += "\n**~~`==========`~~**"
            await client.send_message(cnsl_chnl, log)
        elif option == "server":
            await client.say("Unbanning...")
            try:
                banned_servers.remove(target)
            except:
                print("")
            log = "**__SERVER UNBAN__**"
            log += "\n "
            log += "\n**~~`==========`~~**"
            log += "\nUnbanner: {}\nServer ID: {}!".format(author, target)
            log += "\n**~~`==========`~~**"
            await client.send_message(cnsl_chnl, log)
        else:
            await client.say(":octagonal_sign: Please use the command correctly.\n`ad!unban <user/server> <id>`")
    else:
        await client.say(":octagonal_sign: This command can only be used by bot moderators!")

# ad!dm <server id> <message>
@client.command(pass_context=True)
async def dm(ctx, target = None, *, args = None):
    author = ctx.message.author
    cnsl_chnl = client.get_channel(console_channel)
    if author.id in bot_moderators:
        log = "**__DM__**"
        log += "\n "
        log += "\n**~~`==========`~~**"
        if target == None or args == None:
            await client.say(":octagonal_sign: Please use the command correctly.\n`ad!dm <server id> <message>`")
        else:
            await client.say("DMing...")
            for server in client.servers:
                if server.id == target:
                    user = server.owner
                    try:
                        await client.send_message(user, args)
                        log += "\nSent from: {}\nServer ID: {}\nSuccess!".format(author, target)
                    except:
                        log += "\nSent from: {}\nServer ID: {}\nFailed!".format(author, target)
                else:
                    print("")
            log += "\n**~~`==========`~~**"
            await client.send_message(cnsl_chnl, log)
    else:
        await client.say(":octagonal_sign: This command can only be used by bot moderators!")

# ad!delete <server id>
@client.command(pass_context=True)
async def delete(ctx, args = None):
    author = ctx.message.author
    if author.id in bot_moderators:
        if args == None:
            await client.say(":octagonal_sign: Please use the command correctly.\n`ad!delete <server id>`")
        else:
            try:
                await client.say("Removing server...")
                servers_ids.remove(args)
                if args in gaming_servers_ids:
                    gaming_servers_ids.remove(args)
                elif args in anime_servers_ids:
                    anime_servers_ids.remove(args)
                elif args in nsfw_servers_ids:
                    nsfw_servers_ids.remove(args)
                elif args in memes_servers_ids:
                    memes_servers_ids.remove(args)
                elif args in other_servers_ids:
                    other_servers_ids.remove(args)
                elif args in community_servers_ids:
                    community_servers_ids.remove(args)
                elif args in programming_servers_ids:
                    programming_servers_ids.remove(args)
                else:
                    none_servers_ids.remove(args)
                for server in client.servers:
                    if server.id == args:
                        try:
                            links = await client.invites_from(server)
                            for link in links:
                                if args in gaming_servers_ids:
                                    gaming_servers.remove(link)
                                elif args in anime_servers_ids:
                                    anime_servers.remove(link)
                                elif args in nsfw_servers_ids:
                                    nsfw_servers.remove(link)
                                elif args in memes_servers_ids:
                                    memes_servers.remove(link)
                                elif args in other_servers_ids:
                                    other_servers.remove(link)
                                elif args in community_servers_ids:
                                    community_servers.remove(link)
                                elif args in programming_servers_ids:
                                    programming_servers.remove(link)
                                else:
                                    none_servers.remove(link)
                        except:
                            print("")
                    else:
                        print("")
                await client.say(":white_check_mark: Server removed!")
            except:
                await client.say(":octagonal_sign: Error in removing server!")
    else:
        await client.say(":octagonal_sign: This command can only be used by bot moderators!")
        
''' COMMANDS FOR THE BOT CREATOR '''
# ad!mod <del/add> <user>
@client.command(pass_context=True)
async def mod(ctx, option = None, user: discord.User = None):
    author = ctx.message.author
    if author.id == bot_creator:
        if option == None or user == None:
            await client.say(":octagonal_sign: Please use the command correctly.\n`ad!mod <del/add> <user>`")
        else:
            if option == "add":
                if user.id in bot_moderators:
                    await client.say(":octagonal_sign: That user is already a bot moderator!")
                else:
                    bot_moderators.append(user.id)
                    await client.say(":white_check_mark: {} ### {} - has been added to the bot moderators list!".format(user.display_name, user.id))
            elif option == "del":
                if user.id in bot_moderators:
                    bot_moderators.remove(user.id)
                    await client.say(":white_check_mark: {} ### {} - has been removed from the bot moderators list!".format(user.display_name, user.id))
                else:
                    await client.say(":octagonal_sign: That user is not a bot moderator!")
            else:
                await client.say(":octagonal_sign: Please use the command correctly.\n`ad!mod <del/add> <user>`")
    else:
        await client.say(":octagonal_sign: This command can only be used by the bot creator!")

# ad!special <add/del> <server id> <server link>
@client.command(pass_context=True)
async def special(ctx, add = None, server = None, link = None):
    author = ctx.message.author
    cnsl_chnl = client.get_channel(console_channel)
    if author.id == bot_creator:
        if add == None or server == None or link == None:
            await client.say(":octagonal_sign: Please use the command correctly.\n`ad!special <add/del> <server id> <server link>`")
        else:
            log = "`THIS IS THE BOT'S LOG:`"
            log += "\n**Starting logger...**\n```diff"
            if add == "add":
                log += "\n+ Add option chosen!"
                if server in special_servers_ids:
                    log += "\n- That server ID is already in the list!"
                    log += "\n```\n**Closing logger...**"
                    await client.say(log)
                elif link in special_links:
                    log += "\n- That link is already in the list!"
                    log += "\n```\n**Closing logger...**"
                    await client.say(log)
                else:
                    try:
                        log += "\n= Trying to add the link to the list..."
                        special_links.append(link)
                        log += "\n+ Added!"
                        log += "\n= Trying to add the server's ID to the list..."
                        special_servers_ids.append(server)
                        log += "\n+ Added!"
                        log += "\n= Sending results..."
                        await client.say(":white_check_mark: Server is now marked as 'special'!")
                        log += "\n+ Finished!"
                        log += "\n```\n**Closing logger...**"
                        await client.say(log)
                    except:
                        log += "\n- ^ Error!"
                        log += "\n```\n**Closing logger...**"
                        await client.say(log)
                    log1 = "**__SPECIAL__**"
                    log1 += "\n "
                    log1 += "\n**~~`==========`~~**"
                    log1 += "\nFrom: {}\nServer ID: {}\nServer Link: {}".format(author, server, link)
                    log1 += "\n**~~`==========`~~**"
                    await client.send_message(cnsl_chnl, log1)
            elif add == "del":
                log += "\n+ Remove option chosen!"
                if server not in special_servers_ids:
                    log += "\n- That server ID is not in the list!"
                    log += "\n```\n**Closing logger...**"
                    await client.say(log)
                elif link not in special_links:
                    log += "\n- That link is not in the list!"
                    log += "\n```\n**Closing logger...**"
                    await client.say(log)
                else:
                    try:
                        log += "\n= Trying to remove the link from the list..."
                        special_links.remove(link)
                        log += "\n+ Removed!"
                        log += "\n= Trying to remove the server's ID from the list..."
                        special_servers_ids.remove(server)
                        log += "\n+ Removed!"
                        log += "\n= Sending results..."
                        await client.say(":white_check_mark: Server is no longer marked as 'special'!")
                        log += "\n+ Finished!"
                        log += "\n```\n**Closing logger...**"
                        await client.say(log)
                    except:
                        log += "\n- ^ Error!"
                        log += "\n```\n**Closing logger...**"
                        await client.say(log)
                    log1 = "**__SPECIAL__**"
                    log1 += "\n "
                    log1 += "\n**~~`==========`~~**"
                    log1 += "\nFrom: {}\nServer ID: {}\nServer Link: {}".format(author, server, link)
                    log1 += "\n**~~`==========`~~**"
                    await client.send_message(cnsl_chnl, log1)
            else:
                await client.say(":octagonal_sign: `ad!special <add/del> <server id> <server link>`")
    else:
        await client.say(":octagonal_sign: This command can only be used by the bot creator!")

# TURNS THE BOT ON
client.run(os.environ['BOT_TOKEN'])
