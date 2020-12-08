import random
import os
import time
import text
import game
import sys
import levels

typingspeed = 100

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

def clear():
	os.system("clear")

def mainmenu():
	text.mainmenu()
	typing("Would you like to PLAY, HELP, SEE CREDITS, or QUIT?\n")
	options = ""
	while options not in ["play", "help", "see credits", "quit"]:
		options = input("> ")
	if options == "play":
		game.tutorial()
	elif options == "help":
		help()
	elif options == "see credits":
		credits()
	elif options == "quit":
		typing("Goodbye!\n")

def help():
	clear()
	text.helptext()
	typing("\nPlease press enter to continue.\n")
	input("> ")
	clear()
	mainmenu()

def credits():
	clear()
	typing("This game was created by:")
	text.hipsterdave()
	typing("Please press enter to continue.\n")
	input("> ")
	clear()
	mainmenu()

def loding(repeat):
	x = repeat
	while x > 0:
		x = x - 1
		print(".")
		time.sleep(1)
		clear()
		print("..")
		time.sleep(1)
		clear()
		print("...")
		time.sleep(1)
		clear()

def textloding(repeat, text):
	x = repeat
	while x > 0:
		x = x - 1
		print(text + " .")
		time.sleep(1)
		clear()
		print(text + " ..")
		time.sleep(1)
		clear()
		print(text + " ...")
		time.sleep(1)
		clear()

def waitingroom_teleport():
	typing("Please press enter to continue.\n")
	input("> ")
	clear()
	levels.waiting_room()