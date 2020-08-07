from Friday import bot, tasks

Bot = bot.Bot("Friday", "Sidharth", "", "narela")

task = tasks.Tasks(Bot)

Bot.ask(task, "Hi there, How are you, what is your name??? tell me your name")