import functions
import text
import sys
import time
import random
import os
import levels
import game

typingspeed = 100
coins = 0
hat = "N/A"
shirt = "Hand-me-down shirt from your neanderthal brother"
pants = "Torn Jeans"
shoes = "None (Looks like you're a hobbit)"
outerwear = "N/A"
item = "Distorted Stick"
trophies = []

def clear():
	if sys.platform.startswith("linux"):
		os.system("clear")
	elif sys.platform.startswith("win32"):
		os.system("cls")

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
    global coins
    global hat
    global shirt
    global pants
    global shoes
    global outerwear
    global item
    while True:
        clear()
        print("Welcome to THE CITY!")
        print("You have " + str(coins) + " coins.")
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
            print("You have " + str(coins) + " coins.")
            print("1) Gas Station Coffee - 5 coins")
            print("2) Normal Black Coffee - 8 coins")
            print("3) Cappuccino - 11 coins")
            print("4) Latte - 13 coins")
            print("5) Elvern Berry Cold Brew Tea - 16 coins")
            coffee = ""
            while coffee not in ["1", "2", "3", "4", "5"]:
                coffee = input("> ")
            if coffee == "1":
                gas_station_coffee_price = 5
                if coins < gas_station_coffee_price:
                    clear()
                    typing("You do not have enough coins to buy this.\n")
                    time.sleep(2)
                else:
                    clear()
                    coins = coins - gas_station_coffee_price
                    typing("You now have " + str(coins) + " coins.\n")
                    typing("You drink your gas station coffee. The taste leaves you dissatisfied.\n")
                    typing("Please press enter to continue.\n")
                    input("> ")
            elif coffee == "2":
                black_coffee_price = 8
                if coins < black_coffee_price:
                    clear()
                    typing("You do not have enough coins to buy this.\n")
                    time.sleep(2)
                else:
                    clear()
                    coins = coins - black_coffee_price
                    typing("You now have " + str(coins) + " coins.\n")
                    typing("You drink your black coffee. Nothing special, just makes you feel warm inside.\n")
                    typing("Please press enter to continue.\n")
                    input("> ")
            elif coffee == "3":
                cappuccino_price = 11
                if coins < cappuccino_price:
                    clear()
                    typing("You do not have enough coins to buy this.\n")
                    time.sleep(2)
                else:
                    clear()
                    coins = coins - cappuccino_price
                    typing("You now have " + str(coins) + " coins.\n")
                    typing("You drink your cappuccino. It tastes very good!\n")
                    typing("Please press enter to continue.\n")
                    input("> ")
            elif coffee == "4":
                latte_price = 13
                if coins < latte_price:
                    clear()
                    typing("You do not have enough coins to buy this.\n")
                    time.sleep(2)
                else:
                    clear()
                    coins = coins - latte_price
                    typing("You now have " + str(coins) + " coins.\n")
                    typing("You drink your latte. The combonation of milk and coffee is sensational!\n")
                    typing("Please press enter to continue.\n")
                    input("> ")
            elif coffee == "5":
                elvern_berry_tea_price = 16
                if coins < elvern_berry_tea_price:
                    clear()
                    typing("You do not have enough coins to buy this.\n")
                    time.sleep(2)
                else:
                    clear()
                    coins = coins - elvern_berry_tea_price
                    typing("You now have " + str(coins) + " coins.\n")
                    typing("You drink your elvern berry cold brew tea. The sweetness along with some tartness just makes your day!\n")
                    typing("Please press enter to continue.\n")
                    input("> ")
        elif city_options == "2":
            clear()
            print("Welcome to Aaron's Apparel!")
            print("You have " + str(coins) + " coins.")
            print("What would you like to buy?")
            print("1) Hat")
            print("2) Shirt")
            print("3) Pants")
            print("4) Shoes")
            print("5) Outerwear")
            print("6) Items")
            apparel = ""
            while apparel not in ["1", "2", "3", "4", "5", "6"]:
                apparel = input("> ")
            if apparel == "1":
                clear()
                print("HATS")
                print("1) Fedora - 15 coins")
                print("2) Baseball Cap - 10 coins")
                print("3) I <3 Talera Hat - 5 coins")
                print("4) Bike Helmet - 20 coins")
                hats = ""
                while hats not in ["1", "2", "3"]:
                    hats = input("> ")
                if hats == "1":
                    fedora_price = 15
                    if coins < fedora_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - fedora_price
                        hat = "Fedora"
                        typing("You now have " + str(coins) + " coins.\n")
                        typing("I think this fedora looks nice on you! You look like a secret agent...\n")
                        typing("Please press enter to continue.\n")
                        input("> ")
                if hats == "2":
                    baseball_cap_price = 10
                    if coins < baseball_cap_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - baseball_cap_price
                        hat = "Baseball Cap"
                        typing("You now have " + str(coins) + " coins.\n")
                        typing("I think this baseball cap looks nice on you!\n")
                        typing("Please press enter to continue.\n")
                        input("> ")
                if hats == "3":
                    talera_hat_price = 5
                    if coins < talera_hat_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - talera_hat_price
                        hat = "I <3 Talera Hat"
                        typing("You now have " + str(coins) + " coins.\n")
                        typing("Good choice! I <3 Talera!\n")
                        typing("Please press enter to continue.\n")
                        input("> ")
                if hats == "4":
                    talera_hat_price = 20
                    if coins < talera_hat_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - talera_hat_price
                        hat = "Bike Helmet"
                        typing("You now have " + str(coins) + " coins.\n")
                        typing("Nothing like a bike helmet to keep you nice and safe!\n")
                        typing("Please press enter to continue.\n")
                        input("> ")
            elif apparel == "2":
                clear()
                print("SHIRTS")
                print("1) White T-Shirt - 10 coins")
                print("2) I <3 LT T-Shirt - 15 coins")
                shirts = ""
                while shirts not in ["1", "2"]:
                    shirts = input("> ")
                if shirts == "1":
                    white_Tshirt_price = 10
                    if coins < white_Tshirt_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - white_Tshirt_price
                        shirt = "White T-Shirt"
                        typing("You now have " + str(coins) + " coins.\n")
                        typing("This is a nice, clean, white shirt. Don't get it dirty!\n")
                        typing("Please press enter to continue.\n")
                        input("> ")
                if shirts == "2":
                    talera_shirt_price = 15
                    if coins < talera_shirt_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - talera_shirt_price
                        shirt = "I <3 LT T-Shirt"
                        typing("You now have " + str(coins) + " coins.\n")
                        if hat == "I <3 Talera Hat":
                            typing("It fits nice with the hat. Now you are a REAL fan!\n")
                        else:
                            typing("You should also try to get the matching hat!\n")
                        typing("Please press enter to continue.\n")
                        input("> ")
            elif apparel == "3":
                clear()
                print("PANTS")
                print("1) Blue Jeans - 15 coins")
                print("2) Gym Shorts - 15 coin")
                pair_of_pants = ""
                while pair_of_pants not in ["1", "2"]:
                    pair_of_pants = input("> ")
                if pair_of_pants == "1":
                    blue_jeans_price = 15
                    if coins < blue_jeans_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - blue_jeans_price
                        pants = "Blue Jeans"
                        typing("You now have " + str(coins) + " coins.\n")
                        typing("Yay! Classic blue jeans!\n")
                        typing("Please press enter to continue.\n")
                        input("> ")
                elif pair_of_pants == "2":
                    gym_shorts_price = 15
                    if coins < gym_shorts_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - gym_shorts_price
                        pants = "Gym Shorts"
                        typing("You now have " + str(coins) + " coins.\n")
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
                    if coins < ripoff_sneakers_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - ripoff_sneakers_price
                        shoes = "Off-brand Ripoff Sneakers"
                        typing("You now have " + str(coins) + " coins.\n")
                        typing("Oh, nice! You got some cool sneakers! Hmm... something seems different...\n")
                        typing("Please press enter to continue.\n")
                        input("> ")
                elif shoes_choose == "2":
                    hiking_boots_price = 10
                    if coins < hiking_boots_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - hiking_boots_price
                        shoes = "Hiking Boots"
                        typing("You now have " + str(coins) + " coins.\n")
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
                    if coins < winter_coat_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - winter_coat_price
                        outerwear = "Winter Coat"
                        typing("You now have " + str(coins) + " coins.\n")
                        typing("A nice coat to keep you warm through the cold winter days.\n")
                        typing("Please press enter to continue.\n")
                        input("> ")
                elif outerwear_choose == "3":
                    necktie_price = 10
                    if coins < necktie_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - necktie_price
                        outerwear = "Necktie"
                        typing("You now have " + str(coins) + " coins.\n")
                        typing("Pretty formal, eh?\n")
                        typing("Please press enter to continue.\n")
                        input("> ")
                elif outerwear_choose == "3":
                    bowtie_price = 10
                    if coins < bowtie_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - bowtie_price
                        outerwear = "Bowtie"
                        typing("You now have " + str(coins) + " coins.\n")
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
                    if coins < trusty_backpack_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - trusty_backpack_price
                        item = "Trusty Backpack"
                        typing("You now have " + str(coins) + " coins.\n")
                        typing("Just like it says in the name, it is VERY trusty!\n")
                        typing("Please press enter to continue.\n")
                        input("> ")
                if items == "2":
                    hiking_stick_price = 10
                    if coins < hiking_stick_price:
                        clear()
                        typing("You do not have enough coins to buy this.\n")
                        time.sleep(2)
                    else:
                        clear()
                        coins = coins - hiking_stick_price
                        item = "Hiking Stick"
                        typing("You now have " + str(coins) + " coins.\n")
                        typing("A nice looking stick to support you while hiking.\n")
                        typing("Please press enter to continue.\n")
                        input("> ")
        elif city_options == "3":
            print("Welcome to THE DOCKS!")
            print("At the docks, you can go fishing for some loot, or have some tasty fish!")
            print("You have " + str(coins) + " coins.")
            print("1) Go Fishing - 5 coins")
            docks_options = ""
            while docks_options not in ["1"]:
                docks_options = input("> ")
            if docks_options == "1":
                if coins < 5:
                    clear()
                    typing("You do not have enough coins to buy this.\n")
                    time.sleep(2)
                else:
                    clear()
                    functions.textloading(1, "FISHING")
                    fish_options = [""]
        elif city_options == "4":
            clear()
            typing("Welcome to your trophy room!\n")
            if trophies == []:
                typing("Hmm... Seems like you do not have any trophies. How do you fix this? GO DO SOME QUESTS!!!\n")
            else:
                for trophy in trophies:
                    typing("Here are your trophies:\n")
                    typing(trophy)
            typing("Please press enter to continue.\n")
            input("> ")
        elif city_options == "5":
            clear()
            typing("Here is your inventory:\n")
            print("Hat - " + hat)
            print("Shirt - " + shirt)
            print("Pants - " + pants)
            print("Shoes - " + shoes)
            print("Outerwear - " + outerwear)
            print("Item - " + item)
            typing("Please press enter to continue.\n")
            input("> ")
        elif city_options == "6":
            clear()
            typing("You have now left the city.\n")
            time.sleep(2)
            clear()
            levels.waiting_room()
