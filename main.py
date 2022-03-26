import os
import discord
from alive import keep_alive
from discord.ext import commands
import asyncio
from data import data

my_secret = os.environ['Token']
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "!", intents = intents)

@client.event
async def on_ready():
  print('{0.user}'.format(client)+' is online')

@client.command()
async def odusVerify(ctx):

  await ctx.author.send("`----------------------------------------------------`")
  await ctx.author.send("`THIS INFORMATION CHECKS IF YOU'RE IN OUR DATABASE`")
  await ctx.author.send("`Enter your College ID:`")
  
  def check(m):
    return m.author.id == ctx.author.id
    
  try:
    
    msg1 = await client.wait_for('message', check=check, timeout=60)
    if msg1:
      ID = msg1.content
      
  except asyncio.TimeoutError:
    await ctx.author.send("`Timeout, Please try again by using (!odusVerify)`")  

  try:
    if ID:
      await ctx.author.send("`Enter your Password (Same as OdusPlus):`") 
  
      msg2 = await client.wait_for("message", check=check, timeout= 60)
    if msg2:
      PASS = msg2.content
      await ctx.author.send("`Please wait until we finish searching. It will take a moment`")
      
  except asyncio.TimeoutError:
    await ctx.author.send("`Timeout. Please try again by using (!odusVerify)`")

  def dataResult():
    return data(ID,PASS)  

  placeHold = dataResult()
  
  if placeHold == False:
    await ctx.author.send("`ID or Password is incorrect. Please try again by using (!odusVerify)`")

  if placeHold == "CS":
    user = client.get_user(ctx.author.id)
    guild = client.get_guild(945281834319753236)
    member = guild.get_member(ctx.author.id)
    role = discord.utils.get(guild.roles, name='CS')
    await member.add_roles(role)
    await user.send("`CS role has been assigned to you`")

  if placeHold == "IT":
    user = client.get_user(ctx.author.id)
    guild = client.get_guild(945281834319753236)
    member = guild.get_member(ctx.author.id)
    role = discord.utils.get(guild.roles, name='IT')
    await member.add_roles(role)
    await user.send("`IT role has been assigned to you`")  
    
  if placeHold == "IS":
    user = client.get_user(ctx.author.id)
    guild = client.get_guild(945281834319753236)
    member = guild.get_member(ctx.author.id)
    role = discord.utils.get(guild.roles, name='IS')
    await member.add_roles(role)
    await user.send("`IS role has been assigned to you`")
    
    
keep_alive()
client.run(my_secret)