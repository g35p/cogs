# __init__.py
from .avatar import AvatarCog

def setup(bot):
    bot.add_cog(AvatarCog(bot))
