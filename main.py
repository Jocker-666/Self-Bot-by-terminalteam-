import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '/', self_bot = True)
client.remove_command('help')

@client.command(
	description = "Вывод embed."
	)
async def embed(ctx, *, text):
	await ctx.send(embed = discord.Embed(description = text))


@client.command(
    aliases = ["команды", "comms", "commands", "help"],
    description = "Это сообщение."
    )
async def helpselfbot(ctx):
    comm_list = []
    for command in client.commands:
        if not command.hidden:
            comm_list.append(f"`/{command}` — {command.description}\n")
    embed = discord.Embed(
        title = f"Список команд для Selfbot by elemelkya",
        description = "".join(comm_list),
        color = ctx.author.colour)
    embed.set_footer(text = f"Вызвано пользователем {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_thumbnail(url = "https://sirarcher1.s-ul.eu/rlNVXdGf?thumb=1")
    
    await ctx.send(embed=embed)