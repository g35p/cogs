import discord
from redbot.core import commands

class AvatarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="avatar", aliases=["av"])
    async def get_avatar(self, ctx, user: discord.User = None):
        """Get the avatar of a user."""
        if user is None:
            user = ctx.author

        avatar_url = user.avatar_url
        await ctx.send(f"Avatar of {user.name}: {avatar_url}")

def setup(bot):
    bot.add_cog(AvatarCog(bot))
