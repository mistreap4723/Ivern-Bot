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
    "Organic_waste": "Carbon emissions are reduced",
    "Electronic_waste": "Creates jobs and contributes to the economy by developing a sector",
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
    "Organic_waste": "Energy and water are saved",
    "Electronic_waste": "Provides economic benefits to those who collect recyclable waste",
    "Iron": "Environmental pollution decreases",
    "Textiles": "Energy efficiency increases"
}

recycling = {
    "Glass": "Rinse bottles and jars and place them in a designated glass recycling bin.",
    "Paper": "Keep paper clean and dry, flatten cardboard, and place it in paper recycling.",
    "Aluminum": "Empty and rinse cans and other accepted aluminum packaging.",
    "Plastic": "Check accepted plastic types, rinse containers, and sort according to local rules.",
    "Batteries": "Take used batteries to designated collection points or hazardous-waste facilities.",
    "Concrete": "Separate construction debris and send it to a concrete recycling facility.",
    "Organic_waste": "Compost food scraps and other accepted organic materials.",
    "Electronic_waste": "Take old electronics to authorized e-waste collection points.",
    "Iron": "Separate iron and steel scrap and deliver it to a metal recycling facility.",
    "Textiles": "Donate wearable clothes and take unwanted fabrics to textile collection points."
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
    await ctx.send("$get_help\n$how_to_recycle [item_name]\n$benefit [item_name]\n$result [item_name]\n\nItem names ->\n\nGlass\nPaper\nAluminum\nPlastic\nBatteries\nConcrete\nOrganic_waste\nElectronic_waste\nIron\nTextiles")

@bot.command()
async def get_help(ctx):
    await ctx.send("$how_to_recycle - For learning how to properly recycle each item\n$benefit - For learning how recycling an item benefits the environment\n$result - For learning what happens to the environment as a result when an item is recycled\n\nDon't forget to use the exact item name when using a command! (Ex: $how_to_recycle Organic_waste)")

@bot.command()
async def how_to_recycle(ctx, item_name: str):
    if item_name in recycling:
        await ctx.send(f"To properly recycle {item_name}: {recycling[item_name]}")
    else:
        await ctx.send("Idk this one lol try another one")
        with open('images/wise_tree.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
        return

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

bot.run("eternal knowledge ends here lol") # Replace with bot token
