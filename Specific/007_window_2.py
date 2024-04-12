from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image ,ImageTk
import os

def shut_down():
    pass
    os.system("shutdown /s /t 0")
    root.destroy()

def restart():
    pass
    os.system("shutdown /r /t 1")
    root.destroy()

def sleep():
    pass
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    root.destroy()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("800x420+450+200")
wid = 800
hgt = 420
root.title("Shut Down Windows")
root.iconbitmap(os.path.join( os.getcwd(), r"Specific\beauty.ico" ))
root.resizable(False,False)
my_can=Canvas(root , width=wid , height=hgt, bg="black", highlightcolor="#3c5390", borderwidth=0 )
my_can.pack( fill="both", expand=True)
img_1 = Image.open(os.path.join( os.getcwd(), r"Specific\wynonna_background.jpg" ))
pht_1 = ImageTk.PhotoImage(img_1.resize((1000,525), Image.Resampling.LANCZOS))
my_can.create_image( 0, 0 , image=pht_1 , anchor="nw")

shut = ctk.CTkButton(master=root, text="Shut Down", text_font=("Berlin Sans FB",20), width=150, height=20, corner_radius=10,
         fg_color="#ca0000", hover_color="#dc3333", bg_color="#5c373f", border_width=0, command = shut_down)
shut_win = my_can.create_window(800 , 355 , anchor="nw" , window=shut )

res = ctk.CTkButton(master=root, text="Restart", text_font=("Berlin Sans FB",20), width=153, height=20, corner_radius=10,
         fg_color="#ca0000", hover_color="#dc3333", bg_color="#f36b39", border_width=0, command = restart)
res_win = my_can.create_window(800 , 415 , anchor="nw" , window=res )

slp = ctk.CTkButton(master=root, text="Sleep", text_font=("Berlin Sans FB",20), width=153, height=20, corner_radius=10,
         fg_color="#ca0000", hover_color="#7d0000", bg_color="#f4762a", border_width=0, command = sleep)
slp_win = my_can.create_window(800 , 475 , anchor="nw" , window=slp )

root.mainloop()
