#defines a function where it creates a line in the output
def linespace():
    print("             ")

#enter amount of dice
import time
number_dice = input("Please enter a number of dice to roll. ")
number_dice = int(number_dice)
ready = input("Press any key to continue... ")
time.sleep(3)

import random
#roll dice function
def roll_dice(n):
    dice = []

    for i in range(n):
        dice.append(random.randint(1,6))
    return dice
#user roll
user_rolls = roll_dice(number_dice)

print("User's first roll:", user_rolls)
#reroll or hold 
user_choice = input("Enter h to hold a number or r to re-roll a number. ")
while len(user_choice) != number_dice:
    print("You must enter", number_dice, "choices")
    user_choice = input("Enter h to hold a number or r to re-roll a number. ")

#reroll function
def roll_again(choices, dice_list):
    print("Rolling again")
    time.sleep(3)
    for i in range(len(choices)):
        if choices[i] == "r":
            dice_list[i] = random.randint(1,6)
    time.sleep(3)

roll_again(user_choice, user_rolls)
print("Player's new roll: ", user_rolls)

#computer roll
print("Computer's turn!")
computer_rolls = roll_dice(number_dice)
print("Computer's first roll:" , computer_rolls)

#decide winner
def find_winner(cdice_list, udice_list):
    computer_total = sum(cdice_list)
    user_total = sum(udice_list)
    print("The computer's total:", computer_total)
    linespace()
    print("Your total:", user_total)
    if computer_total > user_total:
        print("The computer wins!")

    elif user_total > computer_total:
        print("You win!")
        
    else:
        print("You and the computer tied!")
find_winner(computer_rolls,user_rolls)
