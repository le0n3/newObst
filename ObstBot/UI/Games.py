import discord
import random as r
from ObstBot.Datenbank import SocialCreditEdit


class HIorLOWButton(discord.ui.Button['HIorLOw']):
    def __init__(self,Hi: bool, Number: int, Credits: int, User: discord.Member):

        super().__init__(style=discord.ButtonStyle.secondary, label='\u200b', row=y)
        self.isHie = Hi
        self.number = Number
        self.Credits = Credits
        self.User = User
        if self.isHie:
            self.label = "Hi"
        else:
            self.label = "Low"

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        if self.isHie:
            if self.number > 6:
                SocialCreditEdit(self.User, self.Credits)
            else:
                SocialCreditEdit(self.User, -self.Credits)
        else:
            if self.number <= 6:
                SocialCreditEdit(self.User, self.Credits)
            else:
                SocialCreditEdit(self.User, -self.Credits)





class HiorLow(discord.ui.View):
    def __init__(self, Credits : int, User : discord.Member):
        super().__init__()
        number: int = r.randint(0,12)

        self.add_item(HIorLOWButton(True, number,Credits, User))
        self.add_item(HIorLOWButton(False, number, Credits, User))
