import random as rnd 
import sys
import os

#Store the input strings to be randomized
items = []

#Title
print ("*********************************")
print ("*********************************")
print ("Welcome to the Randomizer Module!")
print ("*********************************")
print ("*****Created by NinjaRose********")
print ("*********************************")
print ("*********************************")

#function to get the Input from the user and add it to the item array
def GetInput():     
    choice2 = int(input("How many things do you want randomized?:  "))
    print ("Enter your choices, then click Enter after each: ")
    i = 0
    items.clear()
    while i < choice2:
        items.append(input())
        i += 1
    return items

#Randomizer prompt using the input array to choose a random object
while True:
    choice1 = input("Do you have something to be randomized? Y or N:  ")
    if choice1.lower() == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        items = GetInput()
        while True: 
            choiceRnd = rnd.choice(items)
            print ("*****************************")
            print (f">>> Your choice will be {choiceRnd}! <<<")
            contInput = input("Do you want to randomize again with the same inputs? (Y or N): ").lower()
            if contInput == "y":
                continue             
            if contInput == "n":
                break

    elif choice1 == "N" or choice1 == "n":
        sys.exit("Closing now")
        
