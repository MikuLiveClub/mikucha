import discord

from config import ICON_URL


def embed_factory(member: discord.Member, channel_name: str, is_join: bool) -> discord.Embed:
    if is_join:
        return get_in_embed(member, channel_name)
    else:
        return get_out_embed(member, channel_name)


def make_base_embed(member_icon_url: str) -> discord.Embed:
    embed = discord.Embed(color=0x1e63e9)
    embed.set_author(name="ミクちゃ", icon_url=ICON_URL)
    embed.set_thumbnail(url=member_icon_url)

    return embed


def get_in_embed(member: discord.Member, channel_name: str) -> discord.Embed:
    member_icon_url = get_user_icon_url(member)

    embed = make_base_embed(member_icon_url)
    embed.title = "{}が{}に入りました".format(member.display_name, channel_name)
    embed.description = "楽しんでいってくださいね♪"

    return embed


def get_out_embed(member: discord.Member, channel_name: str) -> discord.Embed:
    member_icon_url = get_user_icon_url(member)

    embed = make_base_embed(member_icon_url)
    embed.title = "{}が{}から抜けました".format(member.display_name, channel_name)
    embed.description = "また遊びに来てくださいね♪"

    return embed


def get_user_icon_url(member: discord.Member) -> str:
    return "https://cdn.discordapp.com/avatars/{}/{}.png".format(member.id, member.avatar)
