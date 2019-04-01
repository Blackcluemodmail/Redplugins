import discord

from redbot.core import commands

old_invite = None


class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def _unload(self):
        global old_invite
        if old_invite:
            try:
                self.bot.remove_command("invite")
            except:
                pass
            self.bot.add_command(old_invite)

    @commands.command()
    async def invite(self, ctx):
        """Show's Red's invite url"""
        embed = discord.Embed(
            description="Thanks for chossing to invite {name} to your server".format(
                name=ctx.bot.user.display_name
            ),
            color=0xE78518,
        )
        embed.set_author(
            name=ctx.bot.user.name, icon_url=ctx.bot.user.avatar_url_as(static_format="png")
        )
        embed.set_thumbnail(url=ctx.bot.user.avatar_url_as(static_format="png"))
        embed.add_field(
            name="Bot Invite",
            value="https://discordapp.com/oauth2/authorize?client_id=540694922307698690&scope=bot&permissions=2146958847",
        )
        embed.add_field(name="Support Server", value="https://discord.gg/eYFxDJC")
        embed.set_footer(
            text="{name} made possible with the support of Red Discord Bot".format(
                name=ctx.bot.user.display_name
            ),
            icon_url="https://cdn.discordapp.com/icons/133049272517001216/83b39ff510bb7c3f5aeb51270af09ad3.webp",
        )
        await ctx.send(embed=embed)


def _unload(bot):
    bot.add_command("invite")


def setup(bot):
    invite = Invite(bot)
    global old_invite
    old_invite = bot.get_command("invite")
    if old_invite:
        bot.remove_command(old_invite)
    bot.add_cog(invite)
