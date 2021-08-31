

#importing stuffs

import discord
from discord.ext import commands


#adding prefix
bot = commands.Bot(command_prefix='-', description="This is a Helper Bot")


@bot.command() 
async def add(ctx,a:int,b:int): 
    await ctx.send(f"{a} + {b} = {a+b}") #Adds A and B

@bot.command() 
async def sub(ctx,a:int,b:int): 
    await ctx.send(f"{a} - {b} = {a-b}") #Subtracts A and B

@bot.command() 
async def multiply(ctx,a:int,b:int): 
    await ctx.send(f"{a} * {b} = {a*b}") #Multplies A and B

@bot.command() 
async def divide(ctx,a:int,b:int): 
    await ctx.send(f"{a} / {b} = {a/b}") #Divides A and B
    
bot.run(token_here)  #add the token and run  
    
