import random as rnd
import secrets
import logging

#initiate the logs
logging.basicConfig(filename="randomizer_logs.log", level=logging.INFO, 
                    format="%(asctime)s - %(message)s")

#set the program to run
running = True

# Function to clear the console 
def clear_console():
    print("\n" * 100)

# Function to gracefully close the program
def close_program():
    global running
    print("Thank you for using the Randomizer Application!")
    running = False         #set program to false to shut down
    return

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
    while True:  # Loop to handle repeated invalid input
        try:  # Adding input validation
            choice2 = int(input("How many things do you want randomized?: "))
            logging.info(f"User wants to randomize {choice2} items.")
            if choice2 <= 0:  # Validate input is positive
                raise ValueError("The number must be greater than zero.")
            print("Enter your choices, then click Enter after each: ")
            items.clear()
            for i in range(choice2):  # Use a for loop for cleaner iteration
                item = input(f"Item {i+1}: ")
                items.append(item)
                logging.info(f"Item added: {item}")
            return items  # Break out of the loop after successful input
        except ValueError as e:
            print(f"Invalid Input: {e}")
            # No need for continue, the loop naturally repeats
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting gracefully.")
            break


#Randomizer prompt using the input array to choose a random object
while running:
    choice1 = input("Do you have something to be randomized? Y or N:  ")
    if choice1.lower() == "y":
        clear_console()                     #Clears the console for hygiene
        items = GetInput()
        while True: 
            choiceRnd = secrets.choice(items)
            logging.info(f"Randomized choice: {choiceRnd}")
            print ("*****************************")
            print (f">>> Your choice will be {choiceRnd}! <<<")
            contInput = input("Do you want to randomize again with the same inputs? (Y or N): ").lower()
            if contInput == "y":
                logging.info("User chose to randomize again with the same inputs.")
                continue             
            if contInput == "n":
                logging.info("User chose to stop randomizing with the same inputs.")
                items.clear()
                logging.info("Clearing item list to free memory.")
                break

    elif choice1 == "N" or choice1 == "n":
        logging.info("User exited the program.")
        close_program()             #closes the program gracefully without hooking into the kernel
