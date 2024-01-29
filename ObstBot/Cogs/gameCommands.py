import discord
import random
from discord.ext import commands
import logging
from ObstBot.UI.tictactoe import TicTacToe
from ObstBot.UI.Games import HiorLow
from ObstBot.Datenbank import GetCredits, SocialCreditEdit
from ObstBot.DiscordeLogging import DLogging

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lodad Games Commands")

    @commands.command(brief='AllIn',
                      description='Lege alle deine Credits auf die Kannte und Verlier oder gewinne alles')
    async def AllIn(self, ctx: discord.ext.commands.Context):
        Number = random.randint(0, 1)
        await ctx.message.delete()
        Credits = GetCredits(ctx.author)
        if Credits > 0:
            if Number == 0:
                SocialCreditEdit(ctx.author, (Credits - (Credits * 2)))
                await ctx.send("Du hasst alle Credits Verlohren 😭", delete_after=10)
                await DLogging.Info(f"AllIn wurde von {ctx.author.name} aufgerufen und hat alle Credits Verlohren", self.bot)

            if Number == 1:
                SocialCreditEdit(ctx.author, Credits * 2)
                await ctx.send("Du hast deine Credits Verdoppelt", delete_after=10)
                await DLogging.Info(f"AllIn wurde von {ctx.author.name} aufgerufen und hat seie Credit Verdoppelt", self.bot)
        else:
            await ctx.send("Du hast keine Credits zum Setzen", delete_after=10)
            await DLogging.Info(f"AllIn wurde von {ctx.author.name} aufgerufen er hatte nicht genug Credits", self.bot)

    @commands.command(brief='HiOrLow',
                      description='Rate ob die Zahl höher oder niedriger als 6 ist und gewinne gewinne gewinne')
    async def HiorLow(
            self, ctx: discord.ext.commands.Context, BetCredits: str = commands.parameter(default="0",
            description="Die Anzahl diener Socal Credits die du Einsetzten Möchtest")):
        Credits = int(GetCredits(ctx.author))
        await ctx.message.delete()
        try:
            if Credits > int(BetCredits):
                await ctx.send("Hi or Low", view=HiorLow(int(BetCredits), ctx.author))
                await DLogging.Info(f"HiorLow wurde von {ctx.author.name} ausfgeführt", self.bot)
        except:
            await ctx.send("Du musste eine Zahl angeben")
            await DLogging.Error(f"HiorLow wurde von {ctx.author.name} ausgefüht er hat keine Zahl angegeben", self.bot)

    @commands.command(brief='TicTacToe',
                      description='Rate die Zahl und gewinne gewinne gewinne')
    async def TicTacToe(self, ctx: discord.ext.commands.Context):
        await ctx.send("TicTacToe", view=TicTacToe())
        await ctx.message.delete()
        logging.info(f"TicTacToe wird gespielt")
        await DLogging.Info(f"TicTacToe wurde von {ctx.author.name} ausfgeführt", self.bot)


async def setup(bot):
    print("Loading Game Cog ...")
    await bot.add_cog(Game(bot))
