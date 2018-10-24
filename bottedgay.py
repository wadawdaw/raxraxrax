import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
 
Client = discord.Client()
bot_prefix= "/"
client = commands.Bot(command_prefix=bot_prefix)
 
@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    #Extra 1
    await client.change_presence(game=discord.Game(name='type /help'))
 
@client.command(pass_context=True)
async def rules(ctx):
    await client.say("""**
===========
Rules of BLiTZ
===========
- Do not impersonating People
- Do not spam
- Do not swearing
- Do not say inappropriate words 
- Do not talk about hacking Here!
- Do not send .exe files [insult banned]
- Do not bullying others
====================
Last edited : Fri, August 31.
====================""")
#command1
@client.command(pass_context = True)
async def invite(ctx):
    x = await client.invites_from(ctx.message.server)
    x = ["<" + y.url + ">" for y in x]
    print(x)
    embed = discord.Embed(title = "Invite Links", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context = True)
async def help(ctx):
    x = await client.say("""**COMMANDS: 
    /invite
    /getbans
    /connect
    /disconnect
    /clear
    /ban
    /kick
    /listservers
    /info
    """)
    print(x)
    embed = discord.Embed(title = "Servers", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
#command2
@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
 
#command3
@client.command(pass_context=True)
async def connect(ctx):
    if client.is_voice_connected(ctx.message.server):
        return await client.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)
 
#command4
@client.command(pass_context = True)
async def disconnect(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()
 
#command5
@client.command(pass_context=True)       
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)

#command6
@client.command(pass_context = True)
async def ban(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return

    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to ban!")
    try:
        await client.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")

    embed = discord.Embed(description = "**%s** has been banned!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)

#command7
@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return

    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to kick!")
    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")

    embed = discord.Embed(description = "**%s** has been kicked!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)

#command8
@client.command(pass_context = True)
async def listservers(ctx):
    x = '\n'.join([str(server) for server in client.servers])
    print(x)
    embed = discord.Embed(title = "Servers", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context=True)
async def whomade(ctx):
    await client.say("This bot by NabzGT Aka Blank")
	
#command9
@client.command(pass_context = True)
async def info(ctx):
    await client.say("""**Useful Links:**
Discord Invite: https://discord.gg/n45JcWb

Roles:
@Owner - Owners Of BLiTZ
@Co-owners  - Owners but lower level
@Helpers - helpers who are idiots
@members - normal memebers

Any issues please **PM** @Owners directly.""")

      
client.run("NTA0NjI2MzY3ODk2MzU0ODIx.DrHxiw.b8GyG48Fs84Kuv_iJSN6WTHIv1E")
