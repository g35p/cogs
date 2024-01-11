import discord
from redbot.core import commands

class Avatar(commands.Cog):
    """Get user's avatar URL."""

    @commands.command()
    async def avatar(self, ctx, *, user: discord.Member=None):
        """Returns user avatar URL.

        User argument can be user mention, nickname, username, user ID.
        Defaults to yourself when no argument is supplied.
        """
        user = user or ctx.author
        url = f"{user.avatar.with_static_format('png')}"

        if url:
            message = f"{user}'s Avatar URL: {url}"
        else:
            message = f"{user} does not have a valid avatar."

        await ctx.send(message)
