import os
import discord
from alive import keep_alive
from discord.ext import commands
import asyncio
from data import data

#'Token' is Discord bot's ID.
my_secret = os.environ['Token']
intents = discord.Intents.default()
intents.members = True

#This lets the bot go searching if there's exclamation mark.
client = commands.Bot(command_prefix = "!", intents = intents)

#Whenever the script is active, the bot is also online.
@client.event
async def on_ready():
  print('{0.user}'.format(client)+' is online')

#If the user types "!odusVerify", it will send a private message.
@client.command()
async def odusVerify(ctx):

  await ctx.author.send("`----------------------------------------------------`")
  await ctx.author.send("`THIS INFORMATION CHECKS IF YOU'RE IN OUR DATABASE`")
  await ctx.author.send("`Enter your College ID:`")
  
  def check(m):
    return m.author.id == ctx.author.id
  
#After the message from the bot is sent, it waits for the user input. If 60 seconds passes, it will timeout.
  try:
    
    msg1 = await client.wait_for('message', check=check, timeout=60)
    if msg1:
      ID = msg1.content
      
  except asyncio.TimeoutError:
    await ctx.author.send("`Timeout, Please try again by using (!odusVerify)`")  

#If the user enters the ID, it will send another message and wait for another input.
  try:
    if ID:
      await ctx.author.send("`Enter your Password (Same as OdusPlus):`") 
  
      msg2 = await client.wait_for("message", check=check, timeout= 60)
    if msg2:
      PASS = msg2.content
      await ctx.author.send("`Please wait until we finish searching. It will take a moment`")
      
  except asyncio.TimeoutError:
    await ctx.author.send("`Timeout. Please try again by using (!odusVerify)`")

#Once there's ID and PASS input it will run dataResult method once and the variable placeHold will hold either CS/IT/IS    
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
    
#This pings the script so it keeps running all the time.
keep_alive()
client.run(my_secret)
