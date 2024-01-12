import discord
from discord.ext import commands
import logging

class ObstBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        discord.utils.setup_logging(level=logging.INFO)

        super().__init__(command_prefix=commands.when_mentioned_or('/'), intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('-----------------------------------------------')