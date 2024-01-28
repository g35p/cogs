import asyncio
import json
import sys
from random import choice
from typing import List, Optional, Union

import aiohttp
import discord
from redbot.core import Config, commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import bold, box, inline

from .constants import (
    GOOD_EXTENSIONS,
    IMGUR_LINKS,
    MARTINE_API_BASE_URL,
    NOT_EMBED_DOMAINS,
    REDDIT_BASEURL,
    emoji,
)

# Removed translation-related imports and instantiation
# from redbot.core.i18n import Translator, cog_i18n
# _ = Translator("Nsfw", __file__)

# Removed translation decorator
# @cog_i18n(_)
class Core(commands.Cog):

    __author__ = ["Predä", "aikaterna"]
    __version__ = "2.3.99"

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        return

    def __init__(self, bot: Red):
        self.bot = bot
        self.session = aiohttp.ClientSession(
            headers={
                "User-Agent": (
                    f"Red-DiscordBot PredaCogs-Nsfw/{self.__version__} "
                    f"(Python/{'.'.join(map(str, sys.version_info[:3]))} aiohttp/{aiohttp.__version__})"
                )
            }
        )
        self.config = Config.get_conf(self, identifier=512227974893010954, force_registration=True)
        self.config.register_global(use_reddit_api=False)

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    # Removed translation decorator
    # def format_help_for_context(self, ctx: commands.Context) -> str:
    #    """Thanks Sinbad!"""
    #    pre_processed = super().format_help_for_context(ctx)
    #    return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    async def _get_imgs(self, subs: List[str] = None):
        """Get images from Reddit API."""
        # Removed _("...") from the code

    async def _get_others_imgs(self, ctx: commands.Context, url: str = None):
        """Get images from all other images APIs."""
        # Removed _("...") from the code

    async def _api_errors_msg(self, ctx: commands.Context, error_code: int = None):
        """Error message when API calls fail."""
        return await ctx.send(
            "Error when trying to contact image service, please try again later. (Code: {})".format(inline(str(error_code)))
        )

    async def _version_msg(self, ctx: commands.Context, version: str, authors: List[str]):
        """Cog version message."""
        msg = box(
            "Nsfw cog version: {version}\nAuthors: {authors}".format(
                version=version, authors=", ".join(authors)
            ),
            lang="py",
        )
        return await ctx.send(msg)

    # Removed _("...") from the code

    # Removed _("...") from the code

    # Removed _("...") from the code

    # Removed _("...") from the code

    # Removed _("...") from the code

    @staticmethod
    async def _embed(
        color: Union[int, discord.Color] = None,
        title: str = None,
        description: str = None,
        image: str = None,
        footer: Optional[str] = None,
    ):
        em = discord.Embed(color=color, title=title, description=description)
        em.set_image(url=image)
        if footer:
            em.set_footer(text=footer)
        return em
