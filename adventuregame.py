import turtle
import sys
import random

print("-=-=-=-=-= The Adventures of Scalado =-=-=-=-=-=-")
print("Your eyes slowly open, and they are brutally penetrated by sunlight. After clearing your eyes, \
you can see that you are in a forest.")
print("You see a compass on the ground. You pick it up.")
print("You have picked up a compass!")
print("You see something hanging from a tree. It appears to be a box hanging by string. \
You look to your left, and you see a house in the distance. \
You aim your compass towards it and it reads north.")

path = input('Where do you want to go?')
while not(path == 'north' or path == 'tree'):
    path = input("I don't understand.")
if path == 'north':
    #house path
    print("You head North towards the house. Once you get there, you approach the door. Its locked. \
    You look around, and you see a ladder going to the roof, and a window on the side of the house.")
    path = input("Would you like to climb the ladder or go to the window ")
    while not(path == "ladder" or path == "window"):
        path = input("Please enter 'ladder' or 'window' ")
    if path == 'ladder':
        print("You climb the ladder then get on the roof. You hear a crackle sound, and then the roof breaks.")
        print("You get up, and you shake it off. You look over, and you see a sword looking up next to the furnace. \
        You realize you could have landed on that.")
    else:
        print("You go to the window, and you notice that its slightly open. You lightly push it in, then you enter the house.")
        print("You look near the furnace, and you see a sword prompted blade side up, shining.")
    print("You look around, and you see a bundle of berries. You cant recognize them.")
    berrypath = input('Do you want to pick up the berries? ')
    while not(berrypath == 'yes' or berrypath == 'no'):
        berrypath = input("Please enter yes or no. ")
    if berrypath == 'yes':
        print("You picked up the berry bunch. You have a compass and a bunch of mysterious berries.")

    else:
        print("You leave the berries on the table.")

    print("You look at the sword near the furnace. You decide to pick it up.")
    print("You look around and you dont see anything. You decide to explore. Opening doors just results in empty rooms, or rooms with just a bed.")
    print("You go back to the furnace room, and see one last door. You try to open it, but it's locked. You end up leaving and going back to where you woke up.")
    print("Looking around, you only see the tree with the box hanging on it. Would you like to climb it?")
    
    #treepath after housepath
    
    while not(path == "yes" or path == "no"):
        path = input("")
    if path == 'yes':
        print("You approach the tree.")
        print("You start climbing the tree, and you notice that there is a forked path.")
        print("There is a branch on the left that is more reachable, but you need to climb, then decend on the right side from the very top of the tree. It will take longer.")
        print("The branch on the right is further up, but you would only have to make one more reach to get to the box.")

        branchpath = input("Which branch do you climb onto?  ")
        while not(branchpath == "left" or branchpath == "right"):
            branchpath = input("Please enter 'left' or 'right' ")
        if branchpath == "left":
            print("You grab onto the left branch, and begin climbing. You reach the top of the tree, and you begin to decend onto the branch with the box hanging on it.")
            print("You grab the box and open it. There is a key.")
            print("You take the key.")
            print("You climb down the tree.")

        else:
            print("You grab onto the right branch and you try to get footing on the tree bark. Your foot slips. You fall down, and you brutally hit your back on a branch.")
            deathconf = input("You have died.")
            sys.exit()

else:
    #tree path        
    print("You approach the tree.")
    print("You start climbing the tree, and you notice that there is a forked path.")
    print("There is a branch on the left that is more reachable, but you need to climb, then decend on the right side from the very top of the tree. It will take longer.")
    print("The branch on the right is further up, but you would only have to make one more reach to get to the box.")

    branchpath = input("Which branch do you climb onto?  ")
    while not(branchpath == "left" or branchpath == "right"):
        branchpath = input("Please enter 'left' or 'right' ")
    if branchpath == "left":
        print("You grab onto the left branch, and begin climbing. You reach the top of the tree, and you begin to decend onto the branch with the box hanging on it.")
        print("You grab the box and open it. There is a key.")
        print("You take the key.")
        print("You climb down the tree.")

    else:
        print("You grab onto the right branch and you try to get footing on the tree bark. Your foot slips. You fall down, and you brutally hit your back on a branch.")
        deathconf = input("You have died.")
        sys.exit()

print("You look around and notice the unexplored house do you go there?")

    




