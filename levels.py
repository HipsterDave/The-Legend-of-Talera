import functions
import text
import sys
import time
import random
import os
import game
import city

# name = game.user_name

def waiting_room():
	typing("Ah, welcome back!\n")
	#guides = ["Alice", "Jerry", "Brian", "Rachel", "Pepe", "Steve", "Hipster Dave", "Vadercat", "Albert", "Alfred", "Bruce", "Alfredo", "Phil", "Macy", "Santa", "The Easter Bunny", "The Thanksgiving Turkey", "Tammie", "Clyde", "Chris", "Joy", "Joe", "Benny", "Wolf", "Don", "Mr. Lemon", "Andrew", "Stephanie", "Michelle", "Laura", "Carl", "Harriet", "Danny", "Joey", "Jessie", "Becky", "Nicky", "Alex", "Frank", "Rich", "Dana", "Lily", "Sabrina", "Hilda", "Zelda", "Salem", "Amanda", "Harvey", "Mark", "Waldo", "Stefan", "Weasel", "Eddie", "Judy", "Myra", "Kimmy", "D.J.", "Fernando", "Jimmy", "John", "Mike", "Meatball Sub", "Mr. Subway", "Greg", "Netherite", "Enderman", "George,", "Adam", "Thomas", "Abraham", "Lincoln", "Denzel", "Zachary", "Garfield", "Peter", "Paige", "Andy", "Monty", "Roomba", "Arnold", "Terry", "Simon", "Mel", "Howie", "Heidi", "Frances", "Tommy", "Donald", "Kevin", "Harry", "Marv", "Fuller", "Buzz", "Buddy", "Narwahl", "Rudolph", "Michael", "Tiger", "Metta", "Tiki", "Lewis", "Clark", "Sacajawea", "Reginald", "Jacques", "Augustus", "Charlie", "A person with a very long name and this is it so yes this is his name and you should like it and if you don't deal with it and oh no i am running out of things to say so i will put in a bunch of filler words to make this longer and whoever came up with this name is the greatest person on earth no wait the galaxy actually the universe wow this name is very long but i am proud of it well i am running out of space so goodbye wait did i mention that i can count to 10 do you want to hear it ok you do 1 2 3 4 5 6 7 8 9 9 10 oh no i did it wrong i need to restart but it will take a long time 1   2   3   4   5   6   7   8   9   10 yay i am now done wow that was some superb counting ok goodbye for real oh just one more thing i will miss you a lot bye bye"]
	#randomguide = random.choice(guides)
	#typing("Welcome to Talera waiting room! Today, " + randomguide + " will be your guide.\n")
	#typing(randomguide + " - Let's see what trophies you currently have.\n")
	#if trophies == []:
		#typing("Hmm... seems like you do not have any trophies.\n")
	#else:
		#typing("Your trophies are:\n")
		#for t in trophies:
			#typing(t + "\n")
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
			mines()
		elif levelpick == "2":
			forest()
		elif levelpick == "3":
			mountains()
		elif levelpick == "4":
			temple_level()
		elif levelpick == "1000":
			test()
	elif city_or_quest == "3":
		clear()
		typing("Are you sure you want to leave? (y/n)\n")
		exit_confirm = ""
		while exit_confirm not in ["y", "n"]:
			exit_confirm = input("> ")
		if exit_confirm == "y":
			typing("Okay, then. See you next time!\n")
			exit()
		elif exit_confirm == "n":
			typing("Okay.\n")
			functions.waitingroom_teleport()

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

def mines():
	clear()
	typing("Before we travel to THE MINES, we need to set your levels.\n")
	time.sleep(1)
	clear()
	global speed
	global charisma
	global strength
	global knowledge
	functions.textloading(3, "Rolling Dice")
	levelnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	knowledge = random.choice(levelnumbers)
	strength = random.choice(levelnumbers)
	charisma = random.choice(levelnumbers)
	speed = random.choice(levelnumbers)
	typing("Your knowledge level is " + str(knowledge) + ".\n")
	typing("Your strength level is " + str(strength) + ".\n")
	typing("Your charisma level is " + str(charisma) + ".\n")
	typing("Your speed level is " + str(speed) + ".\n")
	averageleveladd = knowledge + strength + charisma + speed
	averageleveldivide = averageleveladd/4
	typing("Your average level is " + str(averageleveldivide) + ".\n")
	typing("Please press enter to continue.\n")
	input("> ")
	clear()
	functions.textloading(3, "Traveling to THE MINES")
	typing("Welcome to THE MINES! Today, your goal is the get the famous TALERA RUBY.\n")
	typing("You will need to get past rock monsters and big avalanches.\n")
	typing("Let's begin!\n")
	typing("As you walk to the entrance of the mine, you realize that your mine pass has expired. You are not allowed to go in the mines without one.\n")
	typing("You do have the chance to convince the worker to let you in. You need a charisma level above 3 to do that.\n")
	typing("You can also try to sneak in. If it goes wrong, you will spend the rest of your life in prison.\n")
	text.mine_entrance()
	entrance = ""
	while entrance not in ("1", "2"):
		entrance = input("> ")
	if entrance == "1":
		clear()
		if charisma >= 4:
			typing("You sucessfully convinced the worker to let you in.\n")
			mines_again()
		else:
			typing("You were unable to convince the worker to let you in. You walk away in defeat.\n")
			game.save()
			text.youlost()
			functions.waitingroom_teleport()
	elif entrance == "2":
		clear()
		typing("You attempt to sneak in.\n")
		typing("Right as you sneak in to the mine, a police officer sees you.\n")
		typing("Quick! We need to do something!\n")
		text.policeoptions()
		police_options = ""
		while police_options not in ["1", "2", "3", "4"]:
			police_options = input("> ")
		if police_options == "1":
			clear()
			typing("You attempt to run away.\n")
			if speed >= 5:
				typing("Since you have a speed level of over 4, you are pretty fast. The policeman is no match for you.\n")
				mines_again()
			else:
				typing("You have a speed level under 4. You are so slow! The policeman catches you, and you get put in jail forever.\n")
				game.save()
				text.youlost()
				functions.waitingroom_teleport()
		if police_options == "2":
			clear()
			typing("You attempt to negotiate.\n")
			typing("You REALLY think you are going to get away with this? I THINK NOT!\n")
			game.save()
			text.youlost()
			functions.waitingroom_teleport()
		if police_options == "3":
			clear()
			typing("You attempt to hide.\n")
			if knowledge >= 4:
				typing("Since you have a knowledge level of over 3, you at least know a good place to hide.\n")
				mines_again()
			else:
				typing("You have a knowledge level under 3.\n")
				typing("You are pretty dumb, because you for some reason you hid behind the police officer.\n")
				game.save()
				text.youlost()
				functions.waitingroom_teleport()
		if police_options == "4":
			clear()
			typing("You attempt to fight.\n")
			if strength >= 5:
				typing("Since you have a strength level over 4, you are pretty strong. That police man was no match for you.\n")
				mines_again()
			else:
				typing("Why do you even try? You arms are like floppy noodles!\n")
				game.save()
				text.youlost()
				functions.waitingroom_teleport()

def mines_again():
	typing("As you walk through the mine, you see green gems, yellow gems, blue gems, but no TALERA RUBY.\n")
	typing("Then, you see a giant glimmering ruby sitting in a glass cage.\n")
	text.rubysteal()
	glass = ""
	while glass not in ["1", "2", "3"]:
		glass = input("> ")
	if glass == "1":
		clear()
		typing("You attempt to break the glass with a stone.\n")
		typing("BEEP BEEP BEEP! An alarm sounds and a rock monster comes out of the cave.\n")
		text.rockmonster()
		rockmonster = ""
		while rockmonster not in ["1", "2"]:
			rockmonster = input("> ")
		if rockmonster == "1":
			clear()
			typing("You attempt to fight the rock monster.\n")
			if strength >= 7:
				typing("WOW! You have a strength level of over 6! You successfully defeated the rock monster!\n")
				typing("You obtain the TALERA RUBY!\n")
				typing("As you run for the exit of the mine, an AVALANCHE starts!\n")
				text.avalanche()
				avalanche = ""
				while avalanche not in ["1", "2", "3"]:
					avalanche = input("> ")
				if avalanche == "1":
					clear()
					typing("You attempt to run.\n")
					if speed == 10:
						typing("WHAT??? You have a speed level of 10! You successfully made it out of the cave.\n")
						if "Talera Ruby" not in game.data.trophies:
							game.data.trophies.append("Talera Ruby")
							typing("You obtained the TALERA RUBY!\n")
							typing("You have also earned 20 coins!\n")
							game.data.coins = game.data.coins + 20
							game.save()
							text.youwon()
							if "Shattered Ruby Pieces" not in game.data.trophies:
								typing("You may have won, but you can also get the shattered ruby pieces.\n")
							functions.waitingroom_teleport()
						else:
							typing("Seems like you already have the TALERA RUBY inside your trophy room...\n")
							typing("You still have earned 10 coins!\n")
							game.data.coins = game.data.coins + 10
							game.save()
							text.youwon()
							functions.waitingroom_teleport()
					else:
						typing("The avalanche was too fast...\n")
						game.save()
						text.youlost()
						functions.waitingroom_teleport()
				elif avalanche == "2":
					clear()
					typing("You attempt to find a safe place to hide.\n")
					typing("You find a big rock to hide under.\n")
					typing("The avalanche ends.\n")
					if "Talera Ruby" not in game.data.trophies:
						game.data.trophies.append("Talera Ruby")
						typing("You obtained the TALERA RUBY!\n")
						typing("You have also earned 20 coins!\n")
						game.data.coins = game.data.coins + 20
						game.save()
						text.youwon()
						if "Shattered Ruby Pieces" not in game.data.trophies:
							typing("You may have won, but you can also get the shattered ruby pieces.\n")
							
						functions.waitingroom_teleport()
					else:
						typing("Seems like you already have the TALERA RUBY inside your trophy room...\n")
						typing("You still have earned 10 coins!\n")
						game.data.coins = game.data.coins + 10
						game.save()
						functions.waitingroom_teleport()
				elif avalanche == "3":
					clear()
					typing("You attempt to shield yourself with the ruby.\n")
					typing("As the rocks fall on the ruby, it shatters to pieces.\n")
					typing("Still, you have made it out of the mines.\n")
					if "Shattered Ruby Pieces" not in game.data.trophies:
						game.data.trophies.append("Shattered Ruby Pieces")
						typing("You obtained the SHATTERED RUBY PIECES!\n")
						typing("You have also earned 15 coins!\n")
						game.data.coins = game.data.coins + 15
						game.save()
						text.youwon()
						if "Talera Ruby" not in game.data.trophies:
							typing("You may have won, but you can still get the full ruby.\n")
						functions.waitingroom_teleport()
					else:
						typing("Seems like you already have the SHATTERED RUBY PIECES inside your trophy room...\n")
						typing("You still have earned 8 coins!\n")
						game.data.coins = game.data.coins + 8
						game.save()
						functions.waitingroom_teleport()
		elif rockmonster == "2":
			clear()
			typing("You ran away from the monster, but you forgot one key item...\n")
			typing("THE RUBY.\n")
			game.save()
			text.youlost()
			functions.waitingroom_teleport()
	elif glass == "2":
		clear()
		typing("You attempt to slowly lift up the glass.\n")
		typing("You obtain the TALERA RUBY!\n")
		typing("As you run for the exit of the mine, an AVALANCHE starts!\n")
		text.avalanche()
		avalanche = ""
		while avalanche not in ["1", "2", "3"]:
			avalanche = input("> ")
		if avalanche == "1":
			clear()
			typing("You attempt to run.\n")
			if speed == 10:
				typing("WHAT??? You have a speed level of 10! You successfully made it out of the cave.\n")
				if "Talera Ruby" not in game.data.trophies:
					game.data.trophies.append("Talera Ruby")
					typing("You obtained the TALERA RUBY!\n")
					typing("You have also earned 20 coins!\n")
					game.data.coins = game.data.coins + 20
					game.save()
					text.youwon()
					typing("You may have won, but you can also get the shattered ruby pieces.\n")
					functions.waitingroom_teleport()
				else:
					typing("Seems like you already have the TALERA RUBY inside your trophy room...\n")
					typing("You still have earned 10 coins!\n")
					game.data.coins = game.data.coins + 10
					game.save()
					text.youwon()
					functions.waitingroom_teleport()
			else:
				typing("The avalanche was too fast...\n")
				game.save()
				text.youlost()
				functions.waitingroom_teleport()
		elif avalanche == "2":
			clear()
			typing("You attempt to find a safe place to hide.\n")
			typing("You find a big rock to hide under.\n")
			typing("The avalanche ends.\n")
			if "Talera Ruby" not in game.data.trophies:
				game.data.trophies.append("Talera Ruby")
				typing("You obtained the TALERA RUBY!\n")
				typing("You have also earned 20 coins!\n")
				game.data.coins = game.data.coins + 20
				game.save()
				text.youwon()
			if "Shattered Ruby Pieces" not in game.data.trophies:
				typing("You may have won, but you can also get the shattered ruby pieces.\n")
				functions.waitingroom_teleport()
			else:
				typing("Seems like you already have the TALERA RUBY inside your trophy room...\n")
				typing("You still have earned 10 coins!\n")
				game.data.coins = game.data.coins + 10
				game.save()
				functions.waitingroom_teleport()
		elif avalanche == "3":
			clear()
			typing("You attempt to shield yourself with the ruby.\n")
			typing("As the rocks fall on the ruby, it shatters to pieces.\n")
			typing("Still, you have made it out of the mines.\n")
			if "Shattered Ruby Pieces" not in game.data.trophies:
				game.data.trophies.append("Shattered Ruby Pieces")
				typing("You obtained the SHATTERED RUBY PIECES!\n")
				typing("You have also earned 15 coins!\n")
				game.data.coins = game.data.coins + 15
				text.youwon()
				if "Talera Ruby" not in game.data.trophies:
					typing("You may have won, but you can still get the full ruby.\n")
				game.save()
				functions.waitingroom_teleport()
			else:
				typing("Seems like you already have the SHATTERED RUBY PIECES inside your trophy room...\n")
				typing("You have still earned 8 coins!\n")
				game.data.coins = game.data.coins + 8
				game.save()
				functions.waitingroom_teleport()
	elif glass == "3":
		clear()
		typing("You admire the ruby.\n")
		time.sleep(1)
		functions.textloading(3, "Admiring the TALERA RUBY")
		typing("How is this going to help?\n")
		text.youlost()
		game.save()
		functions.waitingroom_teleport()

def forest():
	clear()
	typing("Before we travel to THE FOREST, we need to set your levels.\n")
	time.sleep(1)
	clear()
	functions.textloading(3, "Rolling Dice")
	levelnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	knowledge = random.choice(levelnumbers)
	strength = random.choice(levelnumbers)
	charisma = random.choice(levelnumbers)
	speed = random.choice(levelnumbers)
	typing("Your knowledge level is " + str(knowledge) + ".\n")
	typing("Your strength level is " + str(strength) + ".\n")
	typing("Your charisma level is " + str(charisma) + ".\n")
	typing("Your speed level is " + str(speed) + ".\n")
	averageleveladd = knowledge + strength + charisma + speed
	averageleveldivide = averageleveladd/4
	typing("Your average level is " + str(averageleveldivide) + ".\n")
	typing("Please press enter to continue.\n")
	input("> ")
	clear()
	functions.textloading(3, "Traveling to THE FOREST")
	typing("Welcome to THE FOREST! Today, your goal is to get the ELVERN FLUTE.\n")
	typing("Let's begin!\n")
	typing("For this adventure, you need to choose a weapon. This will affect the game later on.\n")
	text.weapon_forest()
	weapon = ""
	while weapon not in ["1", "2", "3"]:
		weapon = input("> ")
	if weapon == "1":
		clear()
		typing("You have chosen the sword. Good choice!\n")
	elif weapon == "2":
		clear()
		typing("Nice! You chose the bow!\n")
	elif weapon == "3":
		clear()
		typing("The mace is a good choice!\n")
	typing("As you walk through the forest trail, you see many trees and flowers.\n")
	typing("Then, you see a sign. Would you like to read it? (y/n)\n")
	sign = ""
	while sign not in ["y", "n"]:
		sign = input("> ")
	if sign == "y":
		clear()
		typing("You read the sign. It reads:\n\n")
	elif sign == "n":
		clear()
		typing("You do not read the sign. It might have important information that will affect you later on.\n")
	typing("You continue on the road.\n")

def mountains():
	clear()
	typing("Before we travel to THE MOUNTAINS, we need to set your levels.\n")
	time.sleep(1)
	clear()
	functions.textloading(3, "Rolling Dice")
	levelnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	knowledge = random.choice(levelnumbers)
	strength = random.choice(levelnumbers)
	charisma = random.choice(levelnumbers)
	speed = random.choice(levelnumbers)
	typing("Your knowledge level is " + str(knowledge) + ".\n")
	typing("Your strength level is " + str(strength) + ".\n")
	typing("Your charisma level is " + str(charisma) + ".\n")
	typing("Your speed level is " + str(speed) + ".\n")
	averageleveladd = knowledge + strength + charisma + speed
	averageleveldivide = averageleveladd/4
	typing("Your average level is " + str(averageleveldivide) + ".\n")
	typing("Please press enter to continue.\n")
	input("> ")
	clear()
	functions.textloading(3, "Traveling to THE MOUNTAINS")
	typing("Welcome to THE MOUNTAINS! Today, your goal is to obtain the DWARVEN CLUB.\n")
	typing("Let's begin!\n")
	typing("Up ahead, you see a mountain range with many mountains.\n")
	typing("You must decide which mountain the dwarves live in.\n")
	time.sleep(1)
	clear()
	functions.textloading(3, "CHOOSING MOUNTAIN")
	typing("After hours of thinking about where dwarves may live, you narrow your options down to three choices.\n")
	text.mountain_range_mountains()
	typing("Which mountain do you choose?\n")
	chosen_mountain = ""
	while chosen_mountain not in ["1", "2", "3"]:
		chosen_mountain = input("> ")
	if chosen_mountain == "3":
		if knowledge > 4:
			typing("With a knowledge level of " + str(knowledge) + ", I'd expect you to know better.\n")
			game.save()
		else:
			typing("That is not the correct mountain.\n")
			game.save()
		text.youlost()
		functions.waitingroom_teleport()
	elif chosen_mountain == "1":
		return int(chosen_mountain)
		if speed < 5 and strength < 5:
			typing("You try to climb up Talera Mountain, but according to your skill levels, you are too weak and slow to climb it before the dwarves run away with the club.\n")
			game.save()
			text.youlost()
			functions.waitingroom_teleport()
		else:
			typing("You hike towards Talera Mountain.\n")
			time.sleep(1)
			clear()
			typing("You made it to Talera Mountain. You need to climb to the top to reach the dwarves.\n")
			typing("As you climb the mountain, you run into a disco yeti.\n")
			typing("It tries to attack you.\n")
			print("What do you do? Here are your options:")
			print("1) Use your knowledge to formulate a plan.")
			print("2) Fight")
			print("3) Run")
			print("4) Negotiate")
			yeti_choice = ""
			while yeti_choice not in ["1", "2", "3", "4"]:
				yeti_choice = input("> ")
			if yeti_choice == "1":
				if knowledge >= 5:
					typing("Since you have a knowledge level of " + str(knowledge) + ", you decide the best thing to do is to put on some disco music to distract the yeti.\n")
				else:
					typing("With a knowledge level of " + str(knowledge) + ", you are pretty dumb. For some reason, you try to get away by running into the yeti's cave.\n")
					typing("That was a mistake.\n")
					game.save()
					text.youlost()
					functions.waitingroom_teleport()
			elif yeti_choice == "2":
				if strength >= 6:
					typing("You are strong, so you knock the yeti out.\n")
				else:
					typing("Your levels say that you are weak. You know what happens.\n")
					game.save()
					text.youlost()
					functions.waitingroom_teleport()
			elif yeti_choice == "3":
				if speed >= 5:
					typing("According to your levels, you are fast. You outrun the yeti.\n")
				else:
					typing("You are too slow.\n")
					game.save()
					text.youlost()
					functions.waitingroom_teleport()
			elif yeti_choice == "4":
				if charisma >= 4:
					typing("You talk to the yeti.\n")
					typing("He allows you to pass.\n")
				else:
					typing("You have a low charisma level, so he does not allow you to pass.\n")
					game.save()
					text.youlost()
					functions.waitingroom_teleport()
	elif chosen_mountain == "2":
		if knowledge < 4:
			typing("You try to climb the widest mountain in the mountain range, but since you have a knowledge level of " + str(knowledge) + ", you get lost.\n")
			text.youlost()
			functions.waitingroom_teleport()
		else:
			typing("You hike towards Mount Goat.\n")
			time.sleep(1)
			clear()
			typing("You made it to Mount Goat. Time to climb!\n")
			typing("You found a large area. It is a good place to take a break.\n")
			typing("As you sit down, a goat walks up to you.\n")
			typing("Goat - I AM KING GOAT! I COMMAND YOU TO GET OFF MY PROPERTY!\n")
			text.goat_king()
			goat_king = ""
			while goat_king not in ["1", "2", "3", "4", "5"]:
				goat_king = input("> ")
			if goat_king == "1":
				typing("You attempt to negotiate with the goat.\n")
				if charisma > 6:
					typing("You tell the goat that you are trying to get the DWARVEN CLUB.\n")
					typing("Goat - Ah, yes... \n")
					typing("Goat - I have heard rumors that something has happened to it. You may want to go check it out.\n")
					typing("The KING GOAT allows you to pass.\n")
				else:
					typing("Goat - Nice try.\n")
					game.save()
					text.youlost()
					functions.waitingroom_teleport()
			elif goat_king == "2":
				typing("You attempt to fight the goat.\n")
				if strength > 5:
					typing("You are strong enough to beat the goat.\n")
				else:
					typing("With the goat's horns, it charges at you.\n")
					typing("You have been beat by a goat.\n")
					game.save()
					text.youlost()
					functions.waitingroom_teleport()
			elif goat_king == "3":
				typing("You attempt to give a peace offering to the goat.\n")
				if knowledge > 4:
					typing("Goat - I will allow you to pass through my territory, as long as you do not harm any of us goats.\n")
				else:
					typing("The goat denies.\n")
					game.save()
					text.youlost()
					functions.waitingroom_teleport()
			elif goat_king == "4":
				typing("You attempt to run from the goat.\n")
				if speed > 5:
					typing("You successfully outrun the goat. He is no match for you!\n")
				else:
					typing("This goat is faster than you. With a speed level of " + str(speed) + ", never try to outrun a goat.")
					game.save()
					text.youlost()
					functions.waitingroom_teleport()
			elif goat_king == "5":
				typing("You ignore the goat.\n")
				typing("That was a mistake.\n")
				game.save()
				text.youlost()
				functions.waitingroom_teleport()
	typing("Now that you have successfully got past your obstacle, you can continue on to the top of the mountain.\n")
	time.sleep(2)
	clear()
	typing("You are almost at the top of the mountain, but there is a fork. One path leads to the tip-top of the mountain, while the other leads to a cave. Where would you like to go?\n")
	print("1) The tip-top of the mountain\n2) The cave")
	split_in_road = ""
	while split_in_road not in ["1", "2"]:
		split_in_road = input("> ")
	clear()
	if split_in_road == "1":
		typing("You continue on to the tip-top of the mountain.\n")
		time.sleep(1)
		typing("You reach the tip-top of the mountain, but you realize that it is too tiny to hold a group of dwarves.\n")
		game.save()
		text.youlost()
		functions.waitingroom_teleport()
	elif split_in_road == "2":
		typing("You walk into the cave.\n")
		time.sleep(1)
		typing("It is dark, so you rub some sticks together to light a fire.\n")
		time.sleep(1)
		clear()
		functions.textloading(2, "LIGHTING FIRE")
		typing("You successfully light a fire to guide you through the cave.\n")
		typing("You walk around the cave, but don't see anything.\n")
		time.sleep(1)
		clear()
		typing("After about a half-hour, you hear voices.\n")
		typing("Voice 1 - Ah, yes. A very fantastic club this is!\n")
		typing("Voice 2 - I can't believe it's ours now!\n")
		typing("The second voice confuses you. Didn't the dwarves already own a club?\n")
		typing("You walk over towards the voices to find some robbers holding the DWARVEN CLUB.\n")
		time.sleep(1)
		clear()
		typing("The robbers see you.\n")
		typing("Robber 1 - Hey, Gerald. We've got ourselves our first test subject.\n")
		typing("Gerald - I've got the club. Shall I knock him, Rob?\n")
		typing("Rob - Yeah!\n")
		typing("The robbers knock you out.\n")
		time.sleep(1)
		clear()
		typing("When you wake up, you find yourself in a small, rundown shack with Rob and Gerald looking down at you.\n")
		typing("Gerald - Wow! This club actually has powers! It knocked him out with the lightest touch.\n")
		typing("\"Oh no,\" you say to yourself.\n")
		typing("You were wondering why this club was so important.\n")
		time.sleep(1)
		clear()
		typing("All of a sudden, Gerald puts the club down and walks over to you.\n")
		typing("It appears that he wants to tie you up in a chair.\n")
		typing("You also notice some potions on a shelf next to you.\n")
		typing("You realize that you can escape the shack using one of these things.\n")
		typing("Which would you like to use?\n")
		print("1) Grab the club and escape with it\n2) Pick up a random potion and see what it does")
		shack_escape = ""
		while shack_escape not in ["1", "2"]:
			shack_escape = input("> ")
		clear()
		if shack_escape == "1":
			typing("You grab the DWARVEN CLUB, smash (or because the club is magic, lightly touch) the wall and run outside.\n")
			typing("Rob and Gerald hop on horses and chase after you.\n")
			typing("They chase you until you get cornered.\n")
			typing("Rob - It's over now.\n")
			time.sleep(1)
			clear()
			typing("When all seems lost, some police officers on horses ride up and arrest Rob and Gerald for not only chasing you and stealing the club, but also because they tried to steal the TALERA RUBY and the ELVERN FLUTE.\n")
			typing("Police Officer - It seems as though these guys were trying to steal your club.\n")
			typing("You - Uhh, yes. This was one-hundred percent my club...\n")
			typing("Police Officer - Anyway, we should probably get these robbers to jail.\n")
			typing("The police officers ride away with Rob and Gerald.\n")
			typing("You are excited to obtain the DWARVEN CLUB.\n")
			text.youwon()
			if "DWARVEN CLUB" not in game.data.trophies:
				game.data.trophies.append("DWARVEN CLUB")
				typing("Now that the DWARVEN CLUB is yours, you obtain 20 coins.\n")
				game.data.coins += 20
				game.save()
			else:
				typing("Hmm. It looks like you already have the DWARVEN CLUB in your trophy room.\n")
				typing("You have still earned 10 coins.\n")
				game.data.coins += 10
				game.save()
			if "NON-MAGIC DWARVEN CLUB" not in game.data.trophies:
				typing("You can still get the DWARVEN CLUB without its magic powers.\n")
				game.save()
			functions.waitingroom_teleport()
		elif shack_escape == "2":
			typing("You pick up a random potion and throw it towards Rob and Gerald.\n")
			list_of_numbers = ["1", "2", "3"]
			randomnumber = random.choice(list_of_numbers)
			if randomnumber == "1":
				typing("Unfortunately, the potion you threw was an invincibility potion.\n")
				text.youlost()
				game.save()
				functions.waitingroom_teleport()
			elif randomnumber == "2":
				typing("The potion seems to have made a cloud of smoke between you and the robbers.\n")
				typing("You still see the DWARVEN CLUB, so you grab it and turn around, only to find the potion shelf.\n")
				typing("The door is on the other side of the smoke.\n")
				typing("You smash the club through the shelf and through the wall to successfully break out of the shack.\n")
				typing("However, when you smashed through the potion shelf, you smashed a potion that made the DWARVEN CLUB lose its magic.\n")
				typing("Though this is true, you have successfully escaped the robbers!\n")
				text.youwon()
				if "NON-MAGIC DWARVEN CLUB" not in game.data.trophies:
					game.data.trophies.append("NON-MAGIC DWARVEN CLUB")
					typing("You have also earned 10 coins.\n")
					game.data.coins = game.data.coins + 10
					game.save()
				else:
					typing("It seems as though the NON-MAGIC DWARVEN CLUB is already in your trophy room.\n")
					typing("You have still earned 5 coins.")
					game.data.coins = game.data.coins + 5
					game.save()
				if "DWARVEN CLUB" in game.data.trophies:
					typing("You may have won, but you can still get the DWARVEN CLUB with its magic powers.\n")
					game.save()
				functions.waitingroom_teleport()
			elif randomnumber == "3":
				typing("The potion you threw was just a glass of water.\n")
				typing("It didn't do much.\n")
				text.youlost()
				game.save()
				functions.waitingroom_teleport()

def temple_level():
	clear()
	typing("Before we travel to THE TEMPLE, we need to set your levels.\n")
	time.sleep(1)
	clear()
	functions.textloading(3, "Rolling Dice")
	levelnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	knowledge = random.choice(levelnumbers)
	strength = random.choice(levelnumbers)
	charisma = random.choice(levelnumbers)
	speed = random.choice(levelnumbers)
	typing("Your knowledge level is " + str(knowledge) + ".\n")
	typing("Your strength level is " + str(strength) + ".\n")
	typing("Your charisma level is " + str(charisma) + ".\n")
	typing("Your speed level is " + str(speed) + ".\n")
	averageleveladd = knowledge + strength + charisma + speed
	averageleveldivide = averageleveladd/4
	typing("Your average level is " + str(averageleveldivide) + ".\n")
	typing("Please press enter to continue.\n")
	input("> ")
	clear()
	functions.textloading(3, "Traveling to THE TEMPLE")
	typing("Welcome to THE TEMPLE, long lost in the jungle.\n")
	typing("Today, your goal is to obtain the GOLDEN MONKEY STATUE.\n")
	typing("You will have to avoid traps that can be found within the temple.\n")
	typing("To start, you will have to enter the temple, obviously.\n")
	typing("This is your final chance to chicken out if you want. Do you want to chicken out? (y/n)\n")
	chicken_out = ""
	while chicken_out not in ["y", "n"]:
		chicken_out = input("> ")
	clear()
	if chicken_out == "y":
		text.youlost()
		game.save()
		functions.waitingroom_teleport()
	elif chicken_out == "n":
		typing("Good choice!\n")
	typing("You have entered the temple successfully.\n")
	time.sleep(2)
	clear()
	typing("As you walk through the temple, you accidentally step on the wrong tile.\n")
	typing("The walls start closing in on you!\n")
	typing("If you don't do anything, then the walls will close in on you. However, you see an opening above the wall that you can just barely fit in.\n")
	typing("Which option do you choose?\n")
	print("1) Let the walls close in on you\n2) Hide in the small opening.")
	wall_close = ""
	while wall_close not in ["1", "2"]:
		wall_close = input("> ")
	clear()
	if wall_close == "2":
		typing("You successfully jump into the opening.\n")
		typing("However, you remember that you are claustrophobic. You do not like small spaces.\n")
		typing("Also, you got stuck.\n")
		text.youlost()
		game.save()
		functions.waitingroom_teleport()
	elif wall_close == "1":
		typing("You stand and let the walls close.\n")
		typing("That's when you discover a flaw in the temple's design.\n")
		typing("The walls don't close all the way.\n")
		typing("You are safe!\n")
	typing("Now that you have avoided the walls, you can continue on to find your treasure.\n")
	time.sleep(1)
	clear()
	typing("It turns out that you are bad at figuring out where to step. You stepped on the wrong tile AGAIN!\n")
	typing("This time, it's evil hamsters you have to look out for.\n")
	typing("There are a few things you can do:\n")
	print("1) Fight\n2) Run\n3) Negotiate\n4) Use your brainy powers.")
	evil_hamsters = ""
	while evil_hamsters not in ["1", "2", "3", "4"]:
		evil_hamsters = input("> ")
	clear()
	if evil_hamsters == "1":
		typing("You attempt to fight the hamsters.\n")
		if strength >= 3:
			typing("You are strong enough to defeat the hamsters.\n")
		else:
			typing("Apparently, you are too weak to defeat those evil yet adorable hamsters.\n")
			typing("How embarrassing!\n")
			text.youlost()
			game.save()
			functions.waitingroom_teleport()
	elif evil_hamsters == "2":
		typing("You attempt to run from the hamsters.\n")
		some_random_numbers = ["1", "2"]
		a_random_number = random.choice(some_random_numbers)
		if a_random_number == "1":
			typing("Unfortunately, some doors close, leaving you in a small room with the hamsters.\n")
			text.youlost()
			game.save()
			functions.waitingroom_teleport()
		elif a_random_number == "2":
			if speed >= 3:
				typing("You outrun the hamsters!\n")
			else:
				typing("The hamsters are too fast for you.\n")
				text.youlost()
				game.save()
				functions.waitingroom_teleport()
	elif evil_hamsters == "3":
		typing("You attempt to negotiate with the hamsters.\n")
		typing("Since they are hamsters, they don't understand English, Español, Français, or even 中文!\n")
		text.youlost()
		game.save()
		functions.waitingroom_teleport()
	elif evil_hamsters == "4":
		typing("You attempt to use your knowledge to come up with a plan.\n")
		if knowledge >= 3:
			typing("You look around and notice some hamster food on a nearby shelf.\n")
			typing("Knowing that animals do anything for food, you chase them over to the hamster food.\n")
			typing("It's the perfect distraction.\n")
		else:
			typing("Since you have a knowledge level of %s, you are not the smartest and try to pick up the hamsters so they won't run at you.\n" % knowledge)
			text.youlost()
			game.save()
			functions.waitingroom_teleport()
	typing("Now, you can continue on your journey through the temple.\n")
	time.sleep(2)
	clear()
	typing("The floor must not like you, because you step in some quicksand.\n")
	typing("If you're not careful, then you will get stuck inside it...forever!\n")
	typing("You must make a decision quick!\n")
	print("Here are your options:\n1) Wiggle out\n2) Grab something and use it to pull yourself out\n3) Call for help")
	quicksand = ""
	# x = 1
	while quicksand not in ["1", "2", "3"]:
		quicksand = input("> ")
		# x += 1
		# time.sleep(1)
		# if x > 9:
		# 	clear()
		# 	typing("Unfortunately, you ran out of time to make a decision.\n")
		# 	text.youlost()
		# 	functions.waitingroom_teleport()
	clear()
	if quicksand == "1":
		typing("You try to wiggle yourself out.\n")
		if strength > 7:
			typing("You are very strong, so you are able to wiggle yourself out.\n")
		else:
			typing("You are no match for the quicksand.\n")
			text.youlost()
			game.save()
			functions.waitingroom_teleport()
	elif quicksand == "2":
		typing("You look around for something to grab.\n")
		typing("You find a nearby rope that you can reach.\n")
		typing("You successfully pull yourself out of the quicksand.\n")
	elif quicksand == "3":
		typing("You call for help.\n")
		typing("Why would there be someone in the temple who would help you out?\n")
		if knowledge > 5:
			typing("With a knowledge level of %s, I'd expect you to know better.\n" % knowledge)
		text.youlost()
		game.save()
		functions.waitingroom_teleport()
	typing("Now you can keep searching for the GOLDEN MONKEY STATUE.\n")
	time.sleep(1)
	clear()
	typing("You walk into a room that is pitch black.\n")
	typing("You feel around for a light switch.\n")
	typing("Once you find one, you flip it and find the GOLDEN MONKEY STATUE sitting on a pedestal in the middle of the room.\n")
	typing("You walk over and pick it up.\n")
	typing("Then, the temple starts collapsing!\n")
	typing("You run with the statue outside the room.\n")
	typing("The area that was once quicksand is now LAVA!\n")
	typing("You have to come up with an idea to get across.\n")
	typing("You remember that the rope you used earlier to pull yourself out of the quicksand is still there.\n")
	typing("You can use it to swing across the lava pool.\n")
	typing("However, you also find rocks in the lava that are big enough for you to jump on and make a path.\n")
	typing("This is a risky option, though. The rope swinging seems safer.\n")
	typing("Which option do you choose?\n")
	print("1) Swing with the rope\n2) Jump across using the rocks.")
	lava_lake = ""
	while lava_lake not in ["1", "2"]:
		lava_lake = input("> ")
	clear()
	if lava_lake == "1":
		typing("You set down the statue to toss the rope onto a hook on the celing.\n")
		typing("Then, you swing across!\n")
		typing("Once you make it across, you look behind you to see the floor on the other side starting to flood and burn, along with the GOLDEN MONKEY STATUE you accidentally left behind.\n")
		text.youlost()
		game.save()
		functions.waitingroom_teleport()
	elif lava_lake == "2":
		typing("You hold the statue tight in your arms as you barely land on the first rock.\n")
		typing("After several minutes, you make it to the other side, with the GOLDEN MONKEY STATUE safe and sound.\n")
	typing("Then, lava starts rushing after you.\n")
	typing("Even if you have a knowledge level of 1, you know there is only one thing to do:\n")
	typing("RUN.\n")
	time.sleep(2)
	clear()
	functions.textloading(3, "RUNNING FROM LAVA")
	clear()
	typing("You successfully made it out of the temple.\n")
	typing("Behind you, you see the temple completely collapse.\n")
	typing("Bye bye, temple!\n")
	text.youwon()
	if "GOLDEN MONKEY STATUE" not in game.data.trophies:
		game.data.trophies.append("GOLDEN MONKEY STATUE")
		typing("You have successfully obtained the GOLDEN MONKEY STATUE, earning you 25 coins.\n")
		game.data.coins += 25
	else:
		typing("It looks as though you have already obtained the GOLDEN MONKEY STATUE. Well, I guess I'll still give you 8 coins.\n")
		game.data.coins += 8
	game.save()
	functions.waitingroom_teleport()

def lab():
	clear()
	typing("Before we travel to THE LAB, we need to set your levels.\n")
	time.sleep(1)
	clear()
	functions.textloading(3, "Rolling Dice")
	levelnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	knowledge = random.choice(levelnumbers)
	strength = random.choice(levelnumbers)
	charisma = random.choice(levelnumbers)
	speed = random.choice(levelnumbers)
	typing("Your knowledge level is " + str(knowledge) + ".\n")
	typing("Your strength level is " + str(strength) + ".\n")
	typing("Your charisma level is " + str(charisma) + ".\n")
	typing("Your speed level is " + str(speed) + ".\n")
	averageleveladd = knowledge + strength + charisma + speed
	averageleveldivide = averageleveladd/4
	typing("Your average level is " + str(averageleveldivide) + ".\n")
	typing("Please press enter to continue.\n")
	input("> ")
	clear()
	functions.textloading(3, "Traveling to THE LAB")
	clear()
	typing("Ooooooooooooooooooooh. The LAB looks fancy.\n")
	typing("By fancy, I mean that it has a lot of neat stuff.\n")
	typing("Look at that teleportation device over there.\n")
	typing("Anyway, lets not get distracted.\n")
	typing("According to the map you saw, there is a mystery trophy you have to obtain.\n")
	typing("Lets see what it is!\n")
	time.sleep(1)
	clear()
	typing("How about you use that teleportation device to transport yourself around?\n")
	typing("As you transport around, you find one invention with a plaque.\n")
	typing("The plaque says: MYSTERY TROPHY: TIME MACHINE\n")
	typing("Well, you found the mystery trophy. That didn't take long at all, did it?\n")
	typing("That's when you hear a voice yelling at you.\n")
	typing("Voice 1 - Hey! You aren't supposed to be here!\n")
	typing("That voice came from a scientist, who appears to be chasing after you.\n")
	typing("There are a few options you have:\n")
	print("1) Fight\n2) Run\n3) Negotiate\n4) Use your knowledge powers\n5) Hide in the TIME MACHINE")
	typing("Please choose one of these options\n")
	scientist_escape = ""
	while scientist_escape not in ["1", "2", "3", "4", "5"]:
		scientist_escape = input("> ")
	if scientist_escape == "1":
		clear()
		typing("You try to fight the scientist.\n")
		typing("Unfortunately, he picks up his OVER-POWERED BOXING GLOVES he invented.\n")
		text.youlost()
		functions.waitingroom_teleport()
	elif scientist_escape == "2":
		typing("You try to run from the scientist.\n")
		typing("Sadly, he puts on his CHEETAH-STYLE boots he invented.\n")
		typing("You are no match for him.\n")
		text.youlost()
		functions.waitingroom_teleport()
	elif scientist_escape ==  "3":
		typing("You try to negotiate with the scientist.\n")
		typing("He is smart enough to know not to fall for that.\n")
		text.youlost()
		functions.waitingroom_teleport()
	elif scientist_escape == "4":
		typing("You try to come up with a good plan.\n")
		typing("Unfortunately, the scientist is much smarter than you by a thousand levels, so no matter what you do, he outsmarts it.\n")
		text.youlost()
		functions.waitingroom_teleport()
	elif scientist_escape == "5":
		typing("You hide in the TIME MACHINE.\n")
		typing("You can't hide from the scientist.\n")
		typing("You nervously press a few buttons.\n")
		print("ZAP")
		typing("You find yourself outside the front doors of the lab.\n")
		typing("Then you see someone walking inside the lab.\n")
		typing("Then you realize something.\n")
		typing("You see yourself walking in the lab.\n")
		typing("You have accidentally travelled back in time.\n")
		time.sleep(2)
		clear()
	typing("You try to time travel back to the present, but your time machine is broken.\n")
	typing("Not knowing what else to do, you sneak inside the lab to get a glimpse of the original time machine before it broke so you can fix it.\n")
	typing("You make it to the time machine before, well, Past You.\n")
	typing("As you observe the time machine, you notice a nearby teleportation device lighting up.\n")
	typing("You quickly hide behind the time machine.\n")
	typing("Then, you see Past You come out of the teleporter.\n")
	typing("You watch Past You view the machine, and see the angry scientist come along.\n")
	typing("After Past You time travels to the past, the scientist sees you.\n")
	typing("Scientist - How did you get here?\n")
	typing("You realize you can get information from him about fixing the time machine.\n")
	print("Here are the best ways to do it:")
	print("1) Trick him into giving you the information\n2) Fight\n3) Make him chase you so he gets tired\n4) Negotiate")
	typing("Please pick an option\n")
	scientist_help = ""
	while scientist_help not in ["1", "2", "3", "4"]:
		scientist_help = input("> ")
	clear()
	if scientist_help == "1":
		typing("You try to trick the scientist into giving you the information.\n")
		if knowledge > 5:
			typing("Scientist - So you come from the future where my invention is a success and you came to ask me to fix it when it broke?\n")
			typing("The scientist fixes the time machine for you.\n")
			typing("You time travel back to the present.\n")
			typing("All is well.\n")
			text.youwon()
			game.data.trophies.append("TIME MACHINE")
			typing("You have successfully earned the TIME MACHINE, earning you 25 coins.\n")
			game.data.coins += 25
			functions.waitingroom_teleport()
		else:
			typing("Your knowledge level of %s won't really get you anywhere.\n" % knowledge)
			text.youlost()
			functions.waitingroom_teleport()
	elif scientist_help == "2":
		typing("You attempt to fight the scientist.\n")
		if strength > 5:
			typing("You were able to beat the scientist, even though he used his MEGA FISTS.\n")
			typing("Unfortunately, you have nobody to help you fix the time machine.\n")
			typing("You are stuck in the past.\n")
		else:
			typing("With a strength level of %s, you can't beat the scientist.\n")
		text.youlost()
		functions.waitingroom_teleport()
	elif scientist_help == "3":
		typing("YOu attempt to make the scientist tired by making hime chase you.\n")
		if speed > 4:
			typing("You outran the scientist.\n")
			typing("He is tired.\n")
			typing("He goes to get a cup of coffee.\n")
			typing("You stop the scientist and request him to fix the time machine.\n")
			typing("He accepts.\n")
			typing("He fixes the time machine.\n")
			typing("You time travel back to the present.\n")
			text.youwon()
			game.data.trophies.append("TIME MACHINE")
			typing("You have successfully earned the TIME MACHINE, earning you 25 coins.\n")
			game.data.coins += 25
			functions.waitingroom_teleport()
		else:
			typing("The scientist is too fast for you.\n")
			text.youlost()
			functions.waitingroom_teleport()
	elif scientist_help == "4":
		typing("You attempt to negotiate with the scientist.\n")
		if charisma > 3:
			typing("Scientist - Why should I help you fix my time machine?\n")
			typing("You - Because it's yours.\n")
			typing("That seemed to work.\n")
			typing("The scientist fixes the machine.\n")
			typing("Then you quickly time travel back to the present without his permission.\n")
			text.youwon()
			game.data.trophies.append("TIME MACHINE")
			typing("You have successfully earned the TIME MACHINE, earning you 25 coins.\n")
			game.data.coins += 25
			functions.waitingroom_teleport()
		else:
			typing("The scientist is too smart for that.\n")
			text.youlost()
			functions.waitingroom_teleport()

def test():
	game.data.coins += 100
	if "GOLDEN MONKEY STATUE" not in game.data.trophies:
		game.data.trophies.append("TOTALLY SECRET TROPHY THAT YOU ARE NOT SUPPOSED TO KNOW ABOUT")
		typing("You have successfully obtained the TOTALLY SECRET TROPHY THAT YOU ARE NOT SUPPOSED TO KNOW ABOUT, earning you 25 coins.\n")
		game.data.coins += 25
	else:
		typing("It looks as though you have already obtained the TOTALLY SECRET TROPHY THAT YOU ARE NOT SUPPOSED TO KNOW ABOUT. Well, I guess I'll still give you 8 coins.\n")
		game.data.coins += 8
	game.save()