import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

item_benefits = {
    "Glass": "Natural resources are conserved",
    "Paper": "Carbon emissions are reduced",
    "Aluminum": "Creates jobs and contributes to the economy by developing a sector",
    "Plastic": "Enables the economical use of resources",
    "Batteries": "Prevents waste that can negatively affect human health",
    "Concrete": "Natural resources are conserved",
    "Organic waste": "Carbon emissions are reduced",
    "Electronic waste": "Creates jobs and contributes to the economy by developing a sector",
    "Iron": "Enables the economical use of resources",
    "Textiles": "Prevents waste that can negatively affect human health"
}

item_results = {
    "Glass": "Energy and water are saved",
    "Paper": "The amount of waste decreases",
    "Aluminum": "Collecting recyclable waste provides economic benefits",
    "Plastic": "Environmental pollution decreases",
    "Batteries": "Energy efficiency increases",
    "Concrete": "The amount of waste decreases",
    "Organic waste": "Energy and water are saved",
    "Electronic waste": "Provides economic benefits to those who collect recyclable waste",
    "Iron": "Environmental pollution decreases",
    "Textiles": "Energy efficiency increases"
}


@bot.event  
async def on_ready():  
    print(f'{bot.user} olarak giriş yaptık')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if not message.content.startswith('$'):
        if "on't" in message.content:
            await message.channel.send("WHAT??!!?!?")
            with open('images/johnnyvon.png', 'rb') as f:
                picture = discord.File(f)
            await message.channel.send(file=picture)
        else:
            await message.channel.send("I see that you're seeking eternal knowledge my child. Use $_commands to see what you can learn")
    await bot.process_commands(message)

@bot.command()
async def _commands(ctx):
    await ctx.send("$benefit [item_name]\n$result [item_name]\n\nItem names ->\n\nGlass\nPaper\nAluminum\nPlastic\nBatteries\nConcrete\nOrganic waste\nElectronic waste\nIron\nTextiles")

@bot.command()
async def benefit(ctx, item_name: str):
    if item_name in item_benefits:
        await ctx.send(f"The benefit of recycling {item_name} is: {item_benefits[item_name]}")
    else:
        await ctx.send("Idk this one lol try another one")
        with open('images/wise_tree.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
        return

@bot.command()
async def result(ctx, item_name: str):
    if item_name in item_results:
        await ctx.send(f"The result of recycling {item_name} is: {item_results[item_name]}")
    else:
        await ctx.send("Idk this one lol try another one")
        with open('images/wise_tree.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
        return


bot.run("eternal knowledge ends here lol")
