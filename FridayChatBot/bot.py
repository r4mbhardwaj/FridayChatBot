from .tasks import *

class Bot:
  def __init__(self, BotName, user, email, address):
    self.BotName = BotName
    self.user = user
    self.email = email
    self.address = address
    

  def ask(self, task, question):
    return task.work(question)