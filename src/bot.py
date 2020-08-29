import os
import discord
from discord.ext import commands
from cogs.greetings import Greetings
from cogs.calculus import Calculus

bot = commands.Bot(command_prefix='!')
bot.add_cog(Greetings(bot))
bot.add_cog(Calculus(bot))


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('with your mum, panda panda! 🐼'))
    print('Logged on as {0}!'.format(bot.user))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments!! @.@')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used!! >.<')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('You don\'t got the power!! :D')
    else:
        await ctx.send('Somethang wong? :<')


@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(bot.latency * 1000)}ms')


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

if __name__ == '__main__':
    token = os.getenv('TOKEN')
    if token:
        bot.run(token)
    else:
        with open('bot_token.txt') as bot_token_file:
            token = bot_token_file.readline()
            bot.run(token)
