import discord
import datetime
import os

client = discord.Client()

@client.event
async def on_member_join(member):

    embed = discord.Embed(colour=discord.Colour(0xffdeff), timestamp=datetime.datetime.utcnow())

    embed.set_thumbnail(url="https://orig00.deviantart.net/5bf9/f/2018/159/9/1/fidelkirbypastel_by_lahlly-dcdv76r.gif")

    embed.add_field(name="Welcome to Fidel's server!", value="Thanks for joining, {}! Remember to check out <#454831454086627328> before chatting.".format(member.mention))
    embed.add_field(name="Feel free to invite your friends using the link below!", value="━ https://discord.gg/BRkYkAT ━")

    await client.send_message(client.get_channel("454832512582287360"), embed=embed)

client.run(os.environ.get("TOKEN"))
