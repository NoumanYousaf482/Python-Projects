from tkinter import *
import random

# initialize window

root = Tk()                   # use to initialize tkinter to c reate window
root.geometry('400x400')      # set window width and heights
root.resizable(0,0)         # we can fix the size of window
root.title('DataFlair-Rock,Paper,Scissors')
root.config(bg = 'seashell3') # use to set color of background

# headings

Label(root, text = 'Rock, Paper, Scissors' , font='arial 20 bold', bg='seashell2') .pack() # widget use to display text that can not be modified

# User Choice

user_take = StringVar()
Label(root, text = 'choose any one: rock ,paper ,scissors ' , font='arial 15 bold' , bg='seashell2') .place(x = 20,y = 70)
Entry(root, font='arial 15', textvariable=user_take , bg='antiquewhite2') .place (x=90 , y=130
)

# for computer choice

comp_pick = random.randint(1,3) # function will randomly take number
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

# function to start game
    
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you bothselect same')
    elif user_pick =='rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win,computer select paper')
    else:
        Result.set('invalid: choose any one --rock, paper, scissors')

# function to reset
        
def Reset():
    Result.set("")
    user_take.set("")

# function to exit
    
def Exit():
    root.destroy()

# Define Buttons
    
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)


root.mainloop()