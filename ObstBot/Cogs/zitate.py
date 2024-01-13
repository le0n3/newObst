#ToDO Zitate
#   addZitat
# 	Zitat
import discord
from discord.ext import commands
import logging
from Helper import *

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lodad Random Comands")

    @commands.command(brief='Random RGB Wert', description='Erstelle eine Random RGB Farbe')
    async def randomRGB(self, ctx: discord.ext.commands.Context):

        await ctx.send(random_rgb(),delete_after= 15)
        await ctx.message.delete()
        logging.info(f"Random RGB wurde ausgeführt")




async def setup(bot):
    print("Loading Random Cog ...")
    await bot.add_cog(Random(bot))
