import random
import tkinter
import customtkinter
from random import randint

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

w = 400
h = 200
app_len = str(w) + "x" + str(h)
app = customtkinter.CTk()
app.geometry(app_len)
app.title("Roll the Dice")
app.resizable(False, False)

def randnum(minint, maxint):
    return random.randint(int(minint), int(maxint))

def roll():
    n = randnum(1, 6)
    r.set(n)

r = tkinter.IntVar()
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

customtkinter.CTkLabel(master=frame_1, text="Roll a dice!", justify=tkinter.LEFT).pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, text="ROLL", command=roll)
button_1.pack(pady=12, padx=10)

result = customtkinter.CTkLabel(master=frame_1, textvariable=r)
result.pack()
app.mainloop()