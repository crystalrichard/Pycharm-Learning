from tkinter import *

import classes as classes
import customtkinter
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import numpy as np
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

font=customtkinter.CTkFont(family="Arial", size=25)
font=("Arial", 25)


label = customtkinter.CTkLabel(master=frame, text="Login System", font="Arial", size=25)
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password",)
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)


checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()





mainwindow = Tk()
mainwindow.configure(background='#CDCDCD')
img = 0
page_title = "Classification of leukemia cells"
img_path = 0
img_categories = "All\nhem"
category = "The Result is : "


def target_size(param, param1):
    pass


def picture_choose_btn_comm(classes=None, result_lbl=None, y_pred=None, img_frm=None, pred=None):
    global img, img_path, category
    if not img_path:
        return
    img_open = Image.open(img_path)
    if img_open.width > 500 and img_open.height > 500:
        img_open.thumbnail((800, 600))
    img = ImageTk.PhotoImage(img_open)


    canvas = Canvas(master=img_frm, width=600, height=600)
    canvas.grid(row=0, column=1)
    canvas.create_image(250, 250, anchor=CENTER, image=img)


     image = tf.keras.preprocessing.image.load_img(path=img_path,target_size(224, 224))
     input_arr = tf.keras.preprocessing.image.img_to_array(image)
     input_arr = np.array([input_arr])
     Model = tf.keras.models.load_model('model80epochs.h5')
     y_Pred = Model.predict(input_arr)
     classes = classes[np.argma(y_pred)]
     category = classes[np.argmax(y-pred)]
     result_lbl['text'] = category



#widgets:

col1_frm = Frame(master=mainwindow)
col1_frm.grid(row=0, column=1)

col0_frm = Frame(master=mainwindow)
col0_frm.grid(row=0, column=0)

result_lbl = Label(master=col1_frm, text=category, relief='raised', pady=3, padx=5, borderwidth=3)
result_lbl.grid(row=0, column=0, pady=10)

img_frm = Frame(master=col1_frm, relief='groove', borderwidth=2, width=500, height=500, bg='#8EF0F7')
img_frm.grid(row=1, column=0)

#Window Settings:
mainwindow.columnfigure(0, minsize=100, weight=1)
mainwindow.rowconfigure(0,minsize=100, weight=1)
mainwindow.columnconfigure(1, minsize=500, weight=1)
mainwindow.geometry("1000x800")
mainwindow.title(page_title)


mainwindow.mainloop()




#run existing pycode:
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="app_name",
    version="0.1",
    description="app_description",
    executables=[Executable("app_file.py", base=base)],
)