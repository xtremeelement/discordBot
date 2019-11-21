import os
import datetime
from discord.ext import commands
import discord
import json
import requests


client = commands.Bot(command_prefix='!')


print('Bot is booting up...')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

@client.event
async def on_ready():
    print('Bot is loading scripts...')
    print(os.getcwd())
    os.chdir('\\discordBot')
    print(os.getcwd())


for filename in os.listdir('\\discordBot2\\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
async def commands(ctx):
    with open('commands.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def test(ctx):
    with open('test.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


# Log Stuff
@client.command()
async def fflogs(ctx):
    with open('fflogs.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


# Loot list
@client.command()
async def lootlist(ctx):
    with open('lootlist.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


# Dark Knight stuff
@client.command()
async def drkbis(ctx):
    with open('drkbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def drkrotation(ctx):
    with open('drkrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


# Gunbreaker stuff
@client.command()
async def gnbbis(ctx):
    with open('gnbbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def gnbrotation(ctx):
    with open('gnbrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


# Warrior Stuff
@client.command()
async def warbis(ctx):
    with open('warbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def warrotation(ctx):
    with open('warrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


# Scholar Stuff
@client.command()
async def schbis(ctx):
    with open('schbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def schrotation(ctx):
    with open('schrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


# Whitemage Stuff
@client.command()
async def whmbis(ctx):
    with open('whmbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def whmrotation(ctx):
    await ctx.send('```LoL white mages dont have a rotation, glare bot```')
    print('Completed user request')


# Astrologian stuff
@client.command()
async def astbis(ctx):
    with open('astbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def astrotation(ctx):
    with open('astrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


# Dragoon Stuff
@client.command()
async def drgbis(ctx):
    with open('drgbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def drgrotation(ctx):
    with open('drgrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def mnkbis(ctx):
    with open('mnkbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def mnkrotation(ctx):
    with open('mnkrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def ninbis(ctx):
    with open('ninbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def ninrotation(ctx):
    with open('ninrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def brdbis(ctx):
    with open('brdbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def brdrotation(ctx):
    with open('brdrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def dncbis(ctx):
    with open('dncbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def dncrotation(ctx):
    with open('dncrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def mchrotation(ctx):
    with open('mchrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def mchbis(ctx):
    with open('mchbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def blmbis(ctx):
    with open('blmbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def blmrotation(ctx):
    with open('blmrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def rdmbis(ctx):
    with open('rdmbis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def rdmrotation(ctx):
    with open('rdmrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def smnbis(ctx):
    with open('smnrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def smnrotation(ctx):
    with open('smnrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def sambis(ctx):
    nowlog = datetime.datetime.now()
    with open('sambis.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')
    with open('log.txt', 'a') as f:
        f.write('{} completed user request\n'.format(nowlog))


@client.command()
async def samrotation(ctx):
    with open('samrotation.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def static(ctx):
    with open('static.txt', 'r') as f:
        f_contents = f.read()
        await ctx.send(f_contents)
        print('Completed user request')


@client.command()
async def mylogs(ctx, firstName, lastName, server):
    url = ('http://fflogs.com/character/na/{}/{}%20{}' .format(server, firstName, lastName))
    await ctx.send(url)
    print('completed user request mylogs', firstName, lastName, server)


@client.command()
async def myid(ctx):
    my_id = ctx.author.id
    print(my_id)


@client.command()
async def kick(ctx, member : discord.Member):
    if ctx.author.id == 49290412937969664:
        await member.kick()


# user leaving channel
@client.event
async def on_member_remove(ctx, member : discord.Member):
    await ctx.send(f'{member} has left the server.')


@client.command()
async def testshit(ctx):
    await ctx.send(c)
    await ctx.send('''Hello everyone
    THis is a test:
    http:www.google.com
    another shit''')


@client.command()
async def userids(ctx, member : discord.Member):
    print(member.id)


client.run('insert discord bot token here')