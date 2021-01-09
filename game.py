import functions
import text
import sys
import time
import random
import os
import levels

typingspeed = 100


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

def tutorial():
	clear()
	typing("Ah, I see... This is your first time playing THE LEGEND OF TALERA!\n")
	typing("Who am I? I am THE DEVELOPER! I will guide you through your quests!\n")
	typing("Now... Who are you?\n")
	player_name = input("> ")
	typing("Hello, " + player_name + "!\n")
	typing("Since it is your first time playing, here are the rules:\n")
	time.sleep(1)
	typing("Pick the right answer.\n")
	time.sleep(1)
	typing("Here are the current levels!\n")
	text.levels()
	levelpick = ""
	while levelpick not in ["1", "2", "3", "4"]:
		levelpick = input("> ")
	if levelpick == "1":
		levels.mines()
	elif levelpick == "2":
		levels.forest()
	elif levelpick == "3":
		levels.mountains()
	elif levelpick == "4":
		levels.temple_level()
