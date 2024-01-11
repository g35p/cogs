import discord
from redbot.core import commands

class AvatarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="avatar", aliases=["av"])
    async def avatar(self, ctx, user: discord.User = None):
        """
        Retrieves the avatar of the specified user or the user who invoked the command.
        """
        if not user:
            user = ctx.author

        avatar_url = user.avatar_url_as(size=1024)

        embed = discord.Embed(
            title=f"Avatar for {user.name}#{user.discriminator}",
            color=discord.Color.blue()
        )
        embed.set_image(url=avatar_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AvatarCog(bot))
