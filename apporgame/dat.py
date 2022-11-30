import tkinter
import datetime
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x180")
app.title("Find date and time")
app.resizable(False, False)
d_val = tkinter.StringVar()
d = datetime.datetime.now()
d_val.set(str(d))

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

dat = customtkinter.CTkLabel(master=frame_1, textvariable=d_val, justify=tkinter.LEFT)
def find_dat():
    d = datetime.datetime.now()
    d_val.set(str(d))
    dat.pack(pady=12, padx=10)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Date and time", justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, text="Find date and time", command=find_dat)
button_1.pack(pady=12, padx=10)

app.mainloop()