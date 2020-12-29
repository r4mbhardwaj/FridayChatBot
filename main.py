from Friday import bot, tasks, functionalities
Bot = bot.Bot("Friday", "Sidharth", "fridayassitance@gmail.com", "narela")
task = tasks.Tasks(Bot)
print(functionalities.Greetings())
while 1:
	Bot.ask(task, input("you: "))