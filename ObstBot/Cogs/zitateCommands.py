# ToDO Zitate
# 	Zitat

import discord
from discord.ext import commands
import logging
from UI import addZitate
import random as r

class Zitate(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lodad Zitate Comands")

    @commands.command(brief='Füge ein Zitat hinzu', description='Erstelle eine Random RGB Farbe')
    async def addZitat(self, ctx: discord.ext.commands.Context):
        await ctx.send("", view=addZitate.ZitatButtons(), delete_after=15)
        await ctx.message.delete()
        logging.info(f"Random RGB wurde ausgeführt")

    @commands.command(brief='Random Zitat', description='Schreibet ein random Zitat in den Zitate Channel')
    async def Zitat(self, ctx: discord.ext.commands.Context):
        zitate_id = list()
        zitate_archive = self.bot.get_channel(960954169840271443)
        [zitate_id.append(message) async for message in zitate_archive.history(limit=123)]

        # zitate_archive = self.bot.get_channel(960954169840271443)
        # zitate_id.append([message async for message in zitate_archive.history(limit=123)])

        # zitate_archive = self.bot.get_channel(960954169840271443)
        # zitate_id.append([message async for message in zitate_archive.history(limit=123)])
        msg: discord.Message = r.choice(zitate_id)

        ctx.send(msg.content,delete_after=10)


async def setup(bot):
    print("Loading Zitate Cog ...")
    await bot.add_cog(Zitate(bot))
