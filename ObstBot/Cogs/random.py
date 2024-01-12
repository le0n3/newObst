import discord
from discord.ext import commands
import logging
from ObstBot.Helper import *

# ToDo Random Commands
#	 randomRGB
#	 randomHEX
#	 tobin
#	 tohex
#	 iss
#	 wetter
#	 joke


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

    @commands.command(brief='Random HEX Farbe ', description='Erstellt eine Random HEX Farbe')
    async def randomHex(self,ctx: discord.ext.commands.Context  ):
        await ctx.send(random_hex(), delete_after=15)
        await ctx.message.delete()
        logging.info(f"Random HEX wurde ausgeführt")

    @commands.command(brief='Converter to Binär ', description='Convertiert eine Decimal zahl zu einer Binär Zahl')
    async def toBin(self,ctx: discord.ext.commands.Context, decimalNumber:str ):
        await ctx.send(decimal_to_binary(int(decimalNumber)), delete_after=15)
        await ctx.message.delete()
        logging.info(f"To Bin wurde ausgeführt")


    @commands.command(brief='Converter to Hexadezimal', description='Convertiert eine Decimal zahl zu einer Hexadezimal'
                                                                    ' Zahl')
    async def toHex(self,ctx: discord.ext.commands.Context, decimalNumber: str):
        await ctx.send(decimal_to_hex(int(decimalNumber)), delete_after=15)
        await ctx.message.delete()
        logging.info(f"To Hex wurde ausgeführt")

    @commands.command(brief='Abfrage der ISS', description='Zeigt die Position der Iss und alle astronauten die grade '
                                                           'durchs Weltall fliegen')
    async def ISS(self,ctx: discord.ext.commands.Context):
        await ctx.send(iss(), delete_after=15)
        await ctx.message.delete()
        logging.info(f"ISS wurde ausgeführt")


    @commands.command(brief='Abfrage des Wetters', description='Zeigt das Aktuelle Wetter an der BS1 an')
    async def Wetter(self,ctx: discord.ext.commands.Context):
        await ctx.send(wether(), delete_after=15)
        await ctx.message.delete()
        logging.info(f"Wetter wurde ausgeführt")


    @commands.command(brief='Dad Joke', description='Erzählt einen lustigen Dad Joke ;D')
    async def Joke(self,ctx: discord.ext.commands.Context):
        await ctx.send(joke(), delete_after=15)
        await ctx.message.delete()
        logging.info(f"Joke wurde ausgeführt")



async def setup(bot):
    print("Loading Random Cog ...")
    await bot.add_cog(Random(bot))
