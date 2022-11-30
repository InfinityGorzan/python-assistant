import tkinter
import random
import customtkinter
from random import randint
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x300")
app.title("Rock Paper Scissors (RPS)")
app.resizable(False, False)

def randnum(minint, maxint):
    return random.randint(minint, maxint)

def check(event):
    urchoice = choice.get()
    botchoice = randnum(1, 3)
    rootwin = tkinter.Toplevel(app)
    rootwin.title("Score")
    rootwin.configure(bg="black")
    rootwin.geometry("200x100")
    rootwin.resizable(False, False)
    chance = tkinter.StringVar()
    you = tkinter.StringVar()
    bot = tkinter.StringVar()
    if urchoice == botchoice:
        chance.set("TIE.")
        if urchoice == 1:
            you.set("Your choice: ROCK")
            bot.set("Bot choice: ROCK")
        elif urchoice == 2:
            you.set("Your choice: PAPER")
            bot.set("Bot choice: PAPER")
        else:
            you.set("Your choice: SCISSORS")
            bot.set("Bot choice: SCISSORS")
    elif urchoice == 1:
        if botchoice == 2:
            chance.set("You lose.")
            you.set("Your choice: ROCK")
            bot.set("Bot choice: PAPER")
        elif botchoice == 3:
            chance.set("You win.")
            you.set("Your choice: ROCK")
            bot.set("Bot choice: PAPER")
    elif urchoice == 2:
        if botchoice == 1:
            chance.set("You win.")
            you.set("Your choice: PAPER")
            bot.set("Bot choice: ROCK")
        elif botchoice == 3:
            chance.set("You lose.")
            you.set("Your choice: PAPER")
            bot.set("Bot choice: SCISSORS")
    else:
        if botchoice == 1:
            chance.set("You lose")
            you.set("Your choice: SCISSORS")
            bot.set("Bot choice: ROCK")
        elif botchoice == 2:
            chance.set("You win.")
            you.set("Your choice: SCISSORS")
            bot.set("Bot choice: PAPER")
    
    tkinter.Label(rootwin, textvariable=chance).pack()
    tkinter.Label(rootwin, textvariable=you).pack()
    tkinter.Label(rootwin, textvariable=bot).pack()

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

customtkinter.CTkLabel(master=frame_1, text="Select. Press <enter> to confirm.", justify=tkinter.LEFT).pack(pady=12, padx=10)

choice = tkinter.IntVar(value=1)

rock = customtkinter.CTkRadioButton(master=frame_1, text="ROCK", variable=choice, value=1)
rock.pack(pady=12, padx=10)

paper = customtkinter.CTkRadioButton(master=frame_1, text="PAPER", variable=choice, value=2)
paper.pack(pady=12, padx=10)

scissors = customtkinter.CTkRadioButton(master=frame_1, text="SCISSORS", variable=choice, value=3)
scissors.pack(pady=12, padx=10)

def rock_fc(event):
    choice.set(1)

def paper_fc(event):
    choice.set(2)

def scissor_fc(event):
    choice.set(3)

customtkinter.CTkLabel(master=frame_1, text="Use <F(1 for rock, 2\n for paper, 3 for scissors)> to select.", justify=tkinter.LEFT).pack(pady=12, padx=10)

app.bind("<Return>", check)
app.bind("<F1>", rock_fc)
app.bind("<F2>", paper_fc)
app.bind("<F3>", scissor_fc)

app.mainloop()