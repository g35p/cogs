# __init__.py

from .avatar import Avatar

def setup(bot):
    bot.add_cog(Avatar(bot))
