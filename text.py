import time
import random
import sys

typingspeed = 100

def typing(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.05)

def settype(text, typing_speed):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/typing_speed)

def mainmenu():
	print('''
_________          _______    _        _______  _______  _______  _        ______     _______  _______   _________ _______  _        _______  _______  _______ 
\__   __/|\     /|(  ____ \  ( \      (  ____ \(  ____ \(  ____ \( (    /|(  __  \   (  ___  )(  ____ \  \__   __/(  ___  )( \      (  ____ \(  ____ )(  ___  )
   ) (   | )   ( || (    \/  | (      | (    \/| (    \/| (    \/|  \  ( || (  \  )  | (   ) || (    \/     ) (   | (   ) || (      | (    \/| (    )|| (   ) |
   | |   | (___) || (__      | |      | (__    | |      | (__    |   \ | || |   ) |  | |   | || (__         | |   | (___) || |      | (__    | (____)|| (___) |
   | |   |  ___  ||  __)     | |      |  __)   | | ____ |  __)   | (\ \) || |   | |  | |   | ||  __)        | |   |  ___  || |      |  __)   |     __)|  ___  |
   | |   | (   ) || (        | |      | (      | | \_  )| (      | | \   || |   ) |  | |   | || (           | |   | (   ) || |      | (      | (\ (   | (   ) |
   | |   | )   ( || (____/\  | (____/\| (____/\| (___) || (____/\| )  \  || (__/  )  | (___) || )           | |   | )   ( || (____/\| (____/\| ) \ \__| )   ( |
   )_(   |/     \|(_______/  (_______/(_______/(_______)(_______/|/    )_)(______/   (_______)|/            )_(   |/     \|(_______/(_______/|/   \__/|/     \|
                                                                                                                                                               
''')

def youlost():
	print('''
          _______             _        _______  _______ _________
|\     /|(  ___  )|\     /|  ( \      (  ___  )(  ____ \\__   __/
( \   / )| (   ) || )   ( |  | (      | (   ) || (    \/   ) (   
 \ (_) / | |   | || |   | |  | |      | |   | || (_____    | |   
  \   /  | |   | || |   | |  | |      | |   | |(_____  )   | |   
   ) (   | |   | || |   | |  | |      | |   | |      ) |   | |   
   | |   | (___) || (___) |  | (____/\| (___) |/\____) |   | |   
   \_/   (_______)(_______)  (_______/(_______)\_______)   )_(   
                                                                 
''')

def youwon():
	print('''
          _______                      _______  _       
|\     /|(  ___  )|\     /|  |\     /|(  ___  )( (    /|
( \   / )| (   ) || )   ( |  | )   ( || (   ) ||  \  ( |
 \ (_) / | |   | || |   | |  | | _ | || |   | ||   \ | |
  \   /  | |   | || |   | |  | |( )| || |   | || (\ \) |
   ) (   | |   | || |   | |  | || || || |   | || | \   |
   | |   | (___) || (___) |  | () () || (___) || )  \  |
   \_/   (_______)(_______)  (_______)(_______)|/    )_)
                                                        
''')

def hipsterdave():
	print('''
 __ __  ____  ____    _____ ______    ___  ____   ___     ____  __ __    ___ 
|  |  ||    ||    \  / ___/|      |  /  _]|    \ |   \   /    ||  |  |  /  _]
|  |  | |  | |  o  )(   \_ |      | /  [_ |  D  )|    \ |  o  ||  |  | /  [_ 
|  _  | |  | |   _/  \__  ||_|  |_||    _]|    / |  D  ||     ||  |  ||    _]
|  |  | |  | |  |    /  \ |  |  |  |   [_ |    \ |     ||  _  ||  :  ||   [_ 
|  |  | |  | |  |    \    |  |  |  |     ||  .  \|     ||  |  | \   / |     |
|__|__||____||__|     \___|  |__|  |_____||__|\_||_____||__|__|  \_/  |_____|
                                                                                                                                                                                                                                           
''')

def levels():
	print('''Here are your options:
1) The Mines
2) The Forest (UNDER CONSTRUCTION NOT FINISHED)
2) The Mounatins (UNDER CONSTRUCTION NOT FINISHED)''')

def mine_entrance():
	print('''Here are your options:
1) Try and convince the worker to let you in
2) Try to sneak in''')

def policeoptions():
	print('''Here are your options:
1) Run away
2) Try and negotiate
3) Hide
4) Fight''')

def helptext():
	typing('''First and foremost, welcome to THE LEGEND OF TALERA! In this game, you will go to different places to grab artifacts.

In this game, you will be given 4 levels, knowledge, charisma, speed, and strength.
1 is the lowest, and 10 is the highest. Your results will be based on these levels.

You will also be given numbered choices, but even 
those will be based on your 4 levels.

Happy playing!\n''')

def rubysteal():
	print('''Here are your options:
1) Break the glass with a stone
2) Slowly lift up the glass
3) Admire the ruby''')

def rockmonster():
	print('''Here are your options:
1) Fight
2) Run''')

def avalanche():
	print('''Here are your options:
1) Run
2) Find a safe place to hide
3) Shield yourself with the ruby''')

def weapon_forest():
	print('''Here are your options:
1) Sword
2) Bow
3) Mace''')

def forestsign():
	typing('''Welcome to THE FOREST!''')

def city_or_quest():
	print('''Here are your options:
1) Go to the city
2) Start another quest''')

def mountain_range_mountains():
	typing("Here are your options:\n1) Talera Mountain (The tallest mountain in Talera)\n2) The Widest Mountain\n3) A pile of dirt right next to you (The smallest mountain in Talera)\n")
