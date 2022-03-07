# FridayChatBot🤖

Create your own Bot🤖 that can answer simple questions, its pretty lightweight🪶 and fast!⚡

To Install on your computer, execute this command in your terminal.🧑🏻‍💻

    pip install FridayChatBot

for testing.🧪

    from FridayChatBot import bot, tasks, functionalities
    name = "Ram"
    print(f'Hello {name}, you are successfully logged in!')
    Bot = bot.Bot("Gideon", name, gideon@sidtu.be", "gideon.sidtu.be")
    task = tasks.Tasks(Bot)
    print(functionalities.Greetings())

If this code works, you are ready to go!

## To get response for a sentence.💬
Run this command🏃🏻‍♂️

    Bot.ask(task, "<sentence>")
it will return a `dictionary` with key-value🔑  pairs of `"response":"<response of the sentence>", "types":"<it will return the functions that it ran to make the response>"`
