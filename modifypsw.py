import tkinter
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x225")
app.title("Password Changer")
app.resizable(False, False)

def changepsw(event):
    entryval = entry.get()
    try:
       int(entryval)
    except:
       psw_no.pack()
       psw_yes.pack_forget()
       return
    else:
       psw_yes.pack()
       psw_no.pack_forget()
    f = open("pin.txt", "w")
    f.write(str(entryval))
    f.close()


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

psw_yes = customtkinter.CTkLabel(master=frame_1, text="Changed PIN succesfully.")
psw_no = customtkinter.CTkLabel(master=frame_1, text="PIN should be a number")

label_1 = customtkinter.CTkLabel(master=frame_1, text="Change current PIN: to: ", justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)

label_2 = customtkinter.CTkLabel(master=frame_1, text="Press <enter> to confirm.", justify=tkinter.LEFT)
label_2.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="PIN:")
entry.pack(pady=12, padx=10)

app.bind("<Return>", changepsw)
app.mainloop()