from os import environ

DISCORD_TOKEN: str = environ["SELF_VCDIFF_TOKEN"]
TARGET_CH_ID: int = int(environ["SELF_VCDIFF_TARGET_CH_ID"])
ICON_URL: str = "https://cdn.discordapp.com/avatars/853288717215989780/1cf1b8159cbd89884d56532522b0fcf1.png"

COOLDOWN_TIME: int = 15
