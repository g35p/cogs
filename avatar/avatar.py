# Discord
import discord
from discord import File

# Red
from redbot.core import commands

class Avatar(commands.Cog):
    """Get user's avatar and send it as an attachment."""

    @commands.command()
    async def avatar(self, ctx, user: discord.Member=None):
        """
        Sends user avatar as an attachment.

        :param ctx: The command context.
        :param user: The user whose avatar is to be sent.
                     Defaults to the author if not specified.
        :type user: discord.Member
        """
        author = ctx.author

        try:
            if not user:
                user = author

            avatar_url = user.avatar.with_static_format("png")
            avatar_data = await avatar_url.read()

            avatar_file = File(avatar_data, filename="avatar.png")
            await ctx.send(f"{user}'s Avatar:", file=avatar_file)

        except discord.errors.NotFound:
            await ctx.send("User not found.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
