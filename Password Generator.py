from tkinter import *
import random

window = Tk()
window.title('Password Generator')

word_list = ['dog', 'cat', 'dollar', 'mouse', 'word', 'pass', 'sign', 'sing', 'computer', 'keyboard']
seperators = ['%', '!', '#', '$', '<', '>', '@']
def password():
    (random.choice(word_list) + random.choice(seperators) + random.choice(word_list) \
    + str(random.randint(0,100)) + random.choice(seperators))

def password_gen():
    print(password)
    display_area.config(password, fg='black', bg = 'white')


display_area = Label(window, text ="")
display_area.pack()
    

canvas = Canvas(window, width=400,height=400)

generator_button = Button(window, text= 'Generate Password!', command = password_gen)
generator_button.pack()

window.after(500, password)

window.mainloop()
