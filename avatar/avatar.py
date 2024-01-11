import discord
from redbot.core import commands

class AvatarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, user: discord.User = None):
        """Get the avatar of a user."""
        user = user or ctx.author
        avatar_url = user.avatar_url_as(size=1024)
        await ctx.send(f"Avatar of {user.display_name}: {avatar_url}")

def setup(bot):
    bot.add_cog(AvatarCog(bot))
