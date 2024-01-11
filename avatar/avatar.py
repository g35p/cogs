# Discord
import discord

# Red
from redbot.core import commands

class Avatar(commands.Cog):
    """Get user's avatar URL."""

    @commands.command()
    async def avatar(self, ctx, user: discord.Member=None):
        """
        Returns user avatar URL.

        :param ctx: The command context.
        :param user: The user whose avatar URL is to be fetched.
                     Defaults to the author if not specified.
        :type user: discord.Member
        """
        author = ctx.author

        try:
            if not user:
                user = author

            url = user.avatar.with_static_format("png")

            await ctx.send(f"{user}'s Avatar URL: {url}")

        except discord.errors.NotFound:
            await ctx.send("User not found.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
