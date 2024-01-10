# avatar.py
import discord
from redbot.core import commands

class AvatarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="avatar")
    async def get_avatar(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Please provide a valid username.")
            return

        if member not in ctx.guild.members:
            await ctx.send("Member not found on this server.")
            return

        avatar_url = member.avatar_url
        await ctx.send(f"Avatar for {member.display_name}: {avatar_url}")
