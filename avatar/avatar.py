import discord
from redbot.core import commands
from redbot.core.utils.chat_formatting import bold, error
from typing import Optional

class Avatar(commands.Cog):
    """Get a user's avatar."""

    @commands.command(name="avatar", description="Get a user's avatar")
    async def avatar(self, ctx: commands.Context, user: discord.Member = None) -> None:
        """Returns a user's avatar as an attachment.

        The user argument can be a user mention, nickname, username, or user ID.
        Defaults to the requester when no argument is supplied."""
        user = user or ctx.author

        message = ("{author} requested the avatar of {name}.").format(author=ctx.author.mention, name=bold(user.display_name))
        if user == ctx.author:
            message = ("Here is your avatar, {author}.").format(author=ctx.author.mention)
        elif user == ctx.me:
            message = ("This is _my_ avatar, {author}!").format(author=ctx.author.mention)
        elif isinstance(ctx.channel, discord.DMChannel):
            message = ("You requested the avatar of {name}.").format(name=bold(user.display_name))

        if isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).attach_files:
            async with ctx.typing():
                pfp = user.avatar if isinstance(ctx.channel, discord.channel.DMChannel) else user.display_avatar
                file_ext = "gif" if pfp and pfp.is_animated() else "png"
            return await ctx.send(message, file=await pfp.to_file(filename=f"pfp-{user.id}.{file_ext}"))
        elif ctx.channel.permissions_for(ctx.guild.me).embed_links:
            return await ctx.send(message + "\n" + user.display_avatar.url)

        await ctx.send(error(("I do not have permission to attach files or embed links in this channel.")), ephemeral=True)

    async def red_delete_data_for_user(self, **kwargs) -> None:
        pass
