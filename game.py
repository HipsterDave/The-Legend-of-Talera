import functions
import text
import sys
import time
import random
import os
import levels
import pickle
import city


typingspeed = 100

class Data():
	def __init__(self):
		self.coins = 0
		self.rustic_coins = 0
		self.gems = 0
		self.tuna = 0
		self.salmon = 0
		self.cod = 0
		self.clownfish = 0
		self.hat = "N/A"
		self.shirt = "Hand-me-down shirt from your older neanderthal brother"
		self.pants = "Torn Jeans"
		self.shoes = "N/A (Looks like you're a hobbit)"
		self.outerwear = "N/A"
		self.item = 0
		self.trophies = []
	

data = Data()

def clear():
	if sys.platform.startswith("linux"):
		os.system("clear")
	elif sys.platform.startswith("win32"):
		os.system("cls")
	elif sys.platform.startswith("darwin"):
		os.system("clear")

def typing(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/typingspeed)

def settype(text, typing_speed):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/typing_speed)

def login_or_signup():
	clear()
	print("1) Login")
	print("2) Signup")
	login_or_signup = ""
	while login_or_signup not in ["1", "2"]:
		login_or_signup = input("> ")
	if login_or_signup == "1":
		login()
	elif login_or_signup == "2":
		signup()

def login():
	clear()
	global file
	global data
	print("Please enter your login information.")
	username = input("Username: ")
	password = input("Password: ")
	file = "{}_{}.pickle".format(username, password)
	if os.path.exists(file):
		data = load()
		comeback()
	else:
		typing("This account doesn't seem to exist...\n")
		time.sleep(2)
		login_or_signup()

def signup():
	clear()
	global username, password, file
	print("Ah! A new player! Please enter your new username and password.")
	username = input("Username: ")
	password = input("Password: ")
	file = "{}_{}.pickle".format(username, password)
	if os.path.exists(file):
		typing("Hmm... This account already exists.\n")
		typing("Try using a different username or password.\n")
		time.sleep(2)
		login_or_signup()
	tutorial()

def save():
	global data
	if os.path.exists(file):
		os.remove(file)
	with open(file, 'wb') as f:
		pickle.dump(data, f)

def load():
	with open(file, 'rb') as f:
		data = pickle.load(f)
		return data
	print("Couldn't load saved file!")
	return Data()

def comeback():
	clear()
	save()
	typing("Ah, welcome back, adventurer!\n")
	typing("Would you like to go to the city, start another quest, or take a break and leave the game?\n")
	text.city_or_quest()
	city_or_quest = ""
	while city_or_quest not in ["1", "2", "3"]:
		city_or_quest = input("> ")
	if city_or_quest == "1":
		clear()
		typing("Ok! You want to go to the city!\n")
		time.sleep(2)
		city.city_teleport()
	elif city_or_quest == "2":
		clear()
		text.levels()
		levelpick = ""
		while levelpick not in ["1", "2", "3", "4", "1000"]:
			levelpick = input("> ")
		if levelpick == "1":
			levels.mines()
		elif levelpick == "2":
			levels.forest()
		elif levelpick == "3":
			levels.mountains()
		elif levelpick == "4":
			levels.temple_level()
		elif levelpick == "1000":
			levels.test()
	elif city_or_quest == "3":
		typing("Are you sure you want to leave? You will lose all of your progress. (y/n)\n")
		exit_confirm = ""
		while exit_confirm not in ["y", "n"]:
			exit_confirm = input("> ")
		if exit_confirm == "y":
			typing("Okay, then. See you next time!\n")
			exit()
		elif exit_confirm == "n":
			typing("Okay.\n")
			functions.waitingroom_teleport()

def tutorial():
	clear()
	save()
	typing("So... This is your first time playing THE LEGEND OF TALERA!\n")
	typing("Who am I? I am THE DEVELOPER! I will guide you through your quests!\n")
	typing("Since it is your first time playing, here are the rules:\n")
	time.sleep(1)
	typing("Pick the right answer.\n")
	time.sleep(1)
	typing("Now, let's pick a level for you to choose!\n")
	text.levels()
	levelpick = ""
	while levelpick not in ["1", "2", "3", "4", "1000"]:
		levelpick = input("> ")
	if levelpick == "1":
		levels.mines()
	elif levelpick == "2":
		levels.forest()
	elif levelpick == "3":
		levels.mountains()
	elif levelpick == "4":
		levels.temple_level()
	elif levelpick == "1000":
		levels.test()
