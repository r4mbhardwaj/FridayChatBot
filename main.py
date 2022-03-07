from FridayChatBot import bot, tasks, functionalities

name = input('Your name: ')
print(f'Hello {name}, you are successfully logged in!')
Bot = bot.Bot("Gideon", name, "fridayassitance@gmail.com", "gideon.sidtu.be")
task = tasks.Tasks(Bot)
print(functionalities.Greetings())

while 1:
    asked = input(name + '> ')
    data = Bot.ask(task, asked)
    if data:
        print(data['response'])