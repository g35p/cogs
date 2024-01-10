class Avatar(commands.Cog):
    """Get user's avatar."""

    @commands.command()
    async def avatar(self, ctx, *, user: discord.Member=None):
        """Returns user avatar.

        User argument can be user mention, nickname, username, user ID.
        Default to yourself when no argument is supplied.
        """
        author = ctx.author

        if not user:
            user = author

        avatar = user.avatar if user.avatar else user.default_avatar

        # Get the avatar in bytes
        avatar_bytes = await avatar.read()

        # Send the avatar file directly
        await ctx.send(f"{user}'s Avatar:", file=discord.File(avatar_bytes, f"{user}_avatar{avatar.suffix}"))
