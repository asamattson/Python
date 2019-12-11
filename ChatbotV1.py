#this is version 1 of the chat bot, it's only using certain inouts, but chatbot learning and other conversations will be added later.
#get the user's name

name = input("Hello. Im Clara the chatbot. What's your name?: ")
print("Hello ", name, " , that's a nice name")

#get the current year for 100 function
year = input("Im not very good with dates, \
whats the year again?")
print("Ah! Time flies doesn't it?")
year = int(year)

#get the user's guess of the Clara's age, will say its correct for whatever input, only for version 1 though.
age = input(name + ", I have a challenge for you! Guess my age!")
print("Wow! You got it! I'm " + age)

#100 year function
age = int(age)
timeLeft = (100 - age)
timeLeft = int(timeLeft)
print("I will be 100 in ", timeLeft, " years!")
print("I will turn 100 in ", int(year) + timeLeft)
