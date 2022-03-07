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
    data = []
    for task in task_types:
      if task == "greeting":
        data.append(greetings(self.bot))
      if task == "name":
        data.append(MyName(self.bot))
      elif task == "places":
        data.append(MyPlace(self.bot))
      elif task == "contact":
        data.append(contact_methods(self.bot))
      elif task == "bye":
        print(bye(self.bot))
        exit()
    if type(data) != str:
      return '. '.join(data)

  def work(self, question):
    data = []
    task_types = Tasks.task_type(self, question)
    tasks_data = Tasks.do_tasks(self, task_types, question)
    if type(tasks_data) != str:
      data.extend(tasks_data)
    else:
      data.append(tasks_data)
    if type(data) != str:
        joined_data = '. '.join(data)
    else:
        joined_data = data
    return {'response':joined_data, 'types':task_types}