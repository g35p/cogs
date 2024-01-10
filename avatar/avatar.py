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

        message = ("{author} requested the avatar of {name}.").format(author=ctx.author.mention, name=bold(user.display_name))

        if user == ctx.author:
            message = ("Here is your avatar, {author}.").format(author=ctx.author.mention)
        elif user == ctx.me:
            message = ("This is _my_ avatar, {author}!").format(author=ctx.author.mention)
        elif isinstance(ctx.channel, discord.DMChannel):
            message = ("You requested the avatar of {name}.").format(name=bold(user.name))

        async with ctx.typing():
            pfp = user.avatar if isinstance(ctx.channel, discord.channel.DMChannel) else user.display_avatar
            fileExt = "gif" if pfp and pfp.is_animated() else "png"

        if pfp:
            if isinstance(ctx.channel, discord.channel.DMChannel) or ctx.channel.permissions_for(ctx.me).attach_files:
                return await ctx.send(message, file=await pfp.to_file(filename=f"pfp-{user.id}.{fileExt}"))
            elif ctx.guild and ctx.channel.permissions_for(ctx.me).embed_links:
                return await ctx.send(message + "\n" + user.display_avatar.url)

        await ctx.send(error(("I do not have permission to attach files or embed links in this channel.")), ephemeral=True)

    async def red_delete_data_for_user(self, **kwargs) -> None:
        pass
