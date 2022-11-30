import os
import tkinter
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

aot = open("alwaysontop.txt", 'r').read()
aot = int(aot)
if aot == 2:
    aot = 0

app = customtkinter.CTk()
app.geometry("400x580")
app.title("Assistant")
app.wm_attributes("-topmost", aot)

def dat():
    os.startfile("apporgame\dat.py")

def rps():
    os.startfile("apporgame\\rps.py")

def rtd():
    os.startfile("apporgame\\rtd.py")

def aot_fc():
    os.startfile("alwaysontop.py")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

info = customtkinter.CTkLabel(master=frame_1, text="Select option below:", justify=tkinter.LEFT)
info.pack(pady=12, padx=10)

aot_ops_btn = customtkinter.CTkButton(master=frame_1, text="Always On Top Settings", command=aot_fc).pack()
aot_ops_btn

button_dat = customtkinter.CTkButton(master=frame_1, text="View date and time", command=dat).pack(pady=12, padx=10)
button_dat
button_rps = customtkinter.CTkButton(master=frame_1, text="Play RPS (Rock Paper Scissors)", command=rps).pack(pady=12, padx=10)
button_rps
button_rtd = customtkinter.CTkButton(master=frame_1, text="Roll the dice", command=rtd).pack(pady=12, padx=10)
button_rtd

app.mainloop()