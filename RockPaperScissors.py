#import required libs
from tkinter import *
from tkinter import ttk
import random


#initialize window
root = Tk()
root.geometry('520x150')
root.title('Rock Paper Scissor')
root.config(bg='gainsboro')
root.resizable(0,0)

root.attributes('-toolwindow', True)

root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)


inputframe = ttk.Frame(root)
inputframe.grid(column=0, row=0, padx=50, pady=30, sticky=W)

inputframe.columnconfigure(0, weight=2)
inputframe.columnconfigure(1, weight=2)

ttk.Label(inputframe, text='Choose one: \nrock, paper \nor scissors', font='calibri 12 bold').grid(column=0, row=0, sticky=W)
user_take = StringVar()
keyword = ttk.Entry(inputframe, width=30, textvariable=user_take)
keyword.focus()
keyword.grid(column=1, row=0, sticky=E)


comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick == 'paper'
else:
    comp_pick = 'scissors'

Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
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
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')
    

ttk.Label(inputframe, text='Result: ', font='calibri 12 bold').grid(column=0, row=1, sticky=SW)
win = ttk.Entry(inputframe, width=30, textvariable= Result)
win.grid(column=1, row=1, sticky=E)

buttonframe = ttk.Frame(root)
buttonframe.grid(column=1, row=0, padx=30, pady=30, sticky=E)

def Reset():
    Result.set('')
    user_take.set('')

def Exit():
    root.destroy()

ttk.Button(buttonframe, text='PLAY', command=play).grid(column=0, row=0, sticky=N)
ttk.Button(buttonframe, text='RESET', command=Reset).grid(column=0, row=1, sticky=W)
ttk.Button(buttonframe, text='EXIT', command=Exit).grid(column=0, row=2, sticky=S)


root.mainloop()
