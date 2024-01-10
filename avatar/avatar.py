# Simple avatar URL fetch by Yukirin#0048

# Discord
import discord
import asyncio  # Import asyncio for sleep function

# Red
from redbot.core import commands


class Avatar(commands.Cog):
    """Get user's avatar URL."""

    @commands.command()
    async def avatar(self, ctx, *, user: discord.Member=None):
        """Returns user avatar URL.

        User argument can be user mention, nickname, username, user ID.
        Default to yourself when no argument is supplied.
        """
        author = ctx.author

        if not user:
            user = author

        url = user.avatar.with_static_format("png")
        message = await ctx.send(f"{user}'s Avatar URL : {url}")

        # Sleep for 10 seconds, adjust as needed
        await asyncio.sleep(1)

        # Delete the message after 10 seconds
        await message.delete()
