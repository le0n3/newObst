import discord
from discord.ext import commands

TOKEN = 'YOUR_BOT_TOKEN'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} hat sich mit Discord verbunden!')

@bot.command(name='hallo', help='Antwortet mit Hallo Welt!')
async def hallo(ctx):
    await ctx.send('Hallo Welt!')

bot.run(TOKEN)