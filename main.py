from Friday import bot, tasks

Bot = bot.Bot("Friday", "Sidharth", "", "narela")

task = tasks.Tasks(Bot)

while 1:
	Bot.ask(task, input("you: "))