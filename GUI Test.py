from tkinter import *

window = Tk()
window.title("My first GUI")

def hello_function():
    print("Hello World!")
    display_area.config(text = "Hello World!", \
fg="yellow", bg = "black")

button1 = Button(window, text="Click Me", command = hello_function)
button1.pack()

display_area = Label(window, text ="")
display_area.pack()

canvas = Canvas(window, width=400,height=400)
canvas.pack()

circle = canvas.create_oval(100,200,130,230, fill = 'red')
blue_rect = canvas.create_rectangle(50,50,70,80, fill = 'blue')
screen_message = canvas.create_text(200,200, text = 'Welcome!', \
fill='black', font = ('Helvetica', 30))

img = PhotoImage(file="greenChar.gif")
mychar = canvas.create_image(100,100,image = img)

def move_circle(event):
    key = event.keysym
    if key == "Right":
        canvas.move(circle,10,0)
    elif key == "Left":
        canvas.move(circle,-10,0)
    elif key == "Up":
        canvas.move(circle,0,-10)
    elif key == "Down":
        canvas.move(circle,0,10)
    elif key == "w":
        canvas.move(circle,0,-10)
    elif key == "s":
        canvas.move(circle,0,10)
    elif key == "d":
        canvas.move(circle,10,0)
    elif key == "a":
        canvas.move(circle,-10,0)

canvas.bind_all('<Key>', move_circle)

def exit_program():
    window.destroy()

qbutton = Button(window, text="Exit", command = exit_program)
qbutton.pack()

window.mainloop()
    
