from discord.ext import commands
import discord

async def Logging(bot: commands.Bot, type: str , message: str):
    channel: discord.TextChannel = bot.get_channel(978647339998785536)
    if type == "info":
        await channel.send("[INFO] " + message)

    if type == "warning":
        await channel.send("[WARNING] " + message)

    if type == "error":
        await channel.send("[ERROR] " + message)

    if type == "debug":
        await channel.send("[DEBUG] " + message)


async def Info(Message, Bot: commands.Bot):
    await Logging(Bot, type = "info", message = Message)


async def Warning(Message, Bot: commands.Bot):
    await Logging(Bot, type = "warning", message = Message)


async def Error(Message, Bot: commands.Bot):
    await Logging(Bot, type="error", message=Message)

async def Debug(Message, Bot: commands.Bot):
    await Logging(Bot, type="debug", message = Message)