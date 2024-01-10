from .avatar_cog import AvatarCog

def setup(bot):
    bot.add_cog(AvatarCog(bot))
