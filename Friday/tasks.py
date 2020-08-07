import requests
import re
from bs4 import BeautifulSoup
import random
import numpy as np

class Tasks:
  # or make your own greetings
  greetings = np.array(['hi', 'hello', "hey there", "how are you", "what are you doing", "how is it going"])

  name = np.array(['who are you', 'your name', "call you", 'what'])

  def __init__(self, bot):
    self.bot = bot

  def task_type(self, question):
    possible_tasks = {}
    
    # possibility of greeting
    for greet in Tasks.greetings:
      if greet.lower() in question.lower():
        if 'greeting' in possible_tasks:
          possible_tasks['greeting'] = int(possible_tasks['greeting']) + 1
        else:
          possible_tasks['greeting'] = 1
    

    print(possible_tasks)

  def work(self, question):
    print(question)
    print(self.task_type(question))