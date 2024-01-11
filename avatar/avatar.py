import discord
from redbot.core import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, user: discord.User = None):
        user = user or ctx.author
        avatar_url = user.avatar_url_as(size=1024)
        await ctx.send(f"{user.mention}'s avatar: {avatar_url}")

def setup(bot):
    bot.add_cog(Avatar(bot))
