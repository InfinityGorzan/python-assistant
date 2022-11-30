import os
import time
import tkinter
import os.path
from os import path
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("595x170")
root.title("Assistant - Login")

if not path.exists("pin.txt"):
    os.startfile("modifypsw.py")

def login(self):
    acpsw = open("pin.txt", "r").read()
    rpsw = psw_entry.get()
    if rpsw == acpsw:
        correct_psw.pack(pady=9, padx=9)
        correct_note.pack(pady=9, padx=9)
        incorrect_psw.destroy()
        time.sleep(1.2)
        os.startfile("home.py")
    else:
        incorrect_psw.pack(pady=9, padx=9)
        correct_psw.pack_forget()

frame_1 = customtkinter.CTkFrame(master=root)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

psw_entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="PIN:")
psw_entry.pack(pady=12, padx=10)

incorrect_psw = customtkinter.CTkLabel(master=frame_1, text="Incorrect Password! Try again.",justify=tkinter.LEFT)
correct_psw = customtkinter.CTkLabel(master=frame_1, text="Correct Password! We'll log you in in a second",justify=tkinter.LEFT)
correct_note = customtkinter.CTkLabel(master=frame_1, text="Keep this window open to keep the other window. Just minimize this window.",justify=tkinter.LEFT)

root.bind("<Return>", login)
root.mainloop()