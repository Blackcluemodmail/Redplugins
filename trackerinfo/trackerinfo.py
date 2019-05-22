from redbot.core import commands
import discord

import aiohttp

class Trackerinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    @commands.command()
    async def ptp(self, ctx):
        """gets info on PTP"""
        async with self.session.get("https://ptp.trackerstatus.info/api/status/") as r:
            data = await r.json()
        color = await ctx.embed_color()
        website = data["Website"]
        website = (f'Website is {"down" if website == "0" else "up"}')  
        irc = data["IRC"]
        irc = (f'IRC is {"down" if irc == "0" else "up"}') 
        ircannounce = data["IRCTorrentAnnouncer"]
        ircannounce = (f'IRC Announce is {"down" if ircannounce == "0" else "up"}') 
        embed = discord.Embed(title="PTP Status", url="https://ptp.trackerstatus.info", color=color)
        embed.set_image(url="https://ptp.trackerstatus.info/images/logo.png")
        embed.add_field(name="Website", value="{}".format(website))
        embed.add_field(name="IRC", value="{}".format(irc))
        embed.add_field(name="IRC Torrent Announcer", value="{}".format(ircannounce))
        
        await ctx.send(embed=embed)

    @commands.command()
    async def ggn(self, ctx):
        """gets info on GGN"""
        async with self.session.get("https://ggn.trackerstatus.info/api/status/") as r:
            data = await r.json()
        color = await ctx.embed_color()
        website = data["Website"]
        website = (f'Website is {"down" if website == "0" else "up"}')  
        irc = data["IRC"]
        irc = (f'IRC is {"down" if irc == "0" else "up"}') 
        ircannounce = data["IRCTorrentAnnouncer"]
        ircannounce = (f'IRC Announce is {"down" if ircannounce == "0" else "up"}') 
        embed = discord.Embed(title="GGN Status", url="https://ggn.trackerstatus.info", color=color)
        embed.set_image(url="https://ggn.trackerstatus.info/images/logo.png")
        embed.add_field(name="Website", value="{}".format(website))
        embed.add_field(name="IRC", value="{}".format(irc))
        embed.add_field(name="IRC Torrent Announcer", value="{}".format(ircannounce))
        
        await ctx.send(embed=embed)

    @commands.command()
    async def red(self, ctx):
        """gets info on RED"""
        async with self.session.get("https://red.trackerstatus.info/api/status/") as r:
            data = await r.json()
        color = await ctx.embed_color()
        website = data["Website"]
        website = (f'Website is {"down" if website == "0" else "up"}') 
        irc = data["IRC"]
        irc = (f'IRC is {"down" if irc == "0" else "up"}') 
        ircannounce = data["IRCTorrentAnnouncer"]
        ircannounce = (f'IRC Announce is {"down" if ircannounce == "0" else "up"}') 
        embed = discord.Embed(title="RED Status", url="https://red.trackerstatus.info", color=color)
        embed.set_image(url="https://red.trackerstatus.info/images/logo.png")
        embed.add_field(name="Website", value="{}".format(website))
        embed.add_field(name="IRC", value="{}".format(irc))
        embed.add_field(name="IRC Torrent Announcer", value="{}".format(ircannounce))
        
        await ctx.send(embed=embed)

    @commands.command()
    async def btn(self, ctx):
        """gets info on BTN"""
        async with self.session.get("https://btn.trackerstatus.info/api/status/") as r:
            data = await r.json()
        color = await ctx.embed_color()
        website = data["Website"]
        website = (f'Website is {"down" if website == "0" else "up"}') 
        irc = data["IRC"]
        irc = (f'IRC is {"down" if irc == "0" else "up"}') 
        ircannounce = data["Barney"]
        ircannounce = (f'IRC Announce is {"down" if ircannounce == "0" else "up"}') 
        embed = discord.Embed(title="BTN Status", url="https://BTN.trackerstatus.info", color=color)
        embed.set_image(url="https://btn.trackerstatus.info/images/logo.png")
        embed.add_field(name="Website", value="{}".format(website))
        embed.add_field(name="IRC", value="{}".format(irc))
        embed.add_field(name="IRC Torrent Announcer", value="{}".format(ircannounce))
        
        await ctx.send(embed=embed)

    @commands.command()
    async def mtv(self, ctx):
        """gets info on MTV"""
        async with self.session.get("https://mtv.trackerstatus.info/api/status/") as r:
            data = await r.json()
        color = await ctx.embed_color()
        website = data["Website"]
        website = (f'Website is {"down" if website == "0" else "up"}') 
        irc = data["IRC"]
        irc = (f'IRC is {"down" if irc == "0" else "up"}') 
        ircannounce = data["IRCTorrentAnnouncer"]
        ircannounce = (f'IRC Announce is {"down" if ircannounce == "0" else "up"}') 
        embed = discord.Embed(title="MTV Status", url="https://mtv.trackerstatus.info", color=color)
        embed.set_image(url="https://mtv.trackerstatus.info/images/logo.png")
        embed.add_field(name="Website", value="{}".format(website))
        embed.add_field(name="IRC", value="{}".format(irc))
        embed.add_field(name="IRC Torrent Announcer", value="{}".format(ircannounce))

        await ctx.send(embed=embed)