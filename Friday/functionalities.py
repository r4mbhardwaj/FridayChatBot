import random
import re
import datetime

# def Greetings(question):
# 	hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour < 12:
#         return 'Good Morning!'

#     elif hour >= 12 and hour < 17:
#         return 'Good Afternoon!'

#     elif hour >= 17 and hour < 21:
#         return 'Good Evening!'

#     else:
#         return 'Good Night!'

def MyName(bot):
	'''
	bot is an object of class Bot in bot.py
	'''
	ways = [f"Hi {bot.user}, My Name is {bot.BotName}!", f"I am {bot.BotName}", f"You can call me {bot.BotName}", f"I am your faviourate Bot {bot.BotName}"]
	return random.choice(ways)

def MyPlace(bot):
	'''
	bot is an object of class Bot in bot.py
	'''
	ways = [f"I live in {bot.address}", f"I am from {bot.address}, what about you?", f"I am a citizen from {bot.address}, where are you from?", f"I live in {bot.address}, {bot.user} what 'bout ya?"]
	return random.choice(ways)
