from typing import Dict
import datetime

import discord

from config import COOLDOWN_TIME
from src.embed.factory import embed_factory
from src.util.singleton import Singleton


class VCDiffHandler(Singleton):
    def __init__(self, client: discord.Client):
        self.client: discord.Client = client
        self.history: Dict[int: datetime.datetime] = dict()

    async def handle(
            self,
            member: discord.Member,
            before: discord.VoiceState,
            after: discord.VoiceState,
            target_ch: discord.TextChannel
    ):
        user: discord.User = self.client.get_user(member.id)

        if before.channel == after.channel:
            return

        is_join: bool = True if after.channel is not None else False

        if self.is_in_cooldown(user):
            return

        else:
            channel_name = str(after.channel) if after.channel is not None else str(before.channel)

            embed = embed_factory(member, channel_name, is_join)

            await target_ch.send(embed=embed)

    def is_in_cooldown(self, user: discord.User) -> bool:
        user_id: int = user.id

        if not(user_id in self.history):
            self.history[user_id] = datetime.datetime.now()

            return False

        else:
            now_time: datetime.datetime = datetime.datetime.now()
            time_diff: datetime.timedelta = self.history[user_id] - now_time

            if time_diff.seconds <= COOLDOWN_TIME:
                return True

            self.history[user_id] = now_time

            return False
