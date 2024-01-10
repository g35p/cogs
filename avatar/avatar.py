import discord
from redbot.core import app_commands, commands
from redbot.core.utils.chat_formatting import bold, error
from typing import Optional

class Avatar(commands.Cog):
    """Get a user's avatar."""

    @commands.command(name="avatar", description="Get a user's avatar")
    @app_commands.guild_only()
    async def avatar(self, ctx: commands.Context, user: discord.Member = None) -> None:
        """Returns a user's avatar as an attachment.

        User argument can be user mention, nickname, username, user ID.

        Defaults to the requester when no argument is supplied."""
        if user is None:
            user = ctx.author

        message = f"{ctx.author.mention} requested the avatar of {bold(user.display_name)}."

        if user == ctx.author:
            message = f"Here is your avatar, {ctx.author.mention}."
        elif user == ctx.me:
            message = f"This is _my_ avatar, {ctx.author.mention}!"
        elif isinstance(ctx.channel, discord.DMChannel):
            message = f"You requested the avatar of {bold(user.name)}."

        async with ctx.typing():
            pfp = user.avatar if isinstance(ctx.channel, discord.channel.DMChannel) else user.display_avatar
            file_ext = "gif" if pfp and pfp.is_animated() else "png"

            if pfp:
                await ctx.send(message, file=await pfp.to_file(filename=f"pfp-{user.id}.{file_ext}"))
            else:
                embed = discord.Embed(description=message)
                embed.set_image(url=user.display_avatar.url)
                await ctx.send(embed=embed)

    async def red_delete_data_for_user(self, **kwargs) -> None:
        pass
