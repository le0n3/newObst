import discord


class ZitatLehrer(discord.ui.Modal, title='Lehrer Zitat'):
    zitat = discord.ui.TextInput(label='Dein Zitat', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            channel: discord.TextChannel = interaction.client.get_channel(953989554321371146)
            await channel.send(str(self.zitat))
            await interaction.response.send_message('Dein Zitat wurde Erfolgreich hinzugefügt!', ephemeral=True)

        except Exception as e:
            print(e)


class ZitatSchuehler(discord.ui.Modal, title='Schüler Zitat'):
    zitat = discord.ui.TextInput(label='Dein Zitat', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            channel: discord.TextChannel = interaction.client.get_channel(961508892607676416)
            await channel.send(str(self.zitat))
            await interaction.response.send_message('Dein Zitat wurde Erfolgreich hinzugefügt!', ephemeral=True)

        except Exception as e:
            print(e)


class ZitatBetrib(discord.ui.Modal, title='Betribs Zitat'):
    zitat = discord.ui.TextInput(label='Dein Zitat', style=discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        try:

            channel: discord.TextChannel = interaction.client.get_channel(994539048368611418)
            await channel.send(str(self.zitat))
            await interaction.response.send_message('Dein Zitat wurde Erfolgreich hinzugefügt!', ephemeral=True)

        except Exception as e:
            print(e)


class ZitatButtons(discord.ui.View):
    try:
        @discord.ui.button(label="Lehrer Zitat", custom_id="button-1", row=0, style=discord.ButtonStyle.primary,
                           emoji="👩‍🏫")  # the button has a custom_id set
        async def button_callback_one(self, interaction, _):
            await interaction.response.send_modal(ZitatLehrer())

        @discord.ui.button(label="Schüler Zitat", custom_id="button-2", row=0, style=discord.ButtonStyle.primary,
                           emoji="🧑‍🎓")  # the button has a custom_id set
        async def button_callback_tow(self, interaction, _):
            await interaction.response.send_modal(ZitatSchuehler())

        @discord.ui.button(label="Betriebs Zitat", custom_id="button-3", row=0, style=discord.ButtonStyle.primary,
                           emoji="🏗️")  # the button has a custom_id set
        async def button_callback_three(self, interaction, _):
            await interaction.response.send_modal(ZitatBetrib())

    except Exception as e:
        print(e)
