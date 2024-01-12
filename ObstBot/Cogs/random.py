import discord
from discord.ext import commands

# ToDo Random Commands
#	randomRGB
#	randomHEX
#	tobin
#	tohex
#	iss
#	wetter
#	joke


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lodad Random Comands")

    @commands.command(brief='Random RGB Wert', description='Erstelle eine Random RGB Farbe')
    async def randomRGB(self, ctx: discord.ext.commands.Context):
        await ctx.reply("Erstelle eine Random RGB", ephemeral=True)
        await ctx.message.delete()



    @commands.command(brief='Random HEX Farbe ', description='Erstellt eine Random HEX Farbe')
    async def randomHex(self,ctx: discord.ext.commands.Context):
        pass

    @commands.command(brief='Converter to Binär ', description='Convertiert eine Decimal zahl zu einer Binär Zahl')
    async def toBin(self,ctx: discord.ext.commands.Context):
        pass

    @commands.command(brief='Converter to Hexadezimal', description='Convertiert eine Decimal zahl zu einer Hexadezimal'
                                                                    ' Zahl')
    async def toHex(self,ctx: discord.ext.commands.Context):
        pass

    @commands.command(brief='Abfrage der ISS', description='Zeigt die Position der Iss und alle astronauten die grade '
                                                           'durchs Weltall fliegen')
    async def ISS(self,ctx: discord.ext.commands.Context):
        pass

    @commands.command(brief='Abfrage des Wetters', description='Zeigt das Aktuelle Wetter an der BS1 an')
    async def Wetter(self,ctx: discord.ext.commands.Context):
        pass

    @commands.command(brief='Dad Joke', description='Erzählt einen lustigen Dad Joke ;D')
    async def Joke(self,ctx: discord.ext.commands.Context):
        pass


async def setup(bot):
    print("Loading Random Cog ...")
    await bot.add_cog(Random(bot))
