import functions
import text
import sys
import time
import random
import os
import levels
import game

#hi

typingspeed = 100
#coins = 0
#rustic_coins = 0
#gems = 0
#tuna = 0
#salmon = 0
#cod = 0
#clownfish = 0
# hat = "N/A"
# shirt = "Hand-me-down shirt from your older neanderthal brother"
# pants = "Torn Jeans"
# shoes = "N/A (Looks like you're a hobbit)"
# outerwear = "N/A"
# item = "Distorted Stick"
# trophies = []

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

def city_teleport():
	clear()
	functions.textloading(3, "Travelling to THE CITY")
	cityhub()

def cityhub():
	while True:
		clear()
		print("Welcome to THE CITY!")
		print("You have " + str(game.data.coins) + " coins.")
		print("1) Olga's Coffee House")
		print("2) Aaron's Apparel")
		print("3) The Docks")
		print("4) Trophy Room")
		print("5) Inventory")
		print("6) Exit")
		city_options = ""
		while city_options not in ["1", "2", "3", "4", "5", "6"]:
			city_options = input("> ")
		if city_options == "1":
			clear()
			print("Welcome to Olga's Coffee House!")
			print("You have " + str(game.data.coins) + " coins.")
			print("1) Gas Station Coffee - 5 coins")
			print("2) Normal Black Coffee - 8 coins")
			print("3) Cappuccino - 11 coins")
			print("4) Latte - 13 coins")
			print("5) Elvern Berry Cold Brew Tea - 16 coins")
			print("6) Exit Shop")
			coffee = ""
			while coffee not in ["1", "2", "3", "4", "5", "6"]:
				coffee = input("> ")
			if coffee == "1":
				gas_station_coffee_price = 5
				if game.data.coins < gas_station_coffee_price:
					clear()
					typing("You do not have enough coins to buy this.\n")
					short = str(gas_station_coffee_price - game.data.coins)
					typing("You are " + short + " coins short.")
					time.sleep(2)
				else:
					clear()
					game.data.coins = game.data.coins - gas_station_coffee_price
					typing("You now have " + str(game.data.coins) + " coins.\n")
					game.save()
					typing("You drink your gas station coffee. The taste leaves you dissatisfied.\n")
					typing("Please press enter to continue.\n")
					input("> ")
			elif coffee == "2":
				black_coffee_price = 8
				if game.data.coins < black_coffee_price:
					clear()
					typing("You do not have enough coins to buy this.\n")
					short = str(black_coffee_price - game.data.coins)
					typing("You are " + short + " coins short.")
					time.sleep(2)
				else:
					clear()
					game.data.coins = game.data.coins - black_coffee_price
					typing("You now have " + str(game.data.coins) + " coins.\n")
					game.save()
					typing("You drink your black coffee. Nothing special, just makes you feel warm inside.\n")
					typing("Please press enter to continue.\n")
					input("> ")
			elif coffee == "3":
				cappuccino_price = 11
				if game.data.coins < cappuccino_price:
					clear()
					typing("You do not have enough coins to buy this.\n")
					short = str(cappuccino_price - game.data.coins)
					typing("You are " + short + " coins short.")
					time.sleep(2)
				else:
					clear()
					game.data.coins = game.data.coins - cappuccino_price
					typing("You now have " + str(game.data.coins) + " coins.\n")
					game.save()
					typing("You drink your cappuccino. It tastes very good!\n")
					typing("Please press enter to continue.\n")
					input("> ")
			elif coffee == "4":
				latte_price = 13
				if game.data.coins < latte_price:
					clear()
					typing("You do not have enough coins to buy this.\n")
					short = str(latte_price - game.data.coins)
					typing("You are " + short + " coins short.")
					time.sleep(2)
				else:
					clear()
					game.data.coins = game.data.coins - latte_price
					typing("You now have " + str(game.data.coins) + " coins.\n")
					game.save()
					typing("You drink your latte. The combonation of milk and coffee is sensational!\n")
					typing("Please press enter to continue.\n")
					input("> ")
			elif coffee == "5":
				elvern_berry_tea_price = 16
				if game.data.coins < elvern_berry_tea_price:
					clear()
					typing("You do not have enough coins to buy this.\n")
					short = str(elvern_berry_tea_price - game.data.coins)
					typing("You are " + short + " coins short.")
					time.sleep(2)
				else:
					clear()
					game.data.coins = game.data.coins - elvern_berry_tea_price
					typing("You now have " + str(game.data.coins) + " coins.\n")
					game.save()
					typing("You drink your elvern berry cold brew tea. The sweetness along with some tartness just makes your day!\n")
					typing("Please press enter to continue.\n")
					input("> ")
			elif coffee == "6":
				clear()
				typing("You have exited the shop.\n")
		elif city_options == "2":
			clear()
			print("Welcome to Aaron's Apparel!")
			print("You have " + str(game.data.coins) + " coins.")
			print("What would you like to buy?")
			print("1) Hat")
			print("2) Shirt")
			print("3) Pants")
			print("4) Shoes")
			print("5) Outerwear")
			print("6) Items")
			print("7) Exit")
			apparel = ""
			while apparel not in ["1", "2", "3", "4", "5", "6", "7"]:
				apparel = input("> ")
			if apparel == "1":
				clear()
				print("HATS")
				print("1) Fedora - 15 coins")
				print("2) Baseball Cap - 10 coins")
				print("3) I❤LT Hat - 5 coins")
				print("4) Bike Helmet - 20 coins")
				hats = ""
				while hats not in ["1", "2", "3"]:
					hats = input("> ")
				if hats == "1":
					fedora_price = 15
					if game.data.coins < fedora_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(fedora_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - fedora_price
						game.data.hat = "Fedora"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("I think this fedora looks nice on you! You look like a secret agent...\n")
						typing("Please press enter to continue.\n")
						input("> ")
				if hats == "2":
					baseball_cap_price = 10
					if game.data.coins < baseball_cap_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(baseball_cap_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - baseball_cap_price
						game.data.hat = "Baseball Cap"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("I think this baseball cap looks nice on you!\n")
						typing("Please press enter to continue.\n")
						input("> ")
				if hats == "3":
					talera_hat_price = 5
					if game.data.coins < talera_hat_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(talera_hat_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - talera_hat_price
						game.data.hat = "I❤LT Hat"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("Good choice! I❤LT!\n")
						typing("Please press enter to continue.\n")
						input("> ")
				if hats == "4":
					talera_hat_price = 20
					if game.data.coins < talera_hat_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(talera_hat_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - talera_hat_price
						game.data.hat = "Bike Helmet"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("Nothing like a bike helmet to keep you nice and safe!\n")
						typing("Please press enter to continue.\n")
						input("> ")
			elif apparel == "2":
				clear()
				print("SHIRTS")
				print("1) White T-Shirt - 10 coins")
				print("2) I❤LT T-Shirt - 15 coins")
				if levels.mountains() == 1 and "DWARVEN CLUB" or "NON-MAGIC DWARVEN CLUB" in game.data.trophies:
					print("3) I CONQUERED TALERA MOUNTAIN T-shirt - 20 coins")
				shirts = ""
				if levels.mountains() == 1 and "DWARVEN CLUB" or "NON-MAGIC DWARVEN CLUB" in game.data.trophies:
					while shirts not in ["1", "2", "3"]:
						shirts = input("> ")
				else:
					while shirts not in ["1", "2"]:
						shirts = input("> ")
				if shirts == "1":
					white_Tshirt_price = 10
					if game.data.coins < white_Tshirt_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(white_Tshirt_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - white_Tshirt_price
						game.data.shirt = "White T-Shirt"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("This is a nice, clean, white shirt. Don't get it dirty!\n")
						typing("Please press enter to continue.\n")
						input("> ")
				if shirts == "2":
					talera_shirt_price = 15
					if game.data.coins < talera_shirt_price:
						clear()
						typing("You do not have enough .coins to buy this.\n")
						short = str(talera_shirt_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - talera_shirt_price
						game.data.shirt = "I❤LT T-Shirt"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						if game.data.hat == "I❤LT Hat":
							typing("It fits nice with the hat. Now you are a REAL fan!\n")
						else:
							typing("You should also try to get the matching hat!\n")
						typing("Please press enter to continue.\n")
						input("> ")
					if shirts == "3":
						talera_shirt_price = 20
					if game.data.coins < talera_shirt_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(talera_shirt_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - talera_shirt_price
						game.data.shirt = "I CONQUERED TALERA MOUNTAIN T-shirt"
						typing("You now have " + str(game.data.coins) + " .coins.\n")
						game.save()
						typing("This shirt proves that you are a real adventurer!\n")
						typing("Please press enter to continue.\n")
						input("> ")
			elif apparel == "3":
				clear()
				print("PANTS")
				print("1) Blue Jeans - 15 coins")
				print("2) Gym Shorts - 15 coins")
				pair_of_pants = ""
				while pair_of_pants not in ["1", "2"]:
					pair_of_pants = input("> ")
				if pair_of_pants == "1":
					blue_jeans_price = 15
					if game.data.coins < blue_jeans_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(blue_jeans_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - blue_jeans_price
						game.data.pants = "Blue Jeans"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("Yay! Classic blue jeans!\n")
						typing("Please press enter to continue.\n")
						input("> ")
				elif pair_of_pants == "2":
					gym_shorts_price = 15
					if game.data.coins < gym_shorts_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(gym_shorts_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - gym_shorts_price
						game.data.pants = "Gym Shorts"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("Gym Shorts. I guess you are ready to work out!\n")
						typing("Please press enter to continue.\n")
						input("> ")
			elif apparel == "4":
				clear()
				print("SHOES")
				print("1) Off-brand Ripoff Sneakers - 6 coins")
				print("2) Hiking Boots - 10 coins")
				shoes_choose = ""
				while shoes_choose not in ["1", "2"]:
					shoes_choose = input("> ")
				if shoes_choose == "1":
					ripoff_sneakers_price = 6
					if game.data.coins < ripoff_sneakers_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(ripoff_sneakers_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - ripoff_sneakers_price
						game.data.shoes = "Off-brand Ripoff Sneakers"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("Oh, nice! You got some cool sneakers! Hmm... something seems different...\n")
						typing("Please press enter to continue.\n")
						input("> ")
				elif shoes_choose == "2":
					hiking_boots_price = 10
					if game.data.coins < hiking_boots_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(hiking_boots_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - hiking_boots_price
						game.data.shoes = "Hiking Boots"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("Oh, cool! Now you are a dedicated hiker!\n")
						typing("Please press enter to continue.\n")
						input("> ")
			elif apparel == "5":
				clear()
				print("OUTERWEAR")
				print("1) Winter Coat - 20 coins")
				print("2) Necktie - 10 coins")
				print("3) Bow Tie - 10 coins")
				outerwear_choose = ""
				while outerwear_choose not in ["1", "2", "3"]:
					outerwear_choose = input("> ")
				if outerwear_choose == "1":
					winter_coat_price = 20
					if game.data.coins < winter_coat_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(winter_coat_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - winter_coat_price
						game.data.outerwear = "Winter Coat"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("A nice coat to keep you warm through the cold winter days.\n")
						typing("Please press enter to continue.\n")
						input("> ")
				elif outerwear_choose == "3":
					necktie_price = 10
					if game.data.coins < necktie_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(necktie_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - necktie_price
						game.data.outerwear = "Necktie"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("Pretty formal, eh?\n")
						typing("Please press enter to continue.\n")
						input("> ")
				elif outerwear_choose == "3":
					bowtie_price = 10
					if game.data.coins < bowtie_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(bowtie_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - bowtie_price
						game.data.outerwear = "Bowtie"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("Nice!\n")
						typing("Please press enter to continue.\n")
						input("> ")
			elif apparel == "6":
				clear()
				print("ITEMS")
				print("1) Trusty Backpack - 12 coins")
				print("2) Hiking Stick - 10 coins")
				items = ""
				while items not in ["1", "2"]:
					items = input("> ")
				if items == "1":
					trusty_backpack_price = 12
					if game.data.coins < trusty_backpack_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(trusty_backpack_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - trusty_backpack_price
						game.data.item = "Trusty Backpack"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("Just like it says in the name, it is VERY trusty!\n")
						typing("Please press enter to continue.\n")
						input("> ")
				if items == "2":
					hiking_stick_price = 10
					if game.data.coins < hiking_stick_price:
						clear()
						typing("You do not have enough coins to buy this.\n")
						short = str(hiking_stick_price - game.data.coins)
						typing("You are " + short + " coins short.")
						time.sleep(2)
					else:
						clear()
						game.data.coins = game.data.coins - hiking_stick_price
						game.data.item = "Hiking Stick"
						typing("You now have " + str(game.data.coins) + " coins.\n")
						game.save()
						typing("A nice looking stick to support you while hiking.\n")
						typing("Please press enter to continue.\n")
						input("> ")
			elif apparel == "7":
				clear()
				typing("You have exited the shop.\n")
		elif city_options == "3":
			clear()
			print("Welcome to THE DOCKS!")
			print("At the docks, you can go fishing for some loot, or trade in your fish ")
			print("You have " + str(game.data.coins) + " coins.")
			print("1) Go Fishing - 1 coin")
			print("2) Go to the Fishmonger")
			docks_options = ""
			while docks_options not in ["1", "2"]:
				docks_options = input("> ")
			if docks_options == "1":
				if game.data.coins < 1:
					clear()
					typing("You do not have enough coins to buy this.\n")
					time.sleep(2)
				else:
					clear()
					game.data.coins = game.data.coins - 1
					functions.textloading(1, "FISHING")
					fish_options = ["Talera Ruby", "Rustic Coin", "Rustic Coin", "Rustic Coin", "Rustic Coin", "Rustic Coin", "Treasure Chest", "Treasure Chest", "Treasure Chest", "Old Boot", "Old Boot", "Old Boot", "Old Boot", "Old Boot", "Old Boot", "Old Boot", "Old Boot", "Old Boot", "Old Boot", "Wet Sock", "Wet Sock", "Wet Sock", "Wet Sock", "Wet Sock", "Wet Sock", "Wet Sock", "Someone's Underwear", "Someone's Underwear", "Someone's Underwear", "Someone's Underwear", "Someone's Underwear", "Someone's Underwear", "Another Fishing Rod", "Another Fishing Rod", "Another Fishing Rod", "Another Fishing Rod", "Another Fishing Rod", "Shark", "Shark", "Shark", "Shark", "Salmon", "Salmon", "Salmon", "Salmon", "Salmon", "Salmon", "Salmon", "Salmon", "Salmon", "Salmon", "Cod", "Cod", "Cod", "Cod", "Cod", "Cod", "Cod", "Cod", "Cod", "Cod", "Clownfish", "Clownfish", "Clownfish", "Clownfish", "Clownfish", "Clownfish", "Clownfish", "Clownfish", "Clownfish", "Clownfish", "Tuna", "Tuna", "Tuna", "Tuna", "Tuna", "Tuna", "Tuna", "Tuna", "Tuna", "Tuna"]
					random_item = random.choice(fish_options)
					if random_item == "Talera Ruby":
						numbers = ["1", "2", "3"]
						random_number = random.choice(numbers)
						if random_number == "3":
							if "Talera Ruby" not in game.data.trophies:
								typing("Woah! You got the Talera Ruby! I wonder how it got in the water...\n")
							else:
								typing("You got nothing.\n")
						else:
							typing("You got nothing.\n")
					elif random_item == "Rustic Coin":
						typing("Nice. You got a rustic coin. These are worth 5 coins. Adding 5 coins to your treasury...\n")
						game.data.coins = game.data.coins + 5
						game.save()
					elif random_item == "Treasure Chest":
						typing("Cool! You got a treasure chest! I wonder what could be inside?\n")
						loot = ["20 coins", "3 gems", "A seagull", "An old boot"]
						random_loot = random.choice(loot)
						if random_loot == "20 coins":
							typing("Nice! 20 coins were found in the chest!\n")
							game.data.coins = game.data.coins + 20
							game.save()
						elif random_loot == "3 gems":
							typing("Cool! You found 3 gems!\n")
							gems = gems + 3
							game.save()
						elif random_loot == "A seagull":
							typing("AHHHH!!! A SEAGULL!!!\n")
						elif random_loot == "An old boot":
							typing("You found an old boot. Worthless. Just throw it back in the water.\n")
					elif random_item == "Old Boot":
						typing("You got an old boot. Worthless. Just throw it back in the water.\n")
					elif random_item == "Wet Sock":
						typing("You got a wet sock. Worthless. Just throw it back in the water.\n")
					elif random_item == "Someone's Underwear":
						typing("Someone's underwear? Put that back in the water immediately. Hopefully the underwear is empty...\n")
					elif random_item == "Another Fishing Rod":
						typing("Hmm... Another fishing rod. How peculiar.\n")
					elif random_item == "Shark":
						typing("SHARK!!!!!\n")
						time.sleep(1)
						clear()
						functions.textloading(3, "FIGHTING SHARK")
						typing("The shark ate 10 of your coins.\n")
						game.data.coins = game.data.coins - 10
						game.save()
					elif random_item == "Salmon":
						typing("Nice. You caught yourself some salmon.\n")
						game.data.salmon = game.data.salmon + 1
						game.save()
					elif random_item == "Cod":
						typing("Nice. You caught yourself some cod.\n")
						game.data.cod = game.data.cod + 1
						game.save()
					elif random_item == "Clownfish":
						typing("Nice. You caught yourself some clownfish.\n")
						game.data.clownfish = game.data.clownfish + 1
						game.save()
					elif random_item == "Tuna":
						typing("Nice. You caught yourself some tuna.\n")
						game.data.tuna = game.data.tuna + 1
						game.save()
					time.sleep(1)
			if docks_options == "2":
				clear()
				print("Welcome to THE FISHMONGER!")
				print("You have " + str(game.data.salmon) + " salmon.")
				print("You have " + str(game.data.cod) + " cod.")
				print("You have " + str(game.data.clownfish) + " clownfish.")
				print("You have " + str(game.data.tuna) + " tuna.")
				print("1) Salmon - 2 coins")
				print("2) Cod - 1 coin")
				print("3) Clownfish - 2 coins")
				print("4) Tuna - 1 coin")
				fishmonger = ""
				while fishmonger not in ["1", "2", "3", "4"]:
					fishmonger = input("> ")
				if fishmonger == "1":
					clear()
					typing("How much salmon would you like to sell?\n")
					salmon_sell = int(input("> "))
					salmon_price = 2
					if game.data.salmon < salmon_sell:
						clear()
						typing("You do not have enough salmon to sell this.\n")
					else:
						clear()
						game.data.coins = game.data.coins + (salmon_sell * salmon_price)
						typing("You have made " + str(salmon_sell * salmon_price) + " coins!")
						game.data.salmon = game.data.salmon - salmon_sell
						game.save()
				if fishmonger == "2":
					clear()
					typing("How much cod would you like to sell?\n")
					cod_sell = int(input("> "))
					cod_price = 1
					if game.data.cod < cod_sell:
						clear()
						typing("You do not have enough cod to sell this.\n")
					else:
						clear()
						game.data.coins = game.data.coins + (cod_sell * cod_price)
						typing("You have made " + str(cod_sell * cod_price) + " coins!")
						game.data.cod = game.data.cod - cod_sell
						game.save()
				if fishmonger == "3":
					clear()
					typing("How much clownfish would you like to sell?\n")
					clownfish_sell = int(input("> "))
					clownfish_price = 2
					if game.data.clownfish < clownfish_sell:
						clear()
						typing("You do not have enough clownfish to sell this.\n")
					else:
						clear()
						game.data.coins = game.data.coins + (clownfish_sell * clownfish_price)
						typing("You have made " + str(clownfish_sell * clownfish_price) + " coins!")
						game.data.clownfish = game.data.clownfish - clownfish_sell
						game.save()
				if fishmonger == "4":
					clear()
					typing("How much tuna would you like to sell?\n")
					tuna_sell = int(input("> "))
					tuna_price = 1
					if game.data.tuna < tuna_sell:
						clear()
						typing("You do not have enough tuna to sell this.\n")
					else:
						clear()
						game.data.coins = game.data.coins + (tuna_sell * tuna_price)
						typing("You have made " + str(tuna_sell * tuna_price) + " coins!")
						game.data.tuna = game.data.tuna - tuna_sell
						game.save()
					time.sleep(1)
		elif city_options == "4":
			clear()
			typing("Welcome to your trophy room!\n")
			if game.data.trophies == []:
				typing("Hmm... Seems like you do not have any trophies. How do you fix this? GO DO SOME QUESTS!!!\n")
			else:
				typing("Here are your trophies:\n")
				for t in game.data.trophies:
					typing(t + "\n")
			typing("Please press enter to continue.\n")
			input("> ")
		elif city_options == "5":
			clear()
			typing("Here is your inventory:\n")
			print("Hat - " + game.data.hat)
			print("Shirt - " + game.data.shirt)
			print("Pants - " + game.data.pants)
			print("Shoes - " + game.data.shoes)
			print("Outerwear - " + game.data.outerwear)
			print("Item - " + game.data.item)
			typing("Please press enter to continue.\n")
			input("> ")
		elif city_options == "6":
			clear()
			typing("You have now left the city.\n")
			time.sleep(2)
			clear()
			levels.waiting_room()