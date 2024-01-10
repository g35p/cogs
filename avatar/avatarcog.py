import discord
from redbot.core import commands

class AvatarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def initialize(self):
        pass  # You can add any initialization logic here

    @commands.command()
    async def avatar(self, ctx, user: discord.User = None):
        """Retrieve user avatar as an attachment."""
        user = user or ctx.author
        avatar_url = user.avatar_url_as(format="png")  # You can change the format if needed
        avatar_bytes = await avatar_url.read()

        file = discord.File(avatar_bytes, filename="avatar.png")
        await ctx.send(file=file)
