from Friday import bot, tasks

Bot = bot.Bot("Friday", "Sidharth", "")

task = tasks.Tasks(Bot)

Bot.ask(task, "Hi there, How are you")