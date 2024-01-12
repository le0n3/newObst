import discord
from discord.ext import commands
import logging
import os
import datetime

class ObstBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        filname = f"./Log/discord{datetime.date.today()}.log"
        if not os.path.exists(filname):
            open(filname, 'w').close()
        handler = logging.FileHandler(filename=filname, encoding='utf-8', mode='a')
        discord.utils.setup_logging(level=logging.INFO, handler=handler)

        super().__init__(command_prefix=commands.when_mentioned_or('/'), intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('-----------------------------------------------')