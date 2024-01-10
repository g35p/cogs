from .avatarcog import AvatarCog

async def setup(bot):
    cog = AvatarCog(bot)
    bot.add_cog(cog)
    await cog.initialize()
