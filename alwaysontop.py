import tkinter
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

w = 400
h = 275
app_length = str(w) + "x" + str(h)
app = customtkinter.CTk()
app.geometry(app_length)
app.title("Always on top settings")
app.wm_attributes("-topmost", 1)
#app.wm_attributes('-fullscreen', 'True')

app.overrideredirect(1)
ws = app.winfo_screenwidth()
hs = app.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
app.geometry('%dx%d+%d+%d' % (w, h, x, y))

def apply():
    aot = str(alwaysontop.get())
    with open("alwaysontop.txt", 'w') as out_file:
       out_file.write(aot)
    app.destroy()

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

customtkinter.CTkLabel(master=frame_1, text="Settings for Always on Top:", justify=tkinter.LEFT).pack(pady=12, padx=10)

aots = open("alwaysontop.txt", 'r').read()
aots = int(aots)
alwaysontop = tkinter.IntVar(value=aots)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, text="ON", variable=alwaysontop, value=1)
radiobutton_1.pack(pady=12, padx=10)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, text="OFF", variable=alwaysontop, value=2)
radiobutton_2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame_1, text="Apply & Close", command=apply)
button.pack(pady=12, padx=10)

customtkinter.CTkLabel(master=frame_1, text="Refresh to apply when applied.", justify=tkinter.LEFT).pack(pady=12, padx=10)

app.bind("<Return>", apply)

app.mainloop()