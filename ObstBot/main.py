import asyncio
import discord
import ObstBotClass as ObstBot
import config
import logging


bot = ObstBot.ObstBot()


@bot.event
async def on_raw_reaction_add(reaction: discord.RawReactionActionEvent):
    pass


async def load():

    await bot.load_extension("Cogs.random")


async def main():
    if __name__ == '__main__':
        await load()
        handler = logging.FileHandler(filename='ObstBot/Log/discord.log', encoding='utf-8', mode='w')
        await bot.start(config.getBotKey(), log_handler=handler)


asyncio.run(main())