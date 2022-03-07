from FridayChatBot import bot, tasks, functionalities
import sqlite3
from contextlib import closing

# database connection
connection = sqlite3.connect("friday.db")

def get_total_changes():
	return connection.total_changes

print(get_total_changes())

cursor = connection.cursor()

# create table if not exists already!
try:
	cursor.execute("CREATE TABLE User (id, first_name varchar(20), last_name varchar(20), password varchar(20))")
except Exception as e:
	print(e)
	pass
try:
	cursor.execute("CREATE TABLE Command (sentence TEXT, user TEXT, response TEXT, extra_data TEXT)")
except Exception as e:
	print(e)
	pass

def AddCommand(input_, user, response, extra_data='Null'):
	cursor.execute(f'INSERT INTO Command VALUES ("{input_}", "{user[0]}", "{response}", "{extra_data}")')
	connection.commit()

def show_commands_of(user):
	return cursor.execute(f'SELECT * FROM Command WHERE user = "{user[0]}"').fetchall()

# featching all users
users = cursor.execute("SELECT * FROM User").fetchall()
login = False
user = None

def user_register():
	first_name = input('firstname: ')
	last_name = input('lastname: ')
	password = input('password: ')
	print(cursor.execute(f'INSERT INTO User VALUES ("{(len(users)+2)**2}", "{first_name}", "{last_name}", "{password}")'))
	connection.commit()

def welcome_user(user):
	try:
		print(f'Hello {user[1]}, Welcome here!')
	except:
		pass

if not users:
	print("No Users Registered!\nRegister yourself")
	user_register()

def signup():
	global login, user
	while not login:
		users = cursor.execute("SELECT * FROM User").fetchall()
		print('Login\nselect your account or create new: ')
		for index, user in enumerate(users):
			print(index, user[1], user[2])

		next = input('choose index or register another user using("new"): ')

		if next.isdigit():
			try:
				user = users[int(next)]
			except:
				pass
		elif next.lower() == "new":
			print('ok, so create a new account!')
			user_register()
			continue

		if user:
			welcome_user(user)
			times = 3
			for a in range(times):
				password = input("password: ")
				if password == user[3]:
					login = True
					break
				elif a < times:
					print('wrong password, try again')
				else:
					print('Failed to login')

try:	
	signup()
		
	if login:
		name = user[1]
		print(f'Hello {name}, you are successfully logged in!')
		Bot = bot.Bot("Gideon", name, "fridayassitance@gmail.com", "gideon.sidtu.be")
		task = tasks.Tasks(Bot)
		print(functionalities.Greetings())

		while 1:
			if not login:
				print("you are not logged in")
				signup()
				break
			asked = input(name + '> ')
			data = Bot.ask(task, asked)
			if data:
				print(data['response'])
				AddCommand(input_=asked, user=user, response=data['response'], extra_data=data['types'])
			if 'show' and 'history' in asked:
				print('your command history:- ')
				print(show_commands_of(user))
	cursor.close()

except Exception as e:
	print(e)
	print('so, closing cursor')
	cursor.close()
