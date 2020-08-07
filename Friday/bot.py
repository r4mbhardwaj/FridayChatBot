from .tasks import *

class Bot:
  def __init__(self, BotName, user, email):
    self.BotName = BotName
    self.user = user
    self.email = email

  def ask(self, task, question):
    task.work(question)