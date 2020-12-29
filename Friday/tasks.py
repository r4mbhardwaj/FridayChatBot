from .functionalities import *
import requests
import re
from bs4 import BeautifulSoup
import random
import numpy as np

class Tasks:
  # or make your own greetings
  greetings = np.array(['hi', 'hello', "hey there", "how are you", "what are you doing", "how is it going"])
  name = np.array(['who are you', 'who', 'your name', "call you", 'what', 'are you'])
  place = np.array(['where', "you live", "place", "your", "house", "home", "family"])
  feedbacks = np.array(['good', "bad", "amazing", "fantastic", "wonderful", "worst", 'better', "beautiful", 'shit', 'antique'])
  contact = np.array(['contact', 'email', 'your', 'phone', 'mobile'])
  bye = np.array(['bye', 'see you later', 'exit'])

  def __init__(self, bot):
    self.bot = bot

  def task_type(self, question):
    possible_tasks = {}
    array = np.array([{"call":"greeting", "array":Tasks.greetings}, {"call":"name", "array":Tasks.name}, {"call":"places", "array":Tasks.place}, {"call":"contact", "array":Tasks.contact}, {"call":"bye", "array":Tasks.bye}])

    def posibillities(array):
      for i in array:
        for word in i['array']:
          if word.lower() in question.lower():
            if i['call'] in possible_tasks:
              possible_tasks[i['call']] = int(possible_tasks[i['call']]) + 1
            else:
              possible_tasks[i['call']] = 1

    posibillities(array)
    return possible_tasks

  def do_tasks(self, task_types, question):
    for task in task_types:
      if task == "greeting":
        print(greetings(self.bot))
      if task == "name":
        print(MyName(self.bot))
      elif task == "places":
        print(MyPlace(self.bot))
      elif task == "contact":
        print(contact_methods(self.bot))
      elif task == "bye":
        print(bye(self.bot))
        exit()

  def work(self, question):
    task_types = Tasks.task_type(self, question)
    Tasks.do_tasks(self, task_types, question)