import discord
import datetime
import time
import json
import requests
from discord.ext import commands


class botStuff(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def ilvl(self, ctx, first_name, last_name, server):
        await ctx.send('Processing Please wait...')
        gearset = []
        r = requests.get(f'https://xivapi.com/character/search?name={first_name}%20{last_name}&server={server}')
        time.sleep(2)
        the_goods = r.json()
        the_goods_sorted = json.dumps(the_goods['Results'][0]['ID'])
        time.sleep(2)
        c = requests.get(f'https://xivapi.com/character/{the_goods_sorted}')
        time.sleep(2)
        character = c.json()
        body = json.dumps(character['Character']['GearSet']['Gear']['Body']['ID'])
        bracelets = json.dumps(character['Character']['GearSet']['Gear']['Bracelets']['ID'])
        earrings = json.dumps(character['Character']['GearSet']['Gear']['Earrings']['ID'])
        feet = json.dumps(character['Character']['GearSet']['Gear']['Feet']['ID'])
        hands = json.dumps(character['Character']['GearSet']['Gear']['Hands']['ID'])
        head = json.dumps(character['Character']['GearSet']['Gear']['Head']['ID'])
        legs = json.dumps(character['Character']['GearSet']['Gear']['Legs']['ID'])
        mainhand = json.dumps(character['Character']['GearSet']['Gear']['MainHand']['ID'])
        necklace = json.dumps(character['Character']['GearSet']['Gear']['Necklace']['ID'])
        ring1 = json.dumps(character['Character']['GearSet']['Gear']['Ring1']['ID'])
        ring2 = json.dumps(character['Character']['GearSet']['Gear']['Ring2']['ID'])
        waist = json.dumps(character['Character']['GearSet']['Gear']['Waist']['ID'])
        await ctx.send('Character loaded please wait...')
        gearset.append(bracelets)
        gearset.append(body)
        gearset.append(earrings)
        gearset.append(feet)
        gearset.append(hands)
        gearset.append(head)
        gearset.append(legs)
        gearset.append(mainhand)
        gearset.append(necklace)
        gearset.append(ring1)
        gearset.append(ring2)
        gearset.append(waist)
        gear_levels = []
        #whatever = ['ItemCategory']['LevelItem']
        for item in gearset:
            h = requests.get(f'https://xivapi.com/item/{item}')
            time.sleep(1)
            new_item = h.json()
            new_item_sorted = json.dumps(new_item['LevelItem'])
            gear_levels.append(new_item_sorted)

        print(gear_levels)
        new_gear_levels = list(map(int, gear_levels))
        ilvl = round(sum(new_gear_levels)/len(new_gear_levels))
        await ctx.send(f'Your current iLVL is {ilvl}')


def setup(client):
    client.add_cog(botStuff(client))


