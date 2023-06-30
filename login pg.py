from tkinter import label

import customtkinter
import customtkinter as customtkinter
import frame as frame
import login as login
from customtkinter import CTkLabel

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")


def login():
    print("Test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


Label = customtkinter.CTkLabel(master=frame, text="Login System", text_font=("Roboto", 24)
label.pack(pady=12, padx=10)


entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
enrty1.pack(pady=12, padx=10)


entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*" )
entry2.pack(pady=12, padx=10)


button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)


checkbox = customtkinter.CTkCheckbox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()