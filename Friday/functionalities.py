import random
import re
import datetime

def Greetings():
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour < 12:
		return 'Good Morning!'
	elif hour >= 12 and hour < 17:
		return 'Good Afternoon!'
	elif hour >= 17 and hour < 21:
		return 'Good Evening!'
	else:
		return 'Good Night!'

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

def contact_methods(bot):
	ways = [f"You can contact me using my email at {bot.email}", f"Hey {bot.user}, You can always contact me at {bot.email}"]
	return random.choice(ways)

def greetings(bot):
	ways = [f"Hey there! How are you {bot.user}", f"I am preety fine here, What about you?", f"Hello {bot.user}, I am your {bot.BotName}!", f"Your {bot.BotName} is so Good! what about you?"]
	return random.choice(ways)

def bye(bot):
	ways = [f"Ok! Bye!", f"Okay, see you later!", f"Bye, {bot.user}!"]
	return random.choice(ways)