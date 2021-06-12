from typing import Optional

import discord

from config import DISCORD_TOKEN, TARGET_CH_ID
from src.handler.vc import VCDiffHandler
from src.util.singleton import Singleton


class Client(discord.Client, Singleton):
    def __init__(self):
        intents = discord.Intents.all()
        intents.members = True
        super(Client, self).__init__(presences=True, guild_subscriptions=True, intents=intents)

        discord_client: discord.Client = super(Client, self)
        self.vc_handler: VCDiffHandler = VCDiffHandler(discord_client)

        self.target_ch: Optional[discord.TextChannel] = None

    def launch(self):
        self.run(DISCORD_TOKEN)

    async def on_ready(self):
        self.target_ch = self.get_channel(TARGET_CH_ID)

    async def on_message(self, message: discord.Message):
        pass

    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if member.bot or before.channel == after.channel:
            return

        await self.vc_handler.handle(member, before, after, self.target_ch)
